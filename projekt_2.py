"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Barbora Benešová
email: benes.barbora@seznam.cz
discord: Barbora B.#4707
"""

import random
from projekt_2_knihovna import check_input_number
from projekt_2_knihovna import bulls_cows
from time import time
from datetime import timedelta

random_number=str(random.randint(1,9))
while len(random_number)!=4:
    a = str(random.randint(0,9))
    if a in random_number:
        continue
    else:
        random_number+=a

print(
f"""Hi There!
{50*'-'}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{50*'-'}""")
#print(random_number)

input_number = ""
number_guesses = 0
start = time()
while True:
    input_number=check_input_number(input("Enter a number:\n>>> "))
    number_guesses += 1
    if input_number == random_number:
        break
    bulls, cows = bulls_cows(input_number, random_number)
    print(f"{bulls} bulls, {cows} cows\n{50*'-'}")

guess_time=round(time()-start)
print(f"""Correct, you've guessed the right number
in {number_guesses} guesses!
Your time was {timedelta(seconds=guess_time)}
{50*'-'}""")


if number_guesses < 7:
    print("That's amazing!")
elif number_guesses < 12:
    print("That's good.")
elif number_guesses > 12:
    print("That's not so good." )
