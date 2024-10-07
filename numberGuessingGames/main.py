import random, clear
from art import logo

gameNumber = random.randint(1,100)
numberTurns = 0
gameOver = False

def levelDifficulty():
    global numberTurns
    gameDifficulty = (input("Please choose difficulty: Type 'easy' or 'hard' : ").lower())
    # print(gameDifficulty)
    if gameDifficulty == "easy":
        numberTurns = 9
    elif gameDifficulty == "hard":
        numberTurns = 4

    else:
        print("incorrect choice!")
        exit()


def highLow():
    global numberTurns
    if userGuess == gameNumber:
        print("You guessed the number! You Win!")
        exit()
    elif userGuess >= gameNumber:
        print("Too high.")
        numberTurns -= 1
        return numberTurns
    else:
        print("Too Low.")
        numberTurns -= 1
        return numberTurns


gameNumber = random.randint(1,100)
numberTurns = 0
gameOver = False

print(logo)
# print(f"hint the number is {gameNumber}")
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
levelDifficulty()

while not gameOver:
    print(f"Chances remaining {numberTurns + 1}")
    userGuess = int(input("Make a guess: "))
    if numberTurns == 0:
        print("no more chances left! Game Over")
        gameOver = True
    print(f"You have {numberTurns} chances left")
    if userGuess < 1 or userGuess > 100:
        print("you chose a number outside of the game range.")
    highLow()


