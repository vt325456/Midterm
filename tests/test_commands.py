"""
Test Code for command classes in the application.

This module contains unit tests for the arithmetic command classes:
AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, 
and ExitCommand. Each test ensures that the commands behave as expected 
when executed with various inputs.
"""
import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand

def test_add_command():
    """
    Test the execution of the AddCommand.
    Verifies that the add command correctly adds two numbers.
    """
    command = AddCommand()
    result = command.execute(10, 5)
    assert result == 15, f"Expected 15, Wrong Result {result}"

def test_subtract_command():
    """
    Test the execution of the SubtractCommand.
    Verifies that the subtract command correctly subtracts the second number from the first.
    """
    command = SubtractCommand()
    result = command.execute(5, 3)
    assert result == 2, f"Expected 2, Wrong Result {result}"

def test_multiply_command():
    """
    Test the execution of the MultiplyCommand.
    Verifies that the multiply command correctly multiplies two numbers.
    """
    command = MultiplyCommand()
    result = command.execute(5, 5)
    assert result == 25, f"Expected 25, Wrong Result {result}"

def test_divide_command():
    """
    Test the execution of the DivideCommand.
    Verifies that the divide command correctly divides the first number by the second.
    """
    command = DivideCommand()
    result = command.execute(25, 5)
    assert result == 5, f"Expected 5, Wrong Result {result}"

def test_dividebyzero():
    """
    Test the DivideCommand for division by zero.
    Verifies that the divide command raises a ValueError when attempting to divide by zero.
    """
    command = DivideCommand()
    with pytest.raises(ValueError, match="The DivideByZero Exception Occured"):
        command.execute(10, 0)

def test_exit_command():
    """
    Test the execution of the ExitCommand.
    Verifies that the exit command raises a SystemExit exception.
    """
    command = ExitCommand()
    with pytest.raises(SystemExit):
        command.execute()
