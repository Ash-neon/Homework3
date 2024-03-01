import logging
from app.commands import Command
from calculator.operations import subtract
from decimal import Decimal
import multiprocessing


class SubtractCommand(Command):
    def execute(self, a=None, b=None):
        if a is None or b is None:
            logging.error("Usage: subtract <minuend> <subtrahend>")
            return

        # Multiprocessing logic to execute the subtraction operation
        def execute_subtraction(a, b):
            result = subtract(a, b)
            print(f"The result of subtracting {b} from {a} is {result}")
            logging.info(f"The result of subtracting {b} from {a} is {result}")

        # Create a process for executing the subtraction operation
        process = multiprocessing.Process(target=execute_subtraction, args=(a, b))
        process.start()
        process.join()  # Wait for the process to finish