
import random
def create_deck():
    values=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    deck=values*4
    random.shuffle(deck)
    return deck
# print(create_deck())

