##62.	Implement a simple game (e.g., Guess the Number) using branching and loops.

import random

number= random.randint(1,10)
while True:
    guess =int(input("guess a number betwwen 1 and 10:"))
    if guess == number:
       print("correct! you guessed it !")
       break
    else:
       print("try again!")