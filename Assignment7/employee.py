"""
This is an employee class which implements the basic structure of an employee, with an
init method, to string method, and giveRaise method

Pranav Eranki
11/13/18
"""
class Employee:
    def __init__(self, firstName, lastName, SSN, salary):
        # The init method with the 4 parameters given
        self.firstName = firstName
        self.lastName = lastName
        self.ssn = SSN
        self.salary = salary

    def __str__(self):
        # A to string method to print the ssn and salary, along with full name, in a somewhat eloquent fashion
        return (self.firstName + " " + self.lastName + " \n" + "has the social security number: " + str(self.ssn) + "\nand the salary: " + str(self.salary))

    def giveRaise(self, percentRaise):
        # Puts the salary to 100% + percentRaise of its original value
        self.salary = self.salary * (1 + percentRaise/100)
