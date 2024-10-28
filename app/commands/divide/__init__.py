from app.commands import Command

class DivideCommand(Command):

    def execute(self, a, b):
        if b != 0:
            print("Result:", a/b)
        else:
            raise ValueError("The DivideByZero Exception Occured")
        