import random


def guessing_game():
    number_to_guess = random.randint(0, 100)
    chances = 3

    while chances > 0:
        user_guess = int(input(f"Guess the number between 0 and 100. You have {chances} more chance(s)!\n"))
        if number_to_guess == user_guess:
            print(f"You did it, the number was {number_to_guess}!")
            chances = 0
        elif number_to_guess < user_guess:
            print(f"Too high, guess again!")
            chances -= 1
        else:
            print(f"Too low, guess again!")
            chances -= 1

guessing_game()