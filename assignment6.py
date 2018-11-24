'''
Program description : This is my submission for assignment 6, which utilizes the card class created during assignment 5
but adds a series of try / except statements to ensure that valid values are being passed. It is tested on all cases.
Author : Pranav Eranki, 10/27/18
Changes : 11/1/2018 - Fixed some suggestions from the grading of assignment 5
'''

class Card:
    '''
    This class represents a card object, with a rank and a suit.
    It has getters, a string value, and a blackjack value calculator.
    '''
    def __init__(self, rank, suit):
        if not (type(rank) == int):
            raise TypeError
        else:
            if (rank > 14 or rank < 0):
                raise ValueError
            else:
                self.rank = rank

        if not (type(suit) == str):
            raise TypeError
        else:
            if not (suit in {'s', 'h', 'c', 'd'}):
                raise ValueError
            else:
                self.suit = suit

    ''' The below code is unmodified continuation of code from assignment 5'''
    def getRank(self): # This is a getter to return the rank, some checks in place. No parameters necessary.
        if self.rank < 0 or self.rank > 13:
            return 0
        else:
            return self.rank

    def getSuit(self): # This is a getter to return the suit, some checks in place. No parameters necessary.
        if self.suit != "c" and self.suit != "d" and self.suit != "s" and self.suit != "h":
            return "An invalid suit."
        else:
            return self.suit

    def bjValue(self): # This method returns the black jack value, or 0 if the rank is invalid. No params necessary.
        if self.rank > 10:
            return 10
        elif self.rank < 11 and self.rank > 0:
            return self.rank
        else:
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
            values = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
            references = [2,3,4,5,6,7,8,9,10]
            toRet += str(values[references.index(self.rank)])

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

# Helper method to reduce clustering in main method
def tryExcept(rank, suit):
    try:
        c = Card(rank, suit)
        print(c.bjValue())
        print(c)
    except TypeError:
        print("An error occured with the types of the parameters passed")
    except ValueError:
        print("An error occured with the value of the parameters passed")


# Main method itself
def main():
    # Type Errors
    tryExcept('n', -1)
    tryExcept('n', 'n')
    tryExcept(1,1)
    print()
    # Value Errors
    tryExcept(-1, 'n')
    tryExcept(4, 'l')
    tryExcept(100, 'h')
    print()
    # Working
    tryExcept(13, 's')
    tryExcept(10, 'c')
    tryExcept(1, 'h')
    tryExcept(5, 'd')

if __name__ == '__main__':
    main()


''' ### OUTPUT ###
An error occured with the types of the parameters passed
An error occured with the types of the parameters passed
An error occured with the types of the parameters passed

An error occured with the value of the parameters passed
An error occured with the value of the parameters passed
An error occured with the value of the parameters passed

10
King of Spades
10
10 of Clubs
1
Ace of Hearts
5
5 of Diamond
'''