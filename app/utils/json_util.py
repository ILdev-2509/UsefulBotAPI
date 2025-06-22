import json
from app.base.utils_base import BaseDecoder

class JSONDecoder(BaseDecoder):
    def decode(self, filename: str) -> dict | None:
        """
        Преобразует JSON-строку из файла в список словарей.

        Args:
            filename (str): путь до файла JSON
        Returns:
            dict | None: словарь, полученный из файла JSON
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_str: str = file.read()
                dict_list: dict = json.loads(json_str)
            return dict_list
        except (TypeError, ValueError, IOError) as e:
            print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
            return None
