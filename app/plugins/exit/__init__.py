import sys
import logging
from app.commands import Command
from app.plugins.csv import CsvCommand
from app.history import HistoryManager

class ExitCommand(Command):
    def execute(self, history_):
        if history_.get_history():
            logging.info("Exiting with saving history.")
            csv = CsvCommand(history_)
            csv.execute()
            logging.info(f"History is added with:{history_.get_history()}")
        else:
            logging.info("Empty history. Nothing to save.")

        sys.exit("Exiting...")