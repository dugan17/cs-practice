import json
import csv
import io

def csv_to_records(csv_text: str) -> list[dict]:
    if not csv_text:
        return []
    f = io.StringIO(csv_text.strip())
    reader = csv.DictReader(f)
    result = []
    for row in reader:
        new_row = {}
        for k, v in row.items():
            if v is None:
                new_row[k] = v
                continue
            v = v.strip()
            try:
                new_row[k] = int(v)
            except ValueError:
                try:
                    new_row[k] = float(v)
                except ValueError:
                    new_row[k] = v
        result.append(new_row)
    return result

def parse_settings(settings_lines: list[str]) -> dict:
    result = {}
    if not settings_lines:
        return result
    for line in settings_lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '#' in line:
            line = line.split('#')[0].strip()
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value.lower() == 'true':
                result[key] = True
            elif value.lower() == 'false':
                result[key] = False
            elif ',' in value:
                result[key] = [v.strip() for v in value.split(',')]
            else:
                try:
                    result[key] = int(value)
                except ValueError:
                    try:
                        result[key] = float(value)
                    except ValueError:
                        result[key] = value
    return result

def merge_by_key(*args) -> dict[str, dict]:
    if not args:
        return {}
    data = []
    key_field = "id"
    for arg in args:
        if isinstance(arg, list):
            data = arg
        elif isinstance(arg, str):
            key_field = arg
    result = {}
    for d in data:
        if not isinstance(d, dict) or key_field not in d:
            continue
        key_val = str(d[key_field])
        if key_val in result:
            result[key_val].update(d)
        else:
            result[key_val] = d.copy()
    return result

def records_to_json(records: list[dict]) -> str:
    if not records:
        return "[]"
    return json.dumps(records, ensure_ascii=False, indent=4, sort_keys=True)
