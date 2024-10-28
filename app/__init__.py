import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.history import HistoryManager

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue
    def run(self):
        self.load_plugins()
        print("MID TERM \nWelcome to the Advanced Calculator")
        history_ = self.history_manager
        while True:
            command_input = input("Enter a command to execute \nAdd  Subtract  Multiply  Divide  Exit\n").strip().lower()
            try:
                if command_input in self.command_handler.commands and command_input!= 'exit':
                    a = int(input("Enter a:"))
                    b = int(input("Enter b:"))
                    result = self.command_handler.execute_command(command_input, a, b, history_)
                    print(f"Result: {result}")
                elif command_input == 'exit':
                    self.command_handler.execute_command(command_input, history_)
                else:
                    raise ValueError(f"Unknown Command: {command_input}")
            except Exception as e:
                print(f"Error: {e}")

