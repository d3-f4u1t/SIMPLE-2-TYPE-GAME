#main.py

from game1 import *
from game2 import *
def c_s():

    print("Which game you would like to play:")
    print("1.STONE-PAPER-SCISSORS")
    print("2.ROLL THE DICE")
    print("3.EXIT")




while True:
    c_s()
    user_input = input("enter your choice:")


    if user_input == '1':
        print("STARTING GAME...")
        g1()

    elif user_input == '2':
        print("STARTING GAME...")
        g2()

    elif user_input == '3':
        print("Exiting the game. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    