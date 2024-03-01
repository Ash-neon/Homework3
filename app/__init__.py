import sys
import logging
from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.menu import MenuCommand

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        menu_command = MenuCommand(self.command_handler.get_command_names())
        self.command_handler.register_command("menu", menu_command)

        logging.info("Type 'exit' to exit.")
        logging.info("Type 'menu' for MENU.")
        while True:
            user_input = input(">>> ").strip()
            if user_input == 'exit':
                logging.info("Exiting the program. Goodbye!")
                return True
            self.command_handler.execute_command(user_input)
        return False
