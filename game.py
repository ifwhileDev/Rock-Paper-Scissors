from random import randint
from sys import exit

pcChoice = randint(1, 3)

def checkIfValuesAreEqual():
    numbersPossibilities = [1, 2, 3]
    if userChoice == 1 and pcChoice == 1:
        print("Your bet were ROCK")
        print("The CP bet was ROCK")
        print("-=" * 20)
        print("\033[0;30;43mEmpate! :)\033[m")
        print("-=" * 20)
    
    elif userChoice == 1 and pcChoice == 2:
        print("Your bet were ROCK")
        print("The CP bet was PAPER")
        print("-=" * 20)
        print("\033[0;30;41mCP won!\033[m")
        print("-=" * 20)

    elif userChoice == 1 and pcChoice == 3:
        print("Your bet were ROCK")
        print("The CP bet was SCISSORS")
        print("-=" * 20)
        print("\033[0;30;42mYou won!\033[m")
        print("-=" * 20)
        
    elif userChoice == 2 and pcChoice == 1:
        print("Your bet were PAPER")
        print("The CP bet was ROCK")
        print("-=" * 20)
        print("\033[0;30;42mYou won!\033[m")
        print("-=" * 20)
    
    elif userChoice == 2 and pcChoice == 2:
        print("Your bet were PAPER")
        print("The CP bet was PAPER")
        print("-=" * 20)
        print("\033[0;30;43mDraw! :)\033[m")
        print("-=" * 20)
    
    elif userChoice == 2 and pcChoice == 3:
        print("Your bet were PAPER")
        print("The CP bet was SCISSORS")
        print("-=" * 20)
        print("\033[0;30;41mCP won!\033[m")
        print("-=" * 20)
    
    elif userChoice == 3 and pcChoice == 1:
        print("Your bet were SCISSORS")
        print("The CP bet was ROCK")
        print("-=" * 20)
        print("\033[0;30;41mCP won!\033[m")
        print("-=" * 20)
    
    elif userChoice == 3 and pcChoice == 2:
        print("Your bet were SCISSORS")
        print("The CP bet was PAPER")
        print("-=" * 20)
        print("\033[0;30;42mYou won!\033[m")
        print("-=" * 20)
    
    elif userChoice == 3 and pcChoice == 3:
        print("Your bet were SCISSORS")
        print("The CP bet was SCISSORS")
        print("-=" * 20)
        print("\033[0;30;43mDraw! :)\033[m")
        print("-=" * 20)
        
    elif userChoice not in numbersPossibilities:
        print("-=" * 25)
        print("\033[0;30;41mInvalid option! Run it again.\033[m")
        print("-=" * 25)
        exit()

userChoice = int(input("[1] Rock\n[2] Paper\n[3] Scissors\nYour bet: "))
print(f"PC: {pcChoice}")
checkIfValuesAreEqual()
playAgain = str(input("Do you wanna play again? [Y/N]\n")).upper().strip()
print("-=" * 20)

while playAgain == "Y":
    userChoice = int(input("[1] Rock\n[2] Paper\n[3] Scissors\nYour bet: "))
    pcChoice = randint(1, 3)
    print(f"PC: {pcChoice}")
    checkIfValuesAreEqual()
    playAgain = str(input("Do you wanna play again? [Y/N]\n")).upper().strip()
    print("-=" * 20)
print("See you...")