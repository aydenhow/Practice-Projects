# scissors_paper_rock.py #
# Scissors, paper, rock game that runs multiple rounds until user exits.

from random import randint
from time import sleep

options = ['Scissors', 'Paper', 'Rock']

def welcome():
    print("Welcome!")
    sleep(1)
    print("Please answer S for Scissors, P for Paper or R for Rock.")

def play():
    start = True
    scores = {'Player': 0, 'Opponent': 0}
    while start is True:
        player = input("Scissors, Paper or Rock?: ")
        player = player.upper()
        opponent = options[randint(0, 2)]
        if player == 'S':
            player = 'Scissors'
        elif player == 'P':
            player = 'Paper'
        elif player == 'R':
            player = 'Rock'
        else:
            print("Opps! Please enter S, P or R.")
            continue
        sleep(0.5)
        print('Player: ' + player)
        sleep(0.5)
        print("Computer: " + opponent)
        sleep(1)
        if player == opponent:
            print("Draw! Pick again.\n")
            continue
        elif (player == 'Scissors' and opponent == 'Paper') or (player == 'Paper' and opponent == 'Rock') or (player == 'Rock' and opponent == 'Scissors'):
            print("You win this round!\n")
            scores['Player'] += 1
        else:
            print("You lose this round!\n")
            scores['Opponent'] += 1
        again = input("Play again? (Y or N): ").upper()
        if again == 'N':
            start = False
            print("Final scores:")
            sleep(0.5)
            print('Player: ' + str(scores["Player"]))
            sleep(0.5)
            print('Opponent: ' + str(scores['Opponent']))
            sleep(1)
            if scores['Player'] > scores['Opponent']:
                print("Congratulations! You win.")
            elif scores['Player'] < scores['Opponent']:
                print("Oh no! Your opponent won.")
            else:
                print("It's a draw, everyone wins!")

welcome()
play()

