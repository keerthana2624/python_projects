def initializeBoard():
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(' ')
        board.append(row)
    return board
# print(initializeBoard())

def displayBoard(board):
    print("\nCurrent Board:")
    for row in board:
        print("|".join(row))
        print("-" * 5)
    print()
# board=initializeBoard()
# displayBoard(board)