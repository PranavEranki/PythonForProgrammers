"""
Defines class Contact
"""
class Contact:
    """
    One object of class Contact represents one person's contact info.
    """
    def __init__(self, name, phone, email, streetAddress):
        """"
        initializes every new object of class Contact
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.streetAddress = streetAddress

    def __str__(self):
        """
        returns a string containing the data in the Contact
        """
        return "%s\n%s\n%s\n%s\n" % (self.name, self.phone,self.email,self.streetAddress)
"""
Defines class ContactList, in file contactList.py
"""
class ContactList:
    """
    One object of class ContactList represents a list of Contact objects. It
    can function as an address book
    """
    def __init__(self):
        """
        initializes a new ContactList object
        """
        self.list = []

    def add(self, newContact):
        """
        adds newContact to the ContactList
        """
        self.list.append(newContact)

    def __str__(self):
        """
        returns a string containing all the data in the ContactList
        """
        returnedString = ""
        for contact in self.list:
            returnedString = returnedString + "\n" + str(contact)
        return returnedString

    def find(self, name):
        for contact in self.list:
            if (contact.name == name):
                return str(contact)

# tests class ContactList

if __name__ == "__main__":
    myFriends = ContactList()
    friend1 = Contact("Mickey", "650-345-3333", "Mickey@disneyland.com", "Disneyland, California")
    friend2 = Contact("Minnie", "650-345-3344", "Minnie@disneyworld.com", "Disneyworld, Florida")
    friend3 = Contact("Donald", "650-345-3333", "Donald@EuroDisney.com", "EuroDisney, France")
    myFriends.add(friend1)
    myFriends.add(friend2)
    myFriends.add(friend3)
    print (myFriends)
    print()
    print()
    print()
    print()
    print(myFriends.find("Minnie"))