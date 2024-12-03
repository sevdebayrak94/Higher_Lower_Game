# Display art by importing other .py code
#Import necessary data
from random import randint
from art import logo, vs
from game_data import data

score = 0
def check(user_guess, a_account, b_account):
    if user_guess == "A" and a_account > b_account:
        return True
    elif user_guess == "B" and b_account > a_account:
        return True
    else:
        return False


game_continue = True
while game_continue:
    #Choose random data and format the account
    account_a = data[randint(0,50)]
    account_b = data[randint(0,50)]
    if account_a == account_b:
        account_b = data[randint(0,50)]
    print(logo)
    if score != 0:
        print(f"Your current score is {score}")
    print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}")
    print(vs)
    print(f"Against B: {account_b['name']}, {account_b['description']}, from {account_b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    result = check(guess, account_a["follower_count"], account_b["follower_count"])
    if result == True:
        score += 1
        print(f"Your score is {score}")
    else:
        game_continue = False
        new_game = input(f"Your score is {score}. Do you want to play again 'y' or 'n': ").upper()
        if new_game == "Y":
            score = 0
            game_continue = True
        else:
            print("It was pleasure to play with you :)")



