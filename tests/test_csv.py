"""
Test module for the CsvCommand class.

This module contains tests to verify the behavior of the CsvCommand,
including directory creation and handling of write permissions.
"""
import os
from unittest.mock import MagicMock
import pytest
from app.plugins.csv import CsvCommand

@pytest.fixture
def history_manager():
    """Fixture for a mock history manager."""
    manager = MagicMock()
    manager.get_history.return_value = [
        {"Operation": "Add", "Operand1": 10, "Operand2": 5, "Result": 15},
        {"Operation": "Subtract", "Operand1": 10, "Operand2": 3, "Result": 7},
    ]
    return manager

def test_csv_command_directory_creation(history_manager, monkeypatch):
    """Test that the data directory is created if it doesn't exist."""
    command = CsvCommand(history_manager)
    with monkeypatch.context() as m:
        m.setattr(os.path, 'exists', lambda path: False)
        m.setattr(os, 'makedirs', lambda path: None)
        command.execute()
    assert os.path.exists('./data')

def test_csv_command_no_write_permission(history_manager, monkeypatch):
    """Test that no action is taken if the directory is not writable."""
    command = CsvCommand(history_manager)
    with monkeypatch.context() as m:
        m.setattr(os.path, 'exists', lambda path: True)
        m.setattr(os, 'access', lambda path, mode: False)
        assert command.execute() is None
