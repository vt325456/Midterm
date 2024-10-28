from app.commands import Command
from app.history import HistoryManager

history_ = HistoryManager()
class AddCommand(Command):

    def execute(self, a, b, history_):
        result = a + b
        print(f"Add command hit {result}")
        history_.add_to_history(a, b, "Add", result)
        return result
        