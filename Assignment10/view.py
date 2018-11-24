import tkinter
"""
This program creates a GUI to convert between temperatures in
fahrenheit and temperatures in celsius. It has options to convert
the input to fahrenheit or celsius, and also contains the option to quit
from the program.

Author : Pranav Eranki 11/21/2018
"""
class MyFrame(tkinter.Frame):
    """
    This class creates the frame for our GUI application.
    It contains an input field, an output field, and two
    buttons on the left to convert the input to either
    fahrenheit or celsius depending on what the user
    """
    def __init__(self, controller):
        # This is the init method. It makes all 3 buttons, the entry field, and the
        # output field that we need for our program.
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller

        # To fahrenheit button
        self.toFahrenheit = tkinter.Button(self)
        self.toFahrenheit["text"] = "To Fahrenheit"
        self.toFahrenheit["command"] = self.controller.toFahrenheit
        self.toFahrenheit.pack({"side": "left"})

        # To celsius button
        self.toCelsius = tkinter.Button(self)
        self.toCelsius["text"] = "To Celsius"
        self.toCelsius["command"] = self.controller.toCelsius
        self.toCelsius.pack({"side": "left"})

        # Input field
        self.inputField = tkinter.Entry(self)
        self.inputField["text"] = "0"
        self.inputField.pack({"side": "left"})

        # Quit button
        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.pack({"side": "right"})

        # Output field
        self.outputField = tkinter.Label(self)
        self.outputField["text"] = "Output"
        self.outputField.pack({"side": "left"})
        self.outputField.pack({"side": "left"})



