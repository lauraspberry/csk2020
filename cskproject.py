import random
import sys
import time
import rockpaperscissors
import tictactoe
import guess

typing_speed = 350
def slow_type(msg): #maybe include special OWO syntax here
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')


slow_type("As you're coding your CSK project, you see a strange popup. Someone programmed an owobot to infiltrate your computer and fill it with OWOs! It's up to you to defeat owobot before it takes over.")
slow_type("OWO TEST 1: THE NOT-SO-STRATEGIC SELECTION OF AN ITEM (aka rock paper scissors).")
rockpaperscissors.rockpaperscissors()
slow_type("OWO TEST 2: THE STRATEGIC SELECTION OF AN ARBITRARY NUMBER (aka guess the number). Guess the number that owobot is thinking of!")
guess.func()
slow_type("OWO TEST 3: THE STRATEGIC PLACING OF CERTAIN ARBITRARY LETTERS. (aka tic-tac-toe).")
tictactoe.tictactoe()
print('OWOBOT CONGRATULATES YOU! YOU HAVE SUCCESSFULLY PROTECTED YOUR COMPUTER')