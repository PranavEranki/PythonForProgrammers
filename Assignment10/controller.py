from model import Counter
from view import MyFrame
import tkinter
"""
This program creates a GUI to convert between temperatures in
fahrenheit and temperatures in celsius. It has options to convert
the input to fahrenheit or celsius, and also contains the option to quit
from the program.

Author : Pranav Eranki 11/21/2018
"""
class Controller:
    """
    This controller for the temperature converter ensures that when
    a user presses a button on the view, this controller calls the appropriate
    methods in the Model and sets the output and such properly.
    """
    def __init__(self):
        # This starts the framework, instantiates the model, view, and starts
        # the event loop for buttons on the View
        root = tkinter.Tk()
        self.model = Counter()
        self.view = MyFrame(self)
        self.view.mainloop()

    def toCelsius(self):
        # This method is mapped to if a user presses the input to celsius option.
        # Then, it calls the model function on the input from that field,
        # and sets the output to the returned value
        inpt = self.view.inputField.get()
        output = self.model.toCelsius(inpt)
        self.view.outputField["text"] = str(output) + " Degrees Celsius"

    def toFahrenheit(self):
        # This method is mapped to if a user presses the input to fahrenheit option.
        # Then, it calls the model function on the input from that field,
        # and sets the output to the returned value
        inpt = self.view.inputField.get()
        output = self.model.toFahrenheit(inpt)
        self.view.outputField["text"] = str(output) + " Degrees Fahrenheit"

if __name__ == "__main__":
    c = Controller()