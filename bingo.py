import random
def generateBoard():
    x=random.sample(range(1,101),25)
    board=[['.','.','.','.','.']for _ in range(5)]
    for i in range(5):
        for j in range(5):
            board[i][j]=x[i*5+j]
    return board
# print(generateBoard())

def displayBoard(board):
    for i in range(5):
        for j in range(5):
            print(board[i][j],end=' ')
        print("\n")
    return None
# board=generateBoard()
# displayBoard(board)