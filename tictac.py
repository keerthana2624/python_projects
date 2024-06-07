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


def checkDraw(board):
    for row in board:
        if ' ' in row:
            return False
    return True
# board=initializeBoard()
# print(checkWin(board))

def switchPlayer(current_player):
    if current_player == 'X':
        return 'O'
    return 'X'

def playTicTacToe():
    print("Welcome to Tic-Tac-Toe!")
    board = initializeBoard()
    current_player = 'X'
    
    while True:
        displayBoard(board)
        print(f"Player {current_player}'s turn")
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        if not makeMove(board, current_player, row, col):
            print("Invalid move. Try again.")
            continue
        
        if checkWin(board):
            displayBoard(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        
        if checkDraw(board):
            displayBoard(board)
            print("The game is a draw!")
            break
        
        current_player = switchPlayer(current_player)

playTicTacToe()



