from app import App
from app.commands.menu import MenuCommand
from decimal import Decimal
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand

def test_add_command(capfd):
    command = AddCommand()
    # Assuming execute now takes two parameters, and prints the result
    command.execute(Decimal('5'), Decimal('3'))
    out, err = capfd.readouterr()
    assert out.strip() == "The result of adding 5 and 3 is 8", "The AddCommand should print the correct result"

def test_subtract_command(capfd):
    command = SubtractCommand()
    # Assuming execute now takes two parameters, and prints the result
    command.execute(Decimal('5'), Decimal('3'))
    out, err = capfd.readouterr()
    assert out.strip() == "The result of subtracting 3 from 5 is 2", "The SubtractCommand should print the correct result"

def test_menu_command(capfd, monkeypatch):
    # Set up the application with a mocked input to trigger the 'menu' command, then 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    # Register the MenuCommand explicitly for this test
    app.command_handler.register_command("menu", MenuCommand(app.command_handler.get_command_names()))

    app.start()

    out, err = capfd.readouterr()
    # Assert that the menu lists commands; adjust expected output as necessary
    assert "add" in out, "The menu should list the 'add' command"
    assert "subtract" in out, "The menu should list the 'subtract' command"
    assert "multiply" in out, "The menu should list the 'multiply' command"
    assert "divide" in out, "The menu should list the 'divide' command"
    assert "menu" in out, "The menu should list itself"