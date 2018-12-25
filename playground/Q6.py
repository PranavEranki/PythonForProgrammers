""" One object of class Account represents one bank account """
class Account:
   def __init__(self):
      print ("Account constructor")
      self.balance = 0
      self.customer = "Mickey Mouse"

   def deposit(self, amount):
      self.balance = self.balance + amount

   def __str__(self):
      return "%s has a balance of %d" % (self.customer, self.balance)

   def __int__(self):
       return self.balance

class SavingsAccount (Account):
   def __init__(self):
        Account.__init__(self)  # calls the Account constructor to initialize that part of the object
        print ("SavingsAccount constructor")
        self.interestRate = 0.05

   def __str__(self):
        return Account.__str__(self) + ", and the interest rate is " + str(self.interestRate)



def main():
    acc1 =  SavingsAccount()
    acc1.deposit(100)
    print(acc1)
    x = int(acc1)
    print(str(x))

if __name__ == '__main__':
    main()