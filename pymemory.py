
import random
def generateboard():
    cards=['A','B','C','D','E','F','G','H']
    totalcards=cards*2
    random.shuffle(totalcards)
    return totalcards
# print(generateboard())

open=[]
def displayboard(board):
    for i in range(0,len(board),4):
        row=board[i:i+4]
        for card in row:
            if card in open:
                print(card,end=' ')
            else:
                print("*",end=' ')
        print()

def pickedcard(dic,user_choice1,user_choice2):
    if dic[user_choice1]==dic[user_choice2]:
        print(dic[user_choice1],dic[user_choice2])
        return True
    else:
        print(dic[user_choice1],dic[user_choice2])
        return False
    
def marknumber(card):
    if card not in open:
        open.append(card)

def main():
    print("welcome to the memory game")
    board=generateboard()
    dic={
        '00':board[0],'01':board[1],'02':board[2],'03':board[3],
        '10':board[4],'11':board[5],'12':board[6],'13':board[7],
        '20':board[8],'21':board[9],'22':board[10],'23':board[11],
        '30':board[12],'31':board[13],'32':board[14],'33':board[15],
    }
    print(dic)
    playerscore=[0,0]
    currentplayer=0
    opened_pairs=0
    while opened_pairs<8:
        print("you need to open all the pairs to win")
        print("Exit to end the game")
        displayboard(board)
        print(f"Player {currentplayer + 1}'s turn. Current score: {playerscore[currentplayer]}")
        user_choice1=input("enter your card1 possition to open: ")
        user_choice2=input("enter your card2 possition to open: ")
        if user_choice1 in dic and user_choice2 in dic and user_choice1!=user_choice2:
            if pickedcard(dic,user_choice1,user_choice2):
                opened_pairs+=1
                playerscore[currentplayer]+=1
                card1=dic[user_choice1]
                card2=dic[user_choice2]
                marknumber(card1)
                marknumber(card2)
                print("openedpairs")
            else:
                currentplayer = 1 - currentplayer
        else:
            print("invalid card possition.try again")
    print("game over!")
    print(f"player 1s score:{playerscore[0]}")
    print(f"player 2s score:{playerscore[0]}")
    if playerscore[0]>playerscore[1]:
        print("player1 winner")
    elif playerscore[1]>playerscore[0]:
        print("player2 winner")
    else:
        print("tie the game")
  
main()


    









