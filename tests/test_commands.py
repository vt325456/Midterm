"""
Test Code for command classes in the application.

This module contains unit tests for the arithmetic command classes:
AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, 
and ExitCommand. Each test ensures that the commands behave as expected 
when executed with various inputs.
"""
import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand
from app.history import HistoryManager

history_ = HistoryManager()
def test_add_command():
    """
    Test the execution of the AddCommand.
    Verifies that the add command correctly adds two numbers.
    """
    command = AddCommand()
    result = command.execute(10, 5, history_)
    assert result == 15, f"Expected 15, Wrong Result {result}"
    history = history_.get_history()
    assert len(history) == 1, "Expected history to have 1 entry"


def test_subtract_command():
    """
    Test the execution of the SubtractCommand.
    Verifies that the subtract command correctly subtracts the second number from the first.
    """
    command = SubtractCommand()
    result = command.execute(5, 3, history_)
    assert result == 2, f"Expected 2, Wrong Result {result}"
    history = history_.get_history()
    assert len(history) == 2, "Expected history to have 1 entry"

def test_multiply_command():
    """
    Test the execution of the MultiplyCommand.
    Verifies that the multiply command correctly multiplies two numbers.
    """
    command = MultiplyCommand()
    result = command.execute(5, 5, history_)
    assert result == 25, f"Expected 25, Wrong Result {result}"
    history = history_.get_history()
    assert len(history) == 3, "Expected history to have 1 entry"

def test_divide_command():
    """
    Test the execution of the DivideCommand.
    Verifies that the divide command correctly divides the first number by the second.
    """
    command = DivideCommand()
    result = command.execute(25, 5, history_)
    assert result == 5, f"Expected 5, Wrong Result {result}"
    history = history_.get_history()
    assert len(history) == 4, "Expected history to have 1 entry"

def test_dividebyzero():
    """
    Test the DivideCommand for division by zero.
    Verifies that the divide command raises a ValueError when attempting to divide by zero.
    """
    command = DivideCommand()
    result = command.execute(10,0, history_)
    assert result == "The DivideByZero Exception Occured"

def test_exit_command():
    """
    Test the execution of the ExitCommand.
    Verifies that the exit command raises a SystemExit exception.
    """
    command = ExitCommand()
    with pytest.raises(SystemExit):
        command.execute(history_)
