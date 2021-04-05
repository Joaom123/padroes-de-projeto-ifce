from OperationStrategy import OperationStrategy


class SubtractionStrategy(OperationStrategy):
    def calculate(self, number_1: int, number_2: int) -> int:
        return number_1 - number_2
