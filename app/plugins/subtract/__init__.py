from app.commands import Command

class SubtractCommand(Command):

    def execute(self, a, b):
        return a - b
        