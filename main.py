"""
Module :
The main method to start the application by calling the run command in App by initialising the object.
"""
from app import App

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    App().run()  # Instantiate an instance of App
