import sys
from app.commands import Command
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal


class MultiplyCommand(Command):
    def execute(self, a=None, b=None):
        if a is None or b is None:
            a = Decimal(input("Enter first number: "))
            b = Decimal(input("Enter second number: "))
        result = multiply(a, b)
        print(f"The result of multiplying {a} and {b} is {result}")

