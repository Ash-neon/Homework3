import sys
from app.commands import Command
from calculator.operations import add
from decimal import Decimal



class AddCommand(Command):
    def execute(self, a=None, b=None):
        if a is None or b is None:
            a = Decimal(input("Enter first number: "))
            b = Decimal(input("Enter second number: "))
        result = add(a, b)
        print(f"The result of adding {a} and {b} is {result}")
