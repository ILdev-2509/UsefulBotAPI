from typing import Literal
from app.base.api_base import BaseTranslator
from app.utils.json_util import JSONDecoder
from app.utils.fing_json_path import get_path

class KeyboardTranslator(BaseTranslator):
    def __init__(
        self,
        direction: Literal['to_russian', 'to_english'],
        dictionary_path: str = get_path(service_name="translator/keyboard", filename="keyboard.json")
    ):
        """
        :param direction: 'to_russian' — с английской на русскую;
                          'to_english' — с русской на английскую.
        :param dictionary_path: путь к JSON-файлу с раскладкой клавиатуры
        """
        if direction not in ('to_russian', 'to_english'):
            raise ValueError("direction должен быть 'to_russian' или 'to_english'")
        decoder = JSONDecoder()
        raw_dict = decoder.decode(dictionary_path) or {}

        if direction == 'to_russian':
            self._dictionary = raw_dict
        else:
            self._dictionary = {v: k for k, v in raw_dict.items()}

    def translate(self, text: str) -> str:
        """
        Args:
            text (str): текст для перевода
        Returns:
            str: текст, переведенный на противоположную раскладку клавиатуры
        """
        return ''.join(self._dictionary.get(char, char) for char in text)
