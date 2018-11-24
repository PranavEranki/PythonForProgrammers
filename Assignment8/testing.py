from employee import Employee
from manager import Manager


def main():
    # This is the testing method. It tests sorting, creation of employees and managers, and the
    # <, >, and == methods on the employees
    employee_1 = Employee("John", "Doe", 5001, 15)
    employee_2 = Employee("John", "Doe", 5002, 18)
    employee_3 = Employee("Andrew", "Nelson", 5003, 23)
    employee_4 = Employee("Yin", "Yang", 5004, 28)
    manager_1 = Manager("John", "Doe", 5011, 90, "Boss", 15)
    manager_2 = Manager("Jasper", "Doe", 5012, 36, "Sub 1", 5)
    manager_3 = Manager("Jeffrey", "Don", 5013, 45, "Better Sub", 7)

    print()
    print("Output of tests")
    print()

    # TESTS FOR <, > AND == FOR EMPLOYEES #
    print(employee_1 < employee_2) # Should be false
    print(employee_1 > employee_2) # Should be false
    print(employee_1 == employee_2) # Should be true
    print(employee_3 > employee_1) # Should be true
    print(employee_2 > employee_4) # Should be false
    print(employee_2 == employee_4) # Should be false

    # TESTS FOR <, > AND == FOR MANAGERS #
    print(manager_1 < manager_2) # Should be false
    print(manager_3 > manager_1) # Should be true
    print(manager_3 == manager_1) # Should be false

    print()
    print("Original list")
    print()

    # Since sorting occurs based on names, it is sufficient if we just print the names
    # when testing if our code sorting worked
    employees_and_managers = [employee_4, employee_3, employee_2, employee_1, manager_1, manager_2, manager_3]
    for elem in employees_and_managers:
        print(elem.firstName + " " + elem.lastName)

    print()
    print("Now, the sorted list")
    print()

    employees_and_managers.sort()
    for elem in employees_and_managers:
        print(elem.firstName + " " + elem.lastName)


if __name__ == "__main__":
    main()



""" ### OUTPUT ###

Output of tests

False
False
True
True
False
False
False
True
False

Original list

Yin Yang
Andrew Nelson
John Doe
John Doe
John Doe
Jasper Doe
Jeffrey Don

Now, the sorted list

Jasper Doe
John Doe
John Doe
John Doe
Jeffrey Don
Andrew Nelson
Yin Yang


"""