##
# main.py
# Date: 23/07/2022
# Author: Ryan Gordon
# Prints out dad jokes at random until the user terminates the program

import random
from time import sleep
import json

if __name__ == "__main__":
    # Load the jokes.
    jokes = json.load(open("jokes.json"))
    random.shuffle(jokes)

    print("Welcome to Dad Jokes :) ")
    input("Press ctrl+c to exit at any time (but pls don't)")

    try:
        # Loop until all jokes in the jokes() function have been told
        for joke in jokes:
            print(f"\n{joke[0]}")
            input("Press enter to find out the answer... ")
            print(joke[1])
            sleep(2)

        print("\nWe're out of jokes sorry, but we'll have more soon :D\n")
    # There are two ways to end the program, print an appropriate message
    except KeyboardInterrupt:
        print("\nSorry to lose you before the end, come again soon!\n")
