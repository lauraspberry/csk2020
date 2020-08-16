
from random import randint



def func():
    computer = randint(0,100)
    person = int(input("guess a number that I'm thinking of! It's from 1-100: "))
    status = False
    counter = 0
    while status == False:
        if person > computer:
            print('guess lower!')
            person = int(input("guess again:"))
            counter += 1
        elif person < computer:
            print('guess higher!')
            person = int(input("guess again:"))
            counter += 1
        else:
            print("you guessed it! My number was " + str(computer) + ". You took " + str(counter) + " guesses, and you prevented owobot from taking over!")
            status = True


    def lose():
        print("you didn't guess my number. It was " + str(computer) +  ". Try again?")
        response = input("y/n")
        if response.lower() == "y":
            func()
        else:
            print("you lost :( uwu owobot has taken over!")
    def win():
        print("you won! :) you prevented owobot from taking over!")
