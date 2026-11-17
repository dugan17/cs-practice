
[D[A[A[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C


[A


def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Не 3 поля")
    city, temp_raw, date = parts
    if not city or not date:
        raise ValueError("Пустой город или дата")
    try:
        temp = float(temp_raw)
    except ValueError:
        raise ValueError("Температура не число")
    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records

def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temp"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}

def warmest_city(records: list[dict]) -> str:
    avgs = average_by_city(records)
    if not avgs:
        return ""
    best = sorted(avgs.items(), key=lambda kv: (-kv[1], kv[0]))[0]
    return best[0]



[A[A[A[A[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[Cdd