from abc import ABC, abstractmethod
from typing import Tuple

class BaseConverter(ABC):
    @abstractmethod
    def convert(self):
        pass

class BaseTranslator(ABC):
    @abstractmethod
    def translate(self, text: str) -> str:
        pass

class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, length: int | None = None) -> str:
        pass

class BaseChecker(ABC):
    @abstractmethod
    def check(self):
        pass

class BasePasswordRuleStrategy(ABC):
    @abstractmethod
    def validate(self, password: str) -> Tuple[bool, str]:
        pass
