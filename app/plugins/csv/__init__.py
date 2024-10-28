import os
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

        elif not os.access(data_dir, os.W_OK):
            return
        
        history = self.history_manager.get_history()
        print(history)
        df = pd.DataFrame(history)
        file_exists = os.path.isfile(self.filename)

        df.to_csv(self.filename, mode='a', header=not file_exists, index=False)
        print(f"History exported to {self.filename} in the specified format.")