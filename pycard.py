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

def dealcards(deck):
    half_cards=len(deck)//2
    return deck[0:half_cards:1],deck[half_cards::1]
# deck=createcard(cards)
# print(dealcards(deck))

def cardsvalues(card):
    return values[card]
# card='J'
# print(cardsvalues(card))

def play_game(player1_cards,player2_cards):
    player1_score=0
    player2_score=0
    for i in range(len(player1_cards)):
        card1 = player1_cards[i]
        card2 = player2_cards[i]
        value1 = cardsvalues(card1)
        value2 = cardsvalues(card2)
        print(f"Round {i+1}:")
        print(f"Player 1 plays {card1}")
        print(f"Player 2 plays {card2}")
        if value1 > value2:
            print("Player 1 win!")
            player1_score += value1 + value2
        elif value2 > value1:
            print("Player 2 win!")
            player2_score += value1 + value2
        else:
            print("It's a tie!")
        # print(f"Score: Player 1 = {player1_score}, Player 2 = {player2_score}\n")
    return player1_score, player2_score
# player1_cards=['A','7']
# player2_cards=['J','5']
# print(play_game(player1_cards,player2_cards))

def main():
    print("welcome to the Pycards Duel game")
    deck = createcard(totalcards)
    player1_cards, player2_cards = dealcards(deck)
    player1_score, player2_score = play_game(player1_cards, player2_cards)
    print("Final Scores:")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")
    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player2_score > player1_score:
        print("Player 2 wins the game!")
    else:
        print("game is a tie!")
main()
