# number_guess.py #
# Guess the number game by simulating two rolls of dice. 

from random import randint
from time import sleep

def get_user_guess():
    guess = int(input('Guess the number: '))
    return guess

def roll_dice(num_of_sides):
    first_roll = randint(1, num_of_sides)
    second_roll = randint(1, num_of_sides)
    max_val = 2 * num_of_sides
    print('The maximum possible number is: %d' % max_val)
    guess = get_user_guess()
    if guess > max_val:
        print('That guess is higher than the maximum possible!')
    else:
        print('Rolling...')
        sleep(2)
        print('The first roll is %d' % first_roll)
        sleep(1)
        print('The second roll is %d' % second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print('Result...')
        sleep(1)
        print('The total value is %d' % total_roll)
        if guess == total_roll:
            print('You were correct!')
        else:
            print('Uh-oh! The computer beat you.')


sides = int(input('How many sides? '))
roll_dice(sides)
