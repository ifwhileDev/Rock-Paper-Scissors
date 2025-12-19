from random import randint
from sys import exit

def checkIfValuesAreEqual(user, pc):
    options = ["", "ROCK", "PAPER", "SCISSORS"]
    possibilities = [1, 2, 3]

    if user not in possibilities:
        print("\033[0;30;41mInvalid option! Try again.\033[m")
        return

    print(f"Your bet was {options[user]}")
    print(f"The PC bet was {options[pc]}")
    print("-=" * 20)

    if user == pc:
        print("\033[0;30;43mDraw! :)\033[m")
    elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
        print("\033[0;30;42mYou won!\033[m")
    else:
        print("\033[0;30;41mPC won!\033[m")
    print("-=" * 20)

while True:
    try:
        userChoice = int(input("[1] Rock\n[2] Paper\n[3] Scissors\nYour bet: "))
        pcChoice = randint(1, 3)
        checkIfValuesAreEqual(userChoice, pcChoice)
    except ValueError:
        print("Please, type a number!")
        continue

    playAgain = input("Do you want to play again? [Y/N]\n").upper().strip()
    if playAgain != "Y":
        break

print("See you...")
