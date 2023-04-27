import random
import art
from data import data
import os


score = 0
game_continue = True
contestant_b = random.choice(data)
print(art.logo)

while game_continue:

    #generate random contestants
    contestant_a = contestant_b
    contestant_b = random.choice(data)

    if contestant_a == contestant_b:
        contestant_b = random.choice(data)

    print('Contestant A:', contestant_a['name'], ',', contestant_a['description'], 'from', contestant_a['country'])
    print(art.vs)
    print('Contestant B: ', contestant_b['name'], ',', contestant_b['description'], 'from', contestant_b['country'])

    print()

    # user input
    guess = input("Which has more followers, A or B?\n").lower()

    # checking answer
    if contestant_a['follower_count'] > contestant_b['follower_count']:
        if guess == 'a':
            os.system('clear')
            print(art.logo)
            print('Correct!')
            score += 1
            print("Your score is: ", score)
        elif guess == 'b':
            print('Incorrect!')
            print('Your final score is: ', score)
            game_continue = False
    elif contestant_a['follower_count'] < contestant_b['follower_count']:
        if guess == 'b':
            os.system('clear')
            print(art.logo)
            print('Correct!')
            score += 1
            print("Your score is: ", score)
        elif guess == 'a':
            print('Incorrect!')
            print('Your final score is: ', score)
            game_continue = False


