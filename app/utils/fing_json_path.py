from pathlib import Path

def _find_app_root(marker_dir_name: str = "app") -> Path:
    """
    Ищет вверх по дереву каталогов папку с именем marker_dir_name.
    Возвращает Path к этой папке или бросает RuntimeError, если не найдено.
    Args:
        marker_dir_name (str): искомая папка
    Returns:
        Path: путь до искомой папки
    """
    current: Path = Path(__file__).resolve()
    for parent in current.parents:
        if parent.name == marker_dir_name:
            return parent
    raise RuntimeError(f"Не удалось найти родительскую папку '{marker_dir_name}' в цепочке {current.parents}")

def get_path(service_name: str, filename: str) -> str:
    """
    Строит и возвращает строку с абсолютным путём к файлу внутри app/src/{service_name}/{filename}.
    Args:
        service_name (str): имя сервиса, для которого нужен json-файл
        filename (str): название файла JSON
    Returns:
        str: строка с абсолютным путём к файлу внутри app/src/{service_name}/{filename}
    """
    return str((_find_app_root("app") / "src" / service_name / filename).resolve())
