import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation
from app import App    
from history.history_manager import HistoryManager

def calculate_and_print(a, b, operation_name, history_manager):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name)
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
            history_manager.add_record(a, b, operation_name,result(a_decimal, b_decimal))  # Save to history
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    history_manager = HistoryManager()  # Instantiate history manager
    
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation, history_manager)
    
    # saving history when the program ends
    history_manager.save_history()

if __name__ == '__main__':
    App().start()
    # main()