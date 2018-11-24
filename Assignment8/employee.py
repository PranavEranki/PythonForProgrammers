class Employee:
    """
    One object of this class represents an employee with a name, SSN, and salary
    """
    def __init__(self, firstName, lastName, SSN, salary):
        """
        This init method initializes a new employee with 4 parameters: A first name, last name, SSN, and salary.
        """
        self.firstName = firstName
        self.lastName = lastName
        self.ssn = SSN
        self.salary = salary

    def __str__(self):
        """
        A to string method to print the ssn and salary, along with full name, in a somewhat eloquent fashion
        """
        return (self.firstName + " " + self.lastName + " \n" + "has the social security number: " + str(self.ssn) + "\nand the salary: " + str(self.salary))

    def giveRaise(self, percentRaise):
        """
        Puts the salary to 100% + percentRaise of its original value
        """
        self.salary = self.salary * (1 + percentRaise/100)


    def __eq__(self, other):
        """
        This method returns true if both the first and last names of the two employees match (case insensitive)
        """
        return (self.firstName.lower() == other.firstName.lower() and self.lastName.lower() == other.lastName.lower())

    def __lt__(self, other):
        """
        This method essentially compares the alphabetical sorting of the current employee's name to the name of the other employee, returns true if this name comes before the other name
        """

        if (self.lastName.lower() == other.lastName.lower()):
            return self.firstName.lower() < other.firstName.lower()
        else:
            return self.lastName.lower() < other.lastName.lower()


