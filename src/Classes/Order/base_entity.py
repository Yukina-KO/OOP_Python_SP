from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description

    @abstractmethod
    def __str__(self) -> str:
        pass
