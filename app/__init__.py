from app.commands import CommandHandler, Command
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand

class App:
    def __init__(self):
        self.commands_list = CommandHandler()

        self.commands_list.register_command('add', AddCommand())
        self.commands_list.register_command('subtract', SubtractCommand())
        self.commands_list.register_command('multiply', MultiplyCommand())
        self.commands_list.register_command('divide', DivideCommand())
        self.commands_list.register_command('exit', ExitCommand())

    def run(self):
        print("MID TERM \nWelcome to the Advanced Calculator")
        while True:
            command_input = input("Enter a command to execute \nAdd  Subtract  Multiply  Divide  Exit\n").strip().lower()

            if command_input in self.commands_list.commands and command_input!= 'exit':
                a = int(input("Enter a:"))
                b = int(input("Enter b:"))
                result = self.commands_list.execute_command(command_input, a, b)
            elif command_input == 'exit':
                self.commands_list.execute_command(command_input)
            else:
                print(f"Unknown Command: {command_input}")
