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

class FromMorseTranslator(BaseTranslator):
    _reverse_dictionary_cache: dict[str, str] = None

    def __init__(self):
        decoder = JSONDecoder()
        if FromMorseTranslator._reverse_dictionary_cache is None:
            chardict = decoder.decode(get_path("translator/morse", "russian_morse.json")) or {}
            symboldict = decoder.decode(get_path("translator/morse", "symbols.json")) or {}
            merged = chardict | symboldict
            FromMorseTranslator._reverse_dictionary_cache = {v: k for k, v in merged.items()}
        self._dictionary = FromMorseTranslator._reverse_dictionary_cache

    def translate(self, text: str) -> str:
        """
        Переводит код морзе обратно в текст
        Args:
            text (str): код морзе для перевода
        Returns:
            str: текст, переведенный с кода морзе
        """
        words = text.strip().split(' / ')
        decoded_words = []

        for word in words:
            chars = word.strip().split()
            decoded_word = ''.join([self._dictionary.get(c, c) for c in chars])
            decoded_words.append(decoded_word)

        return ' '.join(decoded_words)
