from abc import ABC, abstractmethod

class BaseDecoder(ABC):
    @abstractmethod
    def decode(self, filename: str) -> dict | None:
        pass
