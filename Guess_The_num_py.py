import random as ran
ranNum = ran.randint(1,10)

startGame = int(input("Enter 0 to start and 1 to exit"))

while(startGame != 1):
    guess = int(input("Enter your guess number : "))