import logging
from app.commands import Command
from calculator.operations import divide
from decimal import Decimal
import multiprocessing

class DivideCommand(Command):
    def execute(self, a=None, b=None):
        if a is None or b is None:
            logging.error("Usage: divide <dividend> <divisor>")
            return

        if b == 0:
            logging.error("Error: Division by zero is not allowed.")
            return

        # Multiprocessing logic to execute the division operation
        def execute_division(a, b):
            result = a / b
            logging.info(f"The result of dividing {a} by {b} is {result}")
            print(f"The result of dividing {a} by {b} is {result}")

        # Create a process for executing the division operation
        process = multiprocessing.Process(target=execute_division, args=(Decimal(a), Decimal(b)))
        process.start()
        process.join()  # Wait for the process to finish