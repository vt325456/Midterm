import logging
import logging.config
from app.commands import Command
from app.history import HistoryManager

history_ = HistoryManager()
class AddCommand(Command):

    def execute(self, a, b, history_):
        logging.info(f"Addition Between {a} and {b}")
        result = a + b
        logging.info(f"Result : {result}")
        history_.add_to_history(a, b, "Add", result)
        logging.info(f"Appended calculation to history - Addition")
        return result
        