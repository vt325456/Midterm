from app.commands import Command
from app.history import HistoryManager

history_ = HistoryManager()
class MultiplyCommand(Command):

    def execute(self, a, b, history_):
        result = a * b
        history_.add_to_history(a, b, "Multiply", result)
        return result
        