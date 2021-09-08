# creating  a guess game 

import random

print("\n\tPYTHON GUESS GAME")
print("Try your luck here: ")

name = input("Enter Your Name: ")
name = name.capitalize()

print("Hi,%s! Let's play... "%name)

startGame = input("Type 'Yes' Start: ")
startGame = startGame.upper()

while True:
    if startGame == "YES":

        guessNumber = random.randint(1,10)
        
        number = int(input("Enter A Number: "))
    
        if number == guessNumber: 
          print("Your number is %d and it's correct."%number)
        else: 
          print("%d is wrong, correct number is %d."%(number, guessNumber))
    else:
        print("You have a typing mistake. ):  ")
exit()    
