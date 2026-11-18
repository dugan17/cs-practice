import json

def merge_by_key(dicts: list[dict], key_field: str = "id") -> dict[str, dict]:
    """Объединяет список словарей в один по указанному ключу."""
    result = {}
    for d in dicts:
        if key_field not in d:
            continue
        
        key_val = str(d[key_field])
        
        if key_val in result:
            # Если ключ уже есть, обновляем словарь новыми данными
            result[key_val].update(d)
        else:
            # Если нет — добавляем копию
            result[key_val] = d.copy()
            
    return result

def records_to_json(records: list[dict]) -> str:
    """Превращает список словарей в JSON-строку с сортировкой ключей."""
    if not records:
        return "[]"
        
    return json.dumps(records, ensure_ascii=False, sort_keys=True)
