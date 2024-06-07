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

def makeMove(board, player, row, col):
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = player
        return True
    return False
# board=initializeBoard()
# player=1
# row=0
# col=0
# print(makeMove(board,player,row,col))

def checkWin(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None
# print(checkWin(board))