import sys
from app.commands import Command
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal


class MenuCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        print("Menu")
        for command_name in self.commands:
            print(f"- {command_name}")
