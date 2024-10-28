import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand

def test_add_command():
    command = AddCommand()
    result = command.execute(10, 5)
    assert result == 15, f"Expected 15, Wrong Result {result}"

def test_subtract_command():
    command = SubtractCommand()
    result = command.execute(5, 3)
    assert result == 2, f"Expected 2, Wrong Result {result}"

def test_multiply_command():
    command = MultiplyCommand()
    result = command.execute(5, 5)
    assert result == 25, f"Expected 25, Wrong Result {result}"

def test_divide_command():
    command = DivideCommand()
    result = command.execute(25, 5)
    assert result == 5, f"Expected 5, Wrong Result {result}"

def test_divideByZero():
    command = DivideCommand()
    with pytest.raises(ValueError, match="The DivideByZero Exception Occured"):
        command.execute(10, 0)

def test_exit_command():
    command = ExitCommand()
    with pytest.raises(SystemExit) as exc_info:
            command.execute()