from CalculatorContext import CalculatorContext
from DivisionStrategy import DivisionStrategy
from MultiplyStrategy import MultiplyStrategy
from SubtractionStrategy import SubtractionStrategy
from SumStrategy import SumStrategy

if __name__ == "__main__":
    calculator = CalculatorContext()
    number_1 = 9
    number_2 = 10

    print("Client: Adding two numbers")
    calculator.strategy = SumStrategy()
    calculator.calculate_and_print_result(number_1, number_2)

    print("Client: Multiplying two numbers")
    calculator.strategy = MultiplyStrategy()
    calculator.calculate_and_print_result(number_1, number_2)

    print("Client: Dividing two numbers")
    calculator.strategy = DivisionStrategy()
    calculator.calculate_and_print_result(number_1, number_2)

    print("Client: Subtracting two numbers")
    calculator.strategy = SubtractionStrategy()
    calculator.calculate_and_print_result(number_1, number_2)
