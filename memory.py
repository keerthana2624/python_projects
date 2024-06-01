import random

def generateBoard():
    """Generates and returns a shuffled board with pairs of cards."""
    cards = ["A", "C", "B", "D", "E", "F", "G", "H"]
    totalcards = cards * 2
    random.shuffle(totalcards)
    return totalcards

def display_board(board, guessed):
    """Displays the current state of the board, showing guessed cards and hiding unguessed ones."""
    for i in range(0, len(board), 4):
        row = board[i:i+4]
        for card in row:
            if card in guessed:
                print(card, end="  ")
            else:
                print("*", end="  ")
        print("\n")

def markNumber(board, card, guessed):
    """Marks a card as guessed if it has been picked."""
    for i in range(0, len(board), 4):
        row = board[i:i+4]
        for i in row:
            if card == i:
               guessed.append(i)
    return board

def pickedCard(dic, card1, card2):
    """Checks if two picked cards are a matching pair."""
    if dic[card1] == dic[card2]:
        print(dic[card1], dic[card2])
        print("You picked the same pair. Continue to pick the remaining cards.")
        return True
    else:
        print(dic[card1], dic[card2])
        print("You picked unpaired cards. Please try again.")
        return False

def main():
    board = generateBoard()
    guessed = []
    while len(guessed) < len(board):  
        display_board(board, guessed) 
        card1 = int(input("Enter the position of the first card: "))
        card2 = int(input("Enter the position of the second card: "))
        if pickedCard(board, card1, card2): 
            markNumber(board, card1, guessed) 
            markNumber(board, card2, guessed)
    print("Game over!")
main()




