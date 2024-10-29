import logging
from app.commands import Command
from app.history import HistoryManager

history_ = HistoryManager()
class SubtractCommand(Command):

    def execute(self, a, b, history_):
        logging.info(f"Subtract Operation Between {a} and {b}")
        result  = a - b
        logging.info(f"Result : {result}")
        history_.add_to_history(a, b, "Subtract", result)
        logging.info(f"Appended calculation to history - Subtract")
        return result
        