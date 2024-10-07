

#Write your code below this line 👇
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
print("welcome to Rock, Paper, Scissors!")
playerChoice = int(input("Choose one : 0 = Rock, 1= Paper, or 2 =scissors\n").lower())
if playerChoice >= 3:
    print("wrong choice you loose!")
print("You chose:\n")
print(game_images[playerChoice])
compPlay = random.randint(0,2)
w = "You win!!!"
L = "You loose!"
t = "You tied!"
print("Computer Chose:\n")
print(game_images[compPlay])
if playerChoice >=3:
    print("wrong choice you loose!")
if playerChoice == 0 and compPlay == 1:
   print(L)
elif playerChoice == 0 and compPlay == 2:
    print(w)
elif playerChoice == 1 and compPlay == 0:
    print(w)
elif playerChoice == 1 and compPlay == 2:
    print(L)
elif playerChoice == 2 and compPlay == 1:
    print(L)
elif playerChoice == 2 and compPlay == 1:
    print(w)
elif playerChoice == 1 and compPlay == 1:
    print(t)
elif playerChoice == 0 and compPlay == 0:
    print(t)
elif playerChoice == 2 and compPlay == 2:
    print(t)
else:
    print("Wrong choice you loose!")

