#game1
'''this game is stone paper scissors
with ONE USER AND ONE COMPUTER'''


from random import randint,seed, random
from time import time

def g1():
    print("welcome to the game of rock paper scissors!")
    print("you will be playing against the computer")
    print("the typical rules of rock paper scissors wil be applied")

    while True:
        print("dificulty level:")
        print("PRESS ENTER FOR EASY MODE")
        print("PRESS 1 FOR HARD MODE")
        print("PRESS 2 FOR FEELING LUCKY MODE")
        d_input = input("enter your choice:")



        print("pls chose:")
        print("1.rock")
        print("2.paper")
        print("3.scissors")
        print("4.exit")
        user_score = 0
        comp_score = 0


        #adding a amll adition to this simple game with hard and feeling luck mode
        """where what happens is that the computer will have a 50% chance of winning and 50% chance of losing and 0% chance of tieing
        and the user will have a 50% chance of winning and 50% chance of losing and 0% chance of tieing
         also for feeling lucky mode the computer will have a 70% chance of winning and 30% chance of losing and 0% chance of tieing
         and the user will have a 70% chance of winning and 30% chance of winning and 0% chance of tieing
         with that the computer will have 5 points by d3fau1t """

        user_choice = input("enter your choice:")
        c_time = time()
        seed(c_time)
        c_choice = randint(1,3)
        if user_choice == '1':
            if c_choice == 1:
                print("computer chose rock")
                print("its a tie!")
                user_score -= 1
                comp_score -= 1
                print(f"your score: {user_score} and computer score: {comp_score}")

            elif c_choice == 2:
                print("computer chose paper")
                print("you lose!")
                comp_score += 1
                print(f"your score: {user_score} and computer score: {comp_score}")

            elif c_choice == 3:
                print("computer chose scissors")
                print("you win!")
                user_score += 1
                print(f"your score: {user_score} and computer score: {comp_score}")
            
        elif user_choice == '2':
            if c_choice == 1:
                print("computer chose rock")
                print("you win!")
                user_score += 1
                print(f"your score: {user_score} and computer score: {comp_score}")

            if c_choice == 2:
                print("computer chose paper")
                print("its a tie!")
                user_score -= 1
                comp_score -= 1
                print(f"your score: {user_score} and computer score: {comp_score}")
            
            if c_choice == 3:
                print("computer chose scissors")
                print("you lose!")
                comp_score += 1
                print(f"your score: {user_score} and computer score: {comp_score}")

        elif user_choice == '3':
            if c_choice == 1:
                print("computer chose rock")
                print("you lose!")
                comp_score += 1
                print(f"your score: {user_score} and computer score: {comp_score}")

            if c_choice ==2:
                print("computer chose paper")
                print("you win!")
                user_score += 1
                print(f"your score: {user_score} and computer score: {comp_score}")


            if c_choice == 3:
                print("computer chose scissors")
                print("its a tie!")
                user_score -= 1
                comp_score -= 1
                print(f"your score: {user_score} and computer score: {comp_score}")

        elif user_choice == '4':
            print("Returning to main menu...")
            break

        else:
            print("invalid choice. Please try again.")



            
