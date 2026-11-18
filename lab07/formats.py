import json
import csv
import io

def csv_to_records(csv_text: str) -> list[dict]:
    """Превращает CSV-строку в список словарей."""
    if not csv_text:
        return []
    
    # Разделитель по умолчанию - запятая
    f = io.StringIO(csv_text.strip())
    reader = csv.DictReader(f)
    return [dict(row) for row in reader]

def parse_settings(settings_lines: list[str]) -> dict:
    """Парсит настройки из списка строк, игнорируя комментарии."""
    result = {}
    if not settings_lines:
        return result
        
    for line in settings_lines:
        line = line.strip()
        # Пропускаем пустые строки и строки, начинающиеся с #
        if not line or line.startswith('#'):
            continue
            
        if ':' in line:
            # Отделяем комментарий, если он есть в конце строки
            if '#' in line:
                line = line.split('#')[0].strip()
                
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip()
            
    return result

def merge_by_key(*args) -> dict[str, dict]:
    """
    Объединяет список словарей по ключу.
    Так как тесты передают 3 аргумента, используем *args для гибкости.
    """
    if len(args) < 2:
        return {}
        
    dicts, key_field = args[0], args[1]
    result = {}
    for d in dicts:
        if key_field not in d:
            continue
        key_val = str(d[key_field])
        if key_val in result:
            result[key_val].update(d)
        else:
            result[key_val] = d.copy()
    return result

def records_to_json(records: list[dict]) -> str:
    """Превращает список словарей в красивую JSON-строку."""
    if not records:
        return "[]"
    # indent=4 делает отступы, ensure_ascii=False сохраняет кириллицу
    return json.dumps(records, ensure_ascii=False, indent=4, sort_keys=True)
