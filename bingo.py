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
                board[i][j]="x"
    return board
board=generateBoard() 
displayBoard(board)
number=9       
# markNumber(board,number)

def getUserNumber():
    try:
        n=int(input("enter the number:"))
        if 1<=n<101:
            return n
        elif n<0 and n>100:
            print("invalid number! try again")
        else:
            print("please enter the valid number")
    except:
        print("error in try block")
# getUserNumber()

def horizental(board):
    lst=[]
    for row in range(5):
        lst.append(str(board[row][0])+ str(board[row][1])+str(board[row][2])+ str(board[row][3])+ str(board[row][4]))
    return lst 
def vertical(board):
    lst=[]
    for col in range(5):
        lst.append(str(board[0][col])+str(board[1][col])+str(board[2][col])+str(board[3][col])+str(board[4][col]))
    return lst
def diagonal(board):
    leftdown=(str(board[0][0])+str(board[0][1])+str(board[0][2])+str(board[0][3])+str(board[0][4]))
    rightdown=(str(board[0][4])+str(board[1][3])+str(board[2][2])+str(board[3][1])+str(board[4][0]))
    return(leftdown,rightdown)
def isfull(board):
    for row in range(5):
        for col in range(5):
            if [row][col]!="x":
                return False
    return True
def checkwin(board):
    # x=horizental(board)
    # y=vertical(board)


    x=horizental(board)

    for line in x:
        if line=="xxxxx":
            return True
    for line in vertical(board):
        if line=="xxxxx":
            return True 
    leftwin,rightwin=diagonal(board)
    if leftwin=="xxxxx" or rightwin=="xxxxx":
        return True
    return False
# board=generateBoard()
# checkwin(board)

def playbingogame():
   board=generateBoard()
   displayBoard(board)
   print("welcome to the game")
   k=0
   while True:
       n=getUserNumber()
       newboard=markNumber(board,n)
       displayBoard(newboard)
       if checkwin(board)==True:
           break
       k+=1
   print("you are the winner for this game")
   print("no.of rounds",k)
playbingogame()       
