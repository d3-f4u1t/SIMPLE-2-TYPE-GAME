'''
this game is about dice roll game 
where the user rolls a dice and then the computer rolls a dice and the one with the highest numbers wins
also adding a system that adds score
 '''

from random import randint, seed
import time

def g2():
    print("welcome to the game of dice roll!")
    print("you will be playing aginst the computer")

    while True:
        user_score = 0
        comp_score = 0

        input("press enter to roll the dice")
        c_time = time.time()
        seed(c_time)
        user_dice = randint(1,6)
        
        print(f"you rolled a {user_dice}")
        time.sleep(1)#will pause the code for one sec

        computer_dice = randint(1,6)
        print(f"the computer rolled a {computer_dice}")
        time.sleep(1)

        if user_dice > computer_dice:
            print("comgratulations you win!")
            user_score += 1
            print(f"your score: {user_score} and computer score: {comp_score}")

        elif user_dice < computer_dice:
            print("sorry you lose!")
            comp_score += 1
            print(f"your score: {user_score} and computer score: {comp_score}")



        else:
            print("it's a tie!")
            user_score -= 1
            comp_score -= 1
            print(f"your score: {user_score} and computer score: {comp_score}")

        play_again = input("do you want to play again? (y/n)")

        if play_again.lower() == 'y':
            continue
        else:
            print("thanks for playing!")
            break

