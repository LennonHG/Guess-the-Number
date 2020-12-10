# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import random 

guessLimit = 0
score = 100


print("Dear User")
print("To play the guessing game, please enter a number between")
print("1 to 100\n")
print("Please Note, each wrong guess will be -10 from your")
print("100 initial score\n")

number = random.randint(1,100)
# print("Random Number Generated " + str(number))
while guessLimit < 10:
    print("please enter your guess")
    guess = input()
    guess = int(guess)
    if guess < number:
        print("The number you choose is too low")
        y = input("Press Y for Hints! and N to continue: ")
        try:
            if y == "Y" or y == "y" :
                a1 = number + 10
                a2 = number - 10
                print("Number is in between " + str(a2) + " and " + str(a1))
        except:
            break
    elif guess > number:
        print("The number you choose is to high")
        z = input("Press Y for Hints! and N to continue: ")
        try:
            if z == "Y" or z == "y":
                a1 = number + 10
                a2 = number - 10
                print("Number is in between " + str(a2) + " and " + str(a1))
        except:
            break
    elif guess == number:
        break
    
    guessLimit += 1
    score -= 10 
if guessLimit == 10:
    print("guess limit has exceeded")
    print("Your final score: " + str(score))
if guess == number:
    print("Congrats you have manage to correctly guess the number!")
    print("Your final score: " + str(score))
