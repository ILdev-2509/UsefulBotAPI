from app.base.api_base import BaseConverter
from app.config.exceptions import TooBigBaseException, TooSmallBaseException

class BasesConverter(BaseConverter):
    DIGITS: str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def convert(self, number: int | str, to_base: int, from_base: int) -> str:
        """
        Конвертирует число из одной системы счисления в другую.
        Args:
            number (int | str): число для конвертации
            to_base (int): основание требуемой системы счисления
            from_base (int): основание исходной системы счисления
        Returns:
            str: сконвертированное число
        Raises:
            TooBigBaseException: если хоть одно из оснований больше, чем 36
            TooSmallBaseException: если хоть одно из оснований меньше, чем 2
            ValueError: если формат числа неверный

        """
        if to_base > 36 or from_base > 36:
            raise TooBigBaseException("Основание большее, чем 36, не допускается.")
        if to_base < 2 or from_base < 2:
            raise TooSmallBaseException("Основание меньшее, чем 2, не допускается.")

        is_negative = False

        try:
            number_int = int(str(number).strip(), from_base)
        except ValueError:
            raise ValueError(f"Неверный формат числа '{number}' для системы с основанием {from_base}.")

        if number_int == 0:
            return '0'

        if number_int < 0:
            is_negative = True
            number_int = abs(number_int)

        result = ''
        while number_int > 0:
            result = self.DIGITS[number_int % to_base] + result
            number_int //= to_base

        return '-' + result if is_negative else result
