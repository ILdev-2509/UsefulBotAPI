import string
import random
from app.base.api_base import BaseGenerator

class PasswordGenerator(BaseGenerator):
    def __init__(self, allowed_characters: str | None = None):
        self.allowed_characters = allowed_characters or (string.ascii_letters + string.digits + string.punctuation)
        if not self.allowed_characters:
            raise ValueError("Список разрешенных символов не может быть пустым")
        if len(self.allowed_characters) < 2:
            raise ValueError("Требуется минимум 2 специальных символа в списке")

    def generate(self, length: int) -> str:
        """
        генерирует пароль заданной длины
        Args:
            length (int):
        Returns:
            str: сгенерированный пароль
        Raises:
            TypeError: если длина не является числом
            ValueError: если длина пароля < 1
        """
        if not isinstance(length, int):
            raise TypeError("Длина должна быть числом")
        if length < 1:
            raise ValueError("Длина пароля должна быть больше 1")
        return ''.join(random.choice(self.allowed_characters) for _ in range(length))
