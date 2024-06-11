import random
def initialize_game(min,max):
    return random.randint(min,max)
# print(initialize_game(1,99))

def player_guess(min,max):
    while True:
        try:
            guess=int(input("enter the number: "))
            if min<=guess<=max:
                return guess
            else:
                print("enter number between min and max")
        except ValueError:
            print("Invalid number")
# player_guess(min,max)


def feedback(guess,secret_num):
    if guess<secret_num:
        print("To low")
    elif guess>secret_num:
        print("To high")
    else:
        print("congratulation! guess is correct")
# guess=30
# secret_num=50
# feedback(guess,secret_num)

def check_win(guess,secret_num):
    return guess == secret_num
    # if guess==secrete_num:
    #     return True 
    # else:
    #     return False
# guess=55
# secrete_num=30
# print(check_win(guess,secrete_num))

def play_game(min,max):
    print("welcome to number guessing game!")
    secret_num=initialize_game(min,max)
    while True:
        # secret_num=initialize_game(min,max)
        # print(secret_num)
        guess = player_guess(min,max)
        feedback(guess, secret_num)
        if check_win(guess, secret_num):
            break
play_game(1,100)


        




