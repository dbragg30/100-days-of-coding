from random import randint
from art import logo

easy_level_turns = 10
hard_level_turns = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You loose")
            return
        elif guess != answer:
            print("guess again.")


game()
