from app.base.api_base import BaseTranslator
from app.utils.json_util import JSONDecoder
from app.utils.fing_json_path import get_path

class ToMorseTranslator(BaseTranslator):
    _dictionary_cache: dict[str, str] = None

    def __init__(self):
        decoder = JSONDecoder()
        if ToMorseTranslator._dictionary_cache is None:
            chardict = decoder.decode(get_path("translator/morse", "russian_morse.json")) or {}
            symboldict = decoder.decode(get_path("translator/morse", "symbols.json")) or {}
            ToMorseTranslator._dictionary_cache = chardict | symboldict
        self._dictionary = ToMorseTranslator._dictionary_cache

    def translate(self, text: str) -> str:
        """
        Переводит текст на код морзе
        Args:
            text (str): текст для перевода
        Returns:
            str: текст, переведенный на код морзе
        """
        result = []
        for char in text.upper():
            result.append(self._dictionary.get(char, char))
        return ' '.join(result)

