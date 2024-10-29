import logging
import logging.config
from app.commands import Command
from app.history import HistoryManager

history_ = HistoryManager()
class MultiplyCommand(Command):

    def execute(self, a, b, history_):
        logging.info(f"Multiplication Operation between {a} and {b}")
        result = a * b
        logging.info(f"Result : {result}")
        history_.add_to_history(a, b, "Multiply", result)
        logging.info(f"Appended calculation to history - Multiplication")
        return result
        