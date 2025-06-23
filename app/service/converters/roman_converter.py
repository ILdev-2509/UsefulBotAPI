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
