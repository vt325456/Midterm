from app.commands import Command

class SubtractCommand(Command):

    def execute(self, a, b):
        print("Result:", a - b)
        