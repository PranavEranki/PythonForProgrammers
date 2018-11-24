"""
This program creates a GUI to convert between temperatures in
fahrenheit and temperatures in celsius. It has options to convert
the input to fahrenheit or celsius, and also contains the option to quit
from the program.

Author : Pranav Eranki 11/21/2018
"""
class Counter:
    """
    The counter class implements the logic for our programs,
    behaving as a set of methods we call on to convert the input
    of the user to either celsius or fahrenheit.
    """
    def toCelsius(self, degF):
        # This method converts the input in fahrenheit to celsius and returns it
        degF = float(degF)
        conversion = ((degF - 32) * 5/9)
        return round(conversion, 2)

    def toFahrenheit(self, degC):
        # this method converts the input in celsius to fahrenheit and returns it
        degC = float(degC)
        conversion = ((9 * degC / 5)+ 32)
        return round(conversion,2)
