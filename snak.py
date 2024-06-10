def generateboard():
    board = []
    for row in range(10):
        row = []
        for i in range(10):
            row.append(0)
        board.append(row)
    return board
print(generateboard())

def displayBoard(board, player_position):
    for row in range(9, -1, -1):
        for col in range(10):
            cell = board[row][col]
            if cell == 0:
                print(f"{row * 10 + col + 1:6}", end=" ")
        print()
    print(f"Player Position: {player_position}\n")
board=generateboard()
player_position=
print(board,player_possition)