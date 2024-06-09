
import random
def getuserchoice():
    choices=['rock','paper','scissor']
    user_choice=input("enter your choice: ")
    if user_choice in choices:
        return user_choice
    else:
        print('invalid choice')
# getuserchoice()

def computerchoice():
    choices=['rock','paper','scissor']
    return random.choice(choices)
# print(computerchoice())

def determinewinner(user_choice, computer_choice):
    if user_choice==computer_choice:
        return 'tie'
    elif user_choice=='rock':
        if computer_choice=='scissor':
            return 'user'
        else:
            return 'computer'
    elif user_choice=='paper':
        if computer_choice=='rock':
            return 'user'
        else:
            return 'computer'
    elif user_choice=='scissor':
        if computer_choice=='paper':
            return 'user'
        else:
            return 'computer'
# user_choice='paper'
# computer_choice='scissor'
# print(determinewinner(user_choice, computer_choice))

def rockpaperscissor():
    print('welcom to the rock paper scissor game')
    while True:
        user_choice=getuserchoice()
        computer_choice=computerchoice()
        winner=determinewinner(user_choice, computer_choice)
        if winner=='tie':
            print("game is tie")
        elif winner=='user':
            print('you are the winner for this game')
        else:
            print('computer is the winner')
            print('Thank you for playing')
rockpaperscissor()

