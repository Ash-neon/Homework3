from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.menu import MenuCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        menu_command = MenuCommand(self.command_handler.get_command_names())
        self.command_handler.register_command("menu", menu_command)

        print("Type 'exit' to exit.")
        while True:  
            user_input = input(">>> ").strip()
            if user_input == 'exit':
                print("Exiting the program. Goodbye!")
                return True  # Indicates that the program should exit
            self.command_handler.execute_command(user_input)
        return False  # This line is not necessary, but included for clarity
