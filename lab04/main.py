import sys
from stats import average_by_city, read_valid, warmest_city

def main() -> None:
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    valid = len(records)
    empty = sum(1 for line in lines if line.strip() == "")
    skipped = len(lines) - valid - empty
    
    avgs = average_by_city(records)
    best = warmest_city(records)
    
    print(valid)
    print(skipped)
    if best:
        print(f"{avgs[best]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()
