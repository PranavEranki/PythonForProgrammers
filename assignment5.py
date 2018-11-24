'''
This program implements a Card class, which has an init method, two getters for its attributes 'rank' and 'suit',
a black jack value calculator, and an str method. It also has a few checks in place to ensure that neither
the suit nor the rank are 'bad' values.


'''
class Card:
    def __init__(self, rank, suit): # Initialization method. Two parameters - rank and suit of the card
        # Just some simple checks for sanity
        if rank < 0 or rank > 13:
            print (str(rank) + " is an invalid rank...")
        if suit != "c" and suit != "d" and suit != "s" and suit != "h":
            print(suit + " is an invalid suit...")

        self.rank = rank # This is initializing the rank of the card
        self.suit = suit # This initializes the suit of the card

    def getRank(self): # This is a getter to return the rank, some checks in place. No parameters necessary.
        if self.rank < 0 or self.rank > 13:
            print("Invalid rank value, returning 0")
            return 0
        else:
            return self.rank

    def getSuit(self): # This is a getter to return the suit, some checks in place. No parameters necessary.
        if self.suit != "c" and self.suit != "d" and self.suit != "s" and self.suit != "h":
            print("Invalid suit value, returning 'of invalid suit' ")
            return "An invalid suit."
        else:
            return self.suit

    def bjValue(self): # This method returns the black jack value, or 0 if the rank is invalid. No params necessary.
        if self.rank == 1:
            return 1
        elif self.rank > 10:
            return 10
        elif self.rank < 11 and self.rank > 0:
            return self.rank
        else:
            print("Invalid black jack value, returning 0.")
            return 0

    def __str__(self):
        # This method returns what is to be printed out for the
        # name of the card, which is based on its rank and its suit.
        # No params necessary.
        toRet = ""

        # Ranks - 1 to 13
        if self.rank == 1:
            toRet += "Ace"
        elif self.rank == 11:
            toRet += "Jack"
        elif self.rank == 12:
            toRet += "Queen"
        elif self.rank == 13:
            toRet += "King"
        else:
            toRet += str(self.rank)

        # suits - d, c, h, s
        if self.suit == 'd':
            toRet += " of Diamond"
        elif self.suit == 'c':
            toRet += " of Clubs"
        elif self.suit == 'h':
            toRet += " of Hearts"
        elif self.suit == 's':
            toRet += " of Spades"
        else:
            toRet += " of an invalid suit."

        # Returning
        return toRet


# Testing card declarations
one = Card(12, "d")
two = Card(1, "s")
three = Card(11, "h")
four = Card(13, "h")
five = Card(5, "p")
cards = [one, two, three, four, five]

# Printing
for c in cards:
    print(c)
    print(c.getRank())
    print(c.getSuit())
    print(c.bjValue())

''' ### OUTPUT ###
p is an invalid suit...
Queen of Diamond
12
d
10
Ace of Spades
1
s
1
Jack of Hearts
11
h
10
King of Hearts
13
h
10
5 of an invalid suit.
5
Invalid suit value, returning 'of invalid suit'
An invalid suit.
5


'''