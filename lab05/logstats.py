def parse_event(line):
    parts = line.split(" ", 2)
    if len(parts) != 3:
        raise ValueError("Недостаточно данных")
    time, level, message = parts
    level = level.strip()
    message = message.strip()
    if level not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
        raise ValueError("Неизвестный уровень")
    return {"time": time, "level": level, "message": message}

def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts

def top_errors(lines, n):
    errors_count = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                errors_count[msg] = errors_count.get(msg, 0) + 1
        except ValueError:
            pass
    sorted_errors = sorted(errors_count.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in sorted_errors[:n]]

def format_report(counts, errors):
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(level + ": " + str(counts[level]))
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, count in errors:
        lines.append("- " + msg + " — " + str(count))
    return "\n".join(lines) + "\n"