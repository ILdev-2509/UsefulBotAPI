from app.base.api_base import BaseConverter
from app.utils.fing_json_path import get_path
from app.utils.json_util import JSONDecoder

DATA_PATH = get_path("converter/roman", "roman.json")
decoder = JSONDecoder()
ROMAN_MAPPING = decoder.decode(DATA_PATH)

class ToRomanConverter(BaseConverter):
    def convert(self, number: int | str) -> str:
        """
        конвертирует арабские цифры в римские
        Args:
            number (int | str): исходное число
        Returns:
            str: сконвертированное число
        Raises:
            ValueError: если число невозможно преобразовать в int или если оно меньше нуля
        """
        try:
            value = int(str(number).strip())
        except ValueError:
            raise ValueError(f"Не удалось интерпретировать '{number}' как число.")
        if value <= 0:
            raise ValueError("Римские цифры определены только для положительных целых.")

        result = []
        for roman, arabic in sorted(ROMAN_MAPPING.items(), key=lambda item: item[1], reverse=True):
            count, value = divmod(value, arabic)
            result.append(roman * count)

        return ''.join(result)

class FromRomanConverter(BaseConverter):
    def convert(self, number: int | str) -> int:
        """
        Конвертирует римские цифры в арабские
        Args:
            number (int | str): исходное число
        Returns:
            int: сконвертированное число
        Raises:
            ValueError: если обнаружен недопустимый символ
        """
        roman = str(number).strip().upper()
        result = 0
        i = 0
        length = len(roman)

        while i < length:
            if i + 1 < length and roman[i:i + 2] in ROMAN_MAPPING:
                result += ROMAN_MAPPING[roman[i:i + 2]]
                i += 2
            elif roman[i] in ROMAN_MAPPING:
                result += ROMAN_MAPPING[roman[i]]
                i += 1
            else:
                raise ValueError(f"Недопустимый символ в римском числе: '{roman[i]}'")

        return result
