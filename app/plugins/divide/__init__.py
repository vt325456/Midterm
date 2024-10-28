from app.commands import Command
from app.history import HistoryManager

history_ = HistoryManager()
class DivideCommand(Command):

    def execute(self, a, b, history_):
        if b != 0:
            result = a / b
            history_.add_to_history(a, b, "Divide", result)
            return result
        else:
            return "The DivideByZero Exception Occured"
        