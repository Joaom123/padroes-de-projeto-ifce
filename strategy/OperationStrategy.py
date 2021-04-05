from abc import ABC, abstractmethod


class OperationStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.
    """

    @abstractmethod
    def calculate(self, number_1: int, number_2: int) -> int:
        pass
