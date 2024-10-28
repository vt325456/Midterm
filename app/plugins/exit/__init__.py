import sys
from app.commands import Command
from app.plugins.csv import CsvCommand
from app.history import HistoryManager

class ExitCommand(Command):
    def execute(self, history_):
        if history_:
            csv = CsvCommand(history_)
            csv.execute()
            print(f"History is added with:{history_.get_history()}")

        sys.exit("Exiting...")