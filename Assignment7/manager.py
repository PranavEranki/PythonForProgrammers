from employee import Employee
"""
This program implements a manager class, which is essentially an employee class
but it has the manager title and additional bonus.

Pranav Eranki
11/13/18
"""

class Manager(Employee):
    def __init__(self,  firstName, lastName, SSN, salary, title, bonus):
        Employee.__init__(self, firstName, lastName, SSN, salary)
        self.title = title
        self.bonus = bonus

    def __str__(self):
        return (Employee.__str__(self) + "\nand the manager title: " + self.title + "\nand the manager bonus: " + str(self.bonus))
