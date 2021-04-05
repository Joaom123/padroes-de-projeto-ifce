from OperationStrategy import OperationStrategy


class MultiplyStrategy(OperationStrategy):
    def calculate(self, number_1: int, number_2: int) -> int:
        return number_1 * number_2
