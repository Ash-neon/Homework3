import logging
from app.commands import Command
from calculator.operations import add
from decimal import Decimal
import multiprocessing

class AddCommand(Command):
    def execute(self, a=None, b=None):
        if a is None or b is None:
            logging.error("Usage: add <number1> <number2>")
            return

        # Multiprocessing logic to execute the addition operation
        def execute_addition(a, b):
            result = add(a, b)
            print(f"The result of adding {a} and {b} is {result}")
            logging.info(f"The result of adding {a} and {b} is {result}")

        # Create a process for executing the addition operation
        process = multiprocessing.Process(target=execute_addition, args=(a, b))
        process.start()
        process.join()  # Wait for the process to finish