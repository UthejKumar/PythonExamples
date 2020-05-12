''' "Number Guessing Game" ~ by Uthej Kumar 
    It provides the user with a number of guesses to guess 
    a number that is randomly picked by the computer.
 '''

'''DISCLAIMER/WARNING'''
''' If you want to change the number of chances or
    the range in which the computer selects the number, I have mentioned 
    "#Change" at the lines where it needs to be configured.'''

import random


#Function that asks user to guess a number within the given range.
def game():
    guess_num = random.randint(1,40)    #Computer selects random number within this range.
    print("\nGuess a number between 1 to 40.")
    print("You have 5 chances.")    #Change

    for count in range(1,6):    #Change
        count += 0
        user_guess = int(input(">"))
        if user_guess > guess_num:
            if count < 5:   #Change
                print("Try guessing lower.")
                print("You have %d chances left" % (5 - count)) #Change
            else:
                print("\nYou have exceeded the number of guesses. Sorry!")
                print("The correct guess was %d." % guess_num)
        elif user_guess < guess_num:
            if count < 5:   #Change
                print("Try guessing higher.")
                print("You have %d chances left" % (5 - count)) #Change
            else:
                print("You have exceeded the number of guesses. Sorry!")
                print("The correct guess was %d." % guess_num)
        elif user_guess == guess_num:
            print("Bullseye, that is correct!")
            print("It took you %d chance(s) to guess the number" % count)
            break
    
    repeat()


#Function that asks the user if they want to play again.
def repeat():
    print("\nDo you want to play again Y/N?")
    play = input(">")
    if play == "Y" or play == "y":
        game()
    else:
        print("\nOkay, bye then!\n")
        exit()


game()
