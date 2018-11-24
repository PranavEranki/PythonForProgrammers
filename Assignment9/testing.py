from hand import Hand

"""
This program simulates a hand of cards using the previously defined card class from assignment 5.
The hand file contains the Hand of Cards class, the card class contains the Card class,
and this file contains the testing done to ensure that the Hand class is functional and meets requirements.

It also attempts the extra credit of saving a hand object to a pickle file and reading it
back into the program for usage. (Pickling)

Author: Pranav Eranki - 11/18/2018
"""


h1 = Hand(3)
print (h1.bjValue())
print (h1)
h1.hitMe()
print (h1)
print(h1.bjValue())
print()

h2 = Hand(2)
print (h2)
print (h1)


h3 = Hand(4)
print(h3.bjValue())
print(h3)

for i in range(5):
    h3.hitMe()
    print(h3.bjValue())

print("Third hand after 5 hits:")
print(h3)


""" 
### OUTPUT OF TESTING ###
20
Nine of Diamonds
Ace of Spades
Jack of Diamonds

Nine of Diamonds
Ace of Spades
Jack of Diamonds
Queen of Hearts

30

Ace of Spades
Five of Hearts

Nine of Diamonds
Ace of Spades
Jack of Diamonds
Queen of Hearts

23
Three of Spades
Seven of Diamonds
Queen of Clubs
Three of Spades

28
34
39
48
58
Third hand after 5 hits:
Three of Spades
Seven of Diamonds
Queen of Clubs
Three of Spades
Five of Spades
Six of Hearts
Five of Clubs
Nine of Hearts
King of Diamonds




"""


""" EXTRA CREDIT """
import pickle

print("Original hand of cards before saving: ")
print(h1)
print("Saving...")
print()

handData = open('hand.pkl', 'wb')
pickle.dump(h1, handData)
handData.close()

handData = open('hand.pkl', 'rb')
h1_test = pickle.load(handData)

print("Original hand of cards after saving and being read from pkl file: ")
print(h1_test)
print()

""" ### OUTPUT OF EXTRA CREDIT ###

Original hand of cards before saving:
Nine of Spades
Ace of Diamonds
Six of Hearts
Six of Clubs

Saving...

Original hand of cards after saving and being read from pkl file:
Nine of Spades
Ace of Diamonds
Six of Hearts
Six of Clubs


"""