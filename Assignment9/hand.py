from random import randint
from card import Card

class Hand:
    # An object of this class represents a hand of cards. Each Hand stores some number of cards
    def __init__(self, numCardsInHand):
        """
        This is the initialzation method, which creates a new hand with the number
        of cards specified (each card is generated randomly)
        """
        self.handOfCards = []
        for i in range(numCardsInHand):
            # We need a random rank (1-13), and one random suit (1-4)
            rank = randint(1, 13)
            suits = ['s', 'h', 'c', 'd']
            suit = suits[randint(0, 3)]
            self.handOfCards.append(Card(rank, suit))

    def bjValue(self):
        """
        This returns the blackjack value for the whole hand of cards by summing
        the bj value for each card in the hand
        """
        x = 0
        for card in self.handOfCards:
            x += card.bjValue()
        return x

    def __str__(self):
        """
        This returns the string containing the name of each of the cards in the hand,
        Separated by new lines
        """
        toRet = "";
        for card in self.handOfCards:
            toRet += str(card) + "\n"
        return toRet

    def hitMe(self):
        """
        This adds a randomly generated card to the end of the hand
        Essentially the same code as in the init loop, but only called once
        """
        rank = randint(1, 13)
        suits = ['s', 'h', 'c', 'd']
        suit = suits[randint(0, 3)]
        self.handOfCards.append(Card(rank, suit))