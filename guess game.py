# creating  a guess game 

import random

print("\n\tPYTHON GUESS GAME")
guessUse = 0
guessNum = random.randint(1, 10)

while guessUse < 5:
    
    userNum = int(input("Enter a number b/w (1 - 10) : "))
    guessUse += 1
    if userNum < guessNum:
        print("You guess too low.")
    elif userNum > guessNum:
        print("You guess too high.")
    else:
        break
    
if userNum == guessNum:
    print(f"You took {guessUse} guesses to find the number {guessNum}.")
else:
    print(f"""______Time Out______
    The Number is {guessNum}
    """)
