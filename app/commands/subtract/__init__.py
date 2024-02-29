import sys
from app.commands import Command
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal


class SubtractCommand(Command):
    def execute(self, a=None, b=None):
        if a is None or b is None:
            a = Decimal(input("Enter first num: "))
            b = Decimal(input("Enter second num: "))
        result = subtract(a, b)
        print(f"The result of subtracting {b} from {a} is {result}")
