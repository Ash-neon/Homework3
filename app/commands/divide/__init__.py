import sys
from app.commands import Command
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal


class DivideCommand(Command):
    def execute(self, a=None, b=None):
        if a is None or b is None:
            a = Decimal(input("Enter dividend: "))
            b = Decimal(input("Enter divisor: "))
            if b == Decimal('0'):
                print("Error: Division by zero is not allowed.")
                return
        result = divide(a, b)
        print(f"The result of dividing {a} by {b} is {result}")
