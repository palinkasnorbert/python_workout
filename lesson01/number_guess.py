import random


def guessing_game():
    number_to_guess = random.randint(0, 100)
    print(number_to_guess)

    while True:
        user_guess = int(input("Guess a number between 0 and 100. \n"))
        if number_to_guess == user_guess:
            print(f"You did it, the number was {number_to_guess}!")
            return False
        elif number_to_guess < user_guess:
            print(f"Too high, guess again!")
        else:
            print(f"Too low, guess again!")

guessing_game()