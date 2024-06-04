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

def markNumber(board,number):
    for i in range(5):
        for j in range(5):
            if number==board[i][j]:
                board[i][j]=="x"
            return board
board=generateBoard() 
displayBoard(board)
number=9       
# markNumber(board,number)

def getUserNumber():
    try:
        n=int(input("enter the number"))
        if 1<=n<101:
            return True
        elif n<0 and n>100:
            print("invalid number! try again")
        else:
            print("please enter the valid number")
    except:
        print("error in try block")
# getUserNumber()

    
