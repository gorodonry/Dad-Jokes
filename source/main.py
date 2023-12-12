##
# main.py
# Date: 23/07/2022
# Author: Ryan Gordon
# Prints out dad jokes at random until the user terminates the program

import random
import json
from time import sleep

if __name__ == "__main__":
    jokes = json.load(open("jokes.json"))
    random.shuffle(jokes)

    print("Welcome to Dad Jokes :) ")
    print("Press ctrl+c to exit at any time (but pls don't)")

    try:
        for joke in jokes:
            print(f"\n{joke[0]}")
            input("Press enter to find out the answer... ")
            print(joke[1])

        print("\nWe're out of jokes sorry, but we'll have more soon :D\n")
        print("(Pssst, you could create a pull request with more jokes...)")
    except KeyboardInterrupt:
        print("\nSorry to lose you before the end, come again soon!\n")
