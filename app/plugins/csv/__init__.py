import os
import logging
from app.commands import Command
import pandas as pd


class CsvCommand(Command):
    def __init__(self, history_manager, filename='calculator_history.csv'):
        self.history_manager = history_manager
        self.filename = os.path.join('data', filename)

    def execute(self):
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")

        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return
        
        history = self.history_manager.get_history()
        logging.info(history)
        df = pd.DataFrame(history)
        file_exists = os.path.isfile(self.filename)

        df.to_csv(self.filename, mode='a', header=not file_exists, index=False)
        logging.info(f"History has been exported to {self.filename}")