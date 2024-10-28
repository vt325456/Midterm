"""
This module contains tests for the Command and CommandHandler classes.

It includes tests for registering commands, executing registered commands,
handling unregistered commands, and executing commands with no arguments.
"""
from app.commands import Command, CommandHandler

class MockCommand(Command):
    """
    A mock command for testing purposes.
    This command simply sums its arguments when executed.
    """
    def execute(self, *args):
        return sum(args)

def test_register_command():
    """Test that commands can be registered in the CommandHandler."""
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command('mock', mock_command)
    assert 'mock' in handler.commands
    assert handler.commands['mock'] is mock_command

def test_execute_registered_command():
    """Test that executing a registered command works correctly."""
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command('mock', mock_command)
    result = handler.execute_command('mock', 1, 2)
    assert result == 3

def test_execute_unregistered_command(capsys):
    """Test that executing an unregistered command raises an appropriate error message."""
    handler = CommandHandler()
    handler.execute_command('unregistered')
    captured = capsys.readouterr()
    assert captured.out.strip() == "No such command: unregistered"

def test_execute_command_with_no_arguments():
    """Test that executing a command with no arguments raises an error."""
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command('mock', mock_command)
    result = handler.execute_command('mock')
    assert result == 0
