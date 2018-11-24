from employee import Employee

class Manager(Employee):
    """
    This is a manager class, which is essentially an employee but with a manager title and a bonus
    """
    def __init__(self,  firstName, lastName, SSN, salary, title, bonus):
        """
        This method initializes a new Manager with name, SSN, salary given (calls super on the employee init), then also initializes Manager-independent variables (manager title and bonus)
        """
        Employee.__init__(self, firstName, lastName, SSN, salary)
        self.title = title
        self.bonus = bonus

    def __str__(self):
        """
        This prints out the attributes of the manager class, but in a somewhat eloquent fashion
        """
        return (Employee.__str__(self) + "\nand the manager title: " + self.title + "\nand the manager bonus: " + str(self.bonus))

