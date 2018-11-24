from employee import Employee
from manager import Manager

"""
This program defines an employee class and another manager class which is a subclass
of the employee class. Then, we define a list with both classes and call some methods on
the classes.

Pranav Eranki
11/13/18
"""

JohnDoe_Employee = Employee("John", "Doe", 12345, 20)
StevenChen_Employee = Employee("Steven", "Chen", 23456, 35)
AndrewZhou_Employee = Employee("Andrew", "Zhou", 34567, 43)

JeffreyZhang_Manager = Manager("Jeffrey", "Zhang", 45678, 67, "Sales", 34)

allEmployees = [JohnDoe_Employee, StevenChen_Employee, AndrewZhou_Employee, JeffreyZhang_Manager]

for employee in allEmployees:
    employee.giveRaise(15) # Give everyone a 15% raise
    print(employee) # Print their new stats
    print() # Print a new line for clarity

"""  ### Ouput ###
John Doe
has the social security number: 12345
and the salary: 23.0

Steven Chen
has the social security number: 23456
and the salary: 40.25

Andrew Zhou
has the social security number: 34567
and the salary: 49.449999999999996

Jeffrey Zhang
has the social security number: 45678
and the salary: 77.05
and the manager title: Sales
and the manager bonus: 34

"""