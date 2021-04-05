from OperationStrategy import OperationStrategy


class CalculatorContext:
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: OperationStrategy):
        self._strategy = strategy

    def calculate_and_print_result(self, number_1: int, number_2: int) -> None:
        result = self._strategy.calculate(number_1, number_2)
        print(result)
