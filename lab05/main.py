import sys
from logstats import count_levels, top_errors, format_report

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input().strip()
    
    try:
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Файл не найден")
        return
        
    counts = count_levels(lines)
    errors = top_errors(lines, 3)
    total = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken = counts.get("BROKEN", 0)
    print(total)
    print(error_count)
    print(broken)
    report = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

if __name__ == "__main__":
    main()