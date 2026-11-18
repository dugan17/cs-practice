def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        filename = path.split('/')[-1]
        if '.' not in filename or (filename.startswith('.') and filename.count('.') == 1):
            ext = ""
        else:
            ext = filename.split('.')[-1].lower()
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return sorted(paths, key=lambda p: (-p.count('/'), p))[0]

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if n_bytes == 0:
        return "0 Б"
    size = float(n_bytes)
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1
    if unit_index == 0:
        return f"{int(size)} {units[unit_index]}"
    else:
        return f"{size:.1f} {units[unit_index]}"
# Сделано студентом
