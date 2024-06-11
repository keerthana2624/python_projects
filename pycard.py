import random
cards=['A','2','3','4','5','6','7','8','9','10','J','K','Q']
totalcards=cards*4
values={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'K':10,'Q':10}
# print(totalcards)
# print(values)

def createcard(deck):
    random.shuffle(deck)
    return deck
# print(createcard(cards))

