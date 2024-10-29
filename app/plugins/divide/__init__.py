import logging
import logging.config
from app.commands import Command
from app.history import HistoryManager

history_ = HistoryManager()
class DivideCommand(Command):

    def execute(self, a, b, history_):
        if b != 0:
            logging.info(f"Division Operation Between {a} and {b}")
            result = a / b
            logging.info(f"Result : {result}")
            history_.add_to_history(a, b, "Divide", result)
            logging.info(f"Appended calculation to history - Division")
            return result
        else:
            return "The DivideByZero Exception Occured"
        