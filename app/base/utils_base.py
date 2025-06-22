from abc import ABC, abstractmethod

class BaseDecoder(ABC):
    @abstractmethod
    def decode(self):
        pass

class BaseEncoder(ABC):
    @abstractmethod
    def encode(self):
        pass
