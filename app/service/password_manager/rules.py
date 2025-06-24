import re
from typing import Tuple
from app.base.api_base import BasePasswordRuleStrategy

class MinLengthRule(BasePasswordRuleStrategy):
    def __init__(self, min_length: int = 8):
        if min_length < 1:
            raise ValueError("min_length должен быть >= 1")
        self.min_length = min_length

    def validate(self, password: str) -> Tuple[bool, str]:
        """
        проверяет пароль на длину
        Args:
            password: пароль для проверки
        Returns:
            Tuple[bool, str]: прошел ли пароль проверку и сообщение в случае провала
        """
        if not isinstance(password, str):
            return False, "Пароль должен быть строкой"
        if len(password) >= self.min_length:
            return True, ""
        return False, f"Пароль должен быть не менее {self.min_length} символов"

class DigitRule(BasePasswordRuleStrategy):
    DIGIT_RE = re.compile(r"\d")

    def validate(self, password: str) -> Tuple[bool, str]:
        """
        проверяет пароль на наличие цифр
        Args:
            password: пароль для проверки
        Returns:
            Tuple[bool, str]: прошел ли пароль проверку и сообщение в случае провала
        """
        if not isinstance(password, str):
            return False, "Пароль должен быть строкой"
        if self.DIGIT_RE.search(password):
            return True, ""
        return False, "Пароль не содержит цифр"

class LowercaseRule(BasePasswordRuleStrategy):
    LOWER_RE = re.compile(r"[a-z]")

    def validate(self, password: str) -> Tuple[bool, str]:
        """
        проверяет пароль на наличие строчных символов
        Args:
            password: пароль для проверки
        Returns:
            Tuple[bool, str]: прошел ли пароль проверку и сообщение в случае провала
        """
        if not isinstance(password, str):
            return False, "Пароль должен быть строкой"
        if self.LOWER_RE.search(password):
            return True, ""
        return False, "Пароль не содержит строчных букв"

class UppercaseRule(BasePasswordRuleStrategy):
    UPPER_RE = re.compile(r"[A-Z]")

    def validate(self, password: str) -> Tuple[bool, str]:
        """
        проверяет пароль на наличие заглавных символов
        Args:
            password: пароль для проверки
        Returns:
            Tuple[bool, str]: прошел ли пароль проверку и сообщение в случае провала
        """
        if not isinstance(password, str):
            return False, "Пароль должен быть строкой"
        if self.UPPER_RE.search(password):
            return True, ""
        return False, "Пароль не содержит заглавных букв"

class SpecialCharRule(BasePasswordRuleStrategy):
    def __init__(self, special_chars: str = "@#$^&"):
        if not special_chars:
            raise ValueError("special_chars не может быть пустой строкой")
        self._pattern = re.compile(f"[{re.escape(special_chars)}]")

    def validate(self, password: str) -> Tuple[bool, str]:
        """
        проверяет пароль на наличие спецсимволов
        Args:
            password: пароль для проверки
        Returns:
            Tuple[bool, str]: прошел ли пароль проверку и сообщение в случае провала
        """
        if not isinstance(password, str):
            return False, "Пароль должен быть строкой"
        if self._pattern.search(password):
            return True, ""
        return False, "Пароль не содержит специальных символов"
