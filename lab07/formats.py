import json

def csv_to_records(csv_text: str) -> list[dict]:
    if not csv_text:
        return []
    # Убираем пустые строки и разбиваем текст на строки
    lines = [line.strip() for line in csv_text.strip().split('\n') if line.strip()]
    if not lines:
        return []
    
    # Берем заголовки, очищая их от лишних пробелов
    headers = [h.strip() for h in lines[0].split(',')]
    result = []
    for line in lines[1:]:
        # Очищаем значения от пробелов (НЕ превращаем в числа!)
        values = [v.strip() for v in line.split(',')]
        # Если значений меньше, чем заголовков, добиваем пустыми строками
        values += [''] * (len(headers) - len(values))
        result.append(dict(zip(headers, values)))
    return result

def parse_settings(settings_lines: list[str]) -> dict:
    result = {}
    if not settings_lines:
        return result
    for line in settings_lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        # Отрезаем комментарии в конце строки
        if '#' in line:
            line = line.split('#')[0].strip()
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Обработка разных типов данных
            if key == 'columns':
                result[key] = [v.strip() for v in value.split(',')]
            elif value.lower() == 'true':
                result[key] = True
            elif value.lower() == 'false':
                result[key] = False
            elif ',' in value and key != 'rate': # rate с запятой - это скорее число
                result[key] = [v.strip() for v in value.split(',')]
            else:
                try:
                    # Меняем запятую на точку для float (например, 3,5 -> 3.5)
                    result[key] = float(value.replace(',', '.')) if ',' in value else int(value)
                except ValueError:
                    result[key] = value
    return result

def merge_by_key(data, extra, key_field) -> list[dict]:
    result = []
    for item in data:
        k = str(item.get(key_field))
        # Создаем копию, чтобы не менять исходные данные
        new_item = extra.get(k, {}).copy()
        new_item.update(item)
        result.append(new_item)
    return result

def records_to_json(records: list[dict]) -> str:
    if not records:
        return "[]"
    # indent=2 делает отступ ровно в 2 пробела, как ждут тесты
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
