
import random
def create_deck():
    values=[2,3,4,5,6,7,8,9,10,10,10,10,1]
    deck=values*4
    random.shuffle(deck)
    return deck
# print(create_deck())

def deal_card(deck):
    return deck.pop()
# deck=create_deck()
# print(deck_card(deck))

def calculate_score(cards):
    score=0
    Ace=False
    for card in cards:
        score+=card
        if card==11:
            Ace==True
    if Ace and score+10<=21:
        return score+10
    return score
# cards=[1,4,2]
# print(calculate_score(cards))   

def play_game():
    print("welcome to the blackjack game")
    deck = create_deck()
    # print(deck)
    player_cards = [deal_card(deck), deal_card(deck)]
    dealer_cards = [deal_card(deck), deal_card(deck)]
    while True:
        player_score = calculate_score(player_cards)
        # print(player_score)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        if player_score > 21:
            print("You are lose")
            return
        player_choice = input("Type 'y' get another card, 'n' to pass: ")
        if player_choice == 'y':
            player_cards.append(deal_card(deck))
        else:
            break
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card(deck))
    dealer_score = calculate_score(dealer_cards)
    # print(dealer_score)
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}")
    if dealer_score > 21 or player_score > dealer_score:
        print("You are winner")
    elif player_score < dealer_score:
        print("You are loser")
    else:
        print("It's a draw")
play_game()
