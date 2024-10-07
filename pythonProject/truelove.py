# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lname1 = name1.lower()
lname2 = name2.lower()

lL = name1.count("l") + lname2.count("l")
lO = lname1.count("o") + lname2.count("o")
lV = name1.count("v") + lname2.count('v')
lE = name1.count("e") + lname2.count('e')
love = lL + lO + lV + lE


tT = name1.count("t") + lname2.count('t')
tR = name1.count("r") + lname2.count('r')
tU = name1.count("u") + lname2.count('u')
tE = name1.count("e") + lname2.count('e')
trueL = tT + tR + tU + tE

score = int('{}{}'.format(trueL, love))


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
        print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")





