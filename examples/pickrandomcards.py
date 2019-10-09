'''
This program will create a pack of cards (52) - 13 each of spade, heart, diamond & club
Then we will shuffle and deck, pick 4 cards and display
'''
import itertools, random

# make a deck of cards - 14 each of given type. The product() function performs the Cartesian product of the two sequence
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
print("List of cards = ", deck)

# shuffle the cards
random.shuffle(deck)

# draw 4 cards 2 times
print("You got:")
for j in range(1,3):
    print("\n%d time" %j)
    for i in range(4):
        rand = random.randint(0,51)
        print(deck[rand][0], " of ", deck[rand][1], end=", ")
