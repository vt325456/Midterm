"""
Test module for the HistoryManager class.

This module contains tests to verify the functionality of the HistoryManager,
including adding entries, retrieving history, and clearing the history.
"""
from app.history import HistoryManager

def test_add_to_history():
    """Test that adding an entry to history works correctly."""
    manager = HistoryManager()
    manager.add_to_history(10, 5, "Add", 15)
    assert len(manager.history) == 1
    assert manager.history[0] == {
        "Operation": "Add",
        "Operand1": 10,
        "Operand2": 5,
        "Result": 15
    }

def test_get_history():
    """Test that retrieving the history returns the correct entries."""
    manager = HistoryManager()
    manager.add_to_history(10, 5, "Add", 15)
    manager.add_to_history(8, 2, "Subtract", 6)
    history = manager.get_history()
    assert len(history) == 2
    assert history[0] == {
        "Operation": "Add",
        "Operand1": 10,
        "Operand2": 5,
        "Result": 15
    }
    assert history[1] == {
        "Operation": "Subtract",
        "Operand1": 8,
        "Operand2": 2,
        "Result": 6
    }

def test_clear_history():
    """Test that clearing the history works correctly."""
    manager = HistoryManager()
    manager.add_to_history(10, 5, "Add", 15)
    assert len(manager.history) == 1
    manager.clear_history()
    assert len(manager.history) == 0

def test_clear_history_on_empty_history():
    """Test clearing the history when it is already empty."""
    manager = HistoryManager()
    manager.clear_history()
    assert len(manager.history) == 0
 