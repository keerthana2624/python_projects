import random

def generateboard():
    # Create a list of cards, with each card appearing twice
    cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    totalcards = cards * 2
    # Shuffle the list to randomize the board
    random.shuffle(totalcards)
    return totalcards

# List to keep track of opened cards
openedcards = []

def display(board):
    # Display the current state of the board
    for i in range(0, len(board), 4):
        row = board[i:i+4]
        for card in row:
            # Show the card if it has been opened, otherwise show "*"
            if card in openedcards:
                print(card, end=' ')
            else:
                print("*", end=' ')
        print()

def pickedCard(dic, choice1, choice2):
    # Check if the two chosen cards match
    if dic[choice1] == dic[choice2]:
        print(dic[choice1], dic[choice2])
        return True
    else:
        print(dic[choice1], dic[choice2])
        return False

def markNumber(card):
    # Mark the card as opened
    if card not in openedcards:
        openedcards.append(card)

def play():
    """Main function to play the memory game."""
    print("Welcome to the memory game")
    board = generateboard()
    # Create a dictionary to map board positions to card values
    dic = {
        "00": board[0], "01": board[1], "02": board[2], "03": board[3],
        "10": board[4], "11": board[5], "12": board[6], "13": board[7],
        "20": board[8], "21": board[9], "22": board[10], "23": board[11],
        "30": board[12], "31": board[13], "32": board[14], "33": board[15]
    }

    print(dic)
    
    print('''The board is a 4x4 matrix, each card position is a combination of row and column.
              For example, the first element's position is 00 which is row=0:col=0,
              and the second element's position is 01 which is row=0:col=1.''')

    # Initialize player scores and set the starting player
    player_scores = [0, 0]
    current_player = 0
    revealed_pairs = 0

    while revealed_pairs < 8:
        print("You need to reveal all pairs to win the game.")
        print("Enter 'exit' to end the game.")
        display(board)
        
        # Display current player's turn and score
        print(f"Player {current_player + 1}'s turn. Current score: {player_scores[current_player]}")
        choice1 = input("Enter your card1 position to open (e.g., '00', '23'): ")
        if choice1.lower() == "exit":
            break
        choice2 = input("Enter your card2 position to open (e.g., '01', '32'): ")
        if choice2.lower() == "exit":
            break

        # Ensure valid input for card positions
        if choice1 in dic and choice2 in dic and choice1 != choice2:
            if pickedCard(dic, choice1, choice2):
                # If a match is found, increase the current player's score and revealed pairs count
                revealed_pairs += 1
                player_scores[current_player] += 1
                card1 = dic[choice1]
                card2 = dic[choice2]
                markNumber(card1)
                markNumber(card2)
                display(board)
                print(f"Pairs revealed: {revealed_pairs}")
            else:
                # Switch to the other player if no match is found
                current_player = 1 - current_player
        else:
            print("Invalid card positions. Please try again.")
        
    print("Game over!")
    # Display final scores
    print(f"Player 1's score: {player_scores[0]}")
    print(f"Player 2's score: {player_scores[1]}")
    
    # Determine the winner
    if player_scores[0] > player_scores[1]:
        print("Player 1 wins!")
    elif player_scores[1] > player_scores[0]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

play()
