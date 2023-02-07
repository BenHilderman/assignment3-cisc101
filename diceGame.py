"""
This program is a dice game, it initially rolls two dice. 
If one of the dice is a 3, the game ends. 
If the dice are doubles, it keeps rolling until the dice aren't doubles. 
If the sum of the dice is 7, it re-rolls 10 times. 
If the sum of the dice is even, the dice get re-rolled 4  times.
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Sept 25, 2022
"""
import random

# setting initial variables
rolls = 1
play = 'y'
points = 0

# introduction
print('Welcome to the very fun dice game.')

while play == 'y' or play == 'Y':
    # generating random int for the dice
    die1 = random.randint(1, 6)
    initialDie1 = die1
    die2 = random.randint(1, 6)
    initialDie2 = die2
    evenRolls = 0
    print('You have rolled', die1, die2)
    
    # checks if die1 or die2 is a 3 before continuing the game
    if initialDie1 == 3 or initialDie2 == 3:
        print('You rolled a three...')
        points += die1 + die2
        points += 3
        play = 'n'

    else:
        # doubles
        while initialDie1 == initialDie2: 
            print('You rolled doubles')
            initialDie2 = random.randint(1, 6)
            rolls += 1
            print('Dice re-rolled are:', die1, initialDie2)
            points = die1 + die2 + rolls
        
        # calculate initial sum (to check for sum of 7 and even sum)
        initialSum = initialDie1 + initialDie2

        # sum of 7
        if initialSum == 7:
            print('The sum of ' +str(initialDie1) + ' ' + str(initialDie2) + ' is 7 so rolling the dice 10 times')
            for magicRolls in range(10):
                magicRolls += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                print('Dice currently are:', die1, die2)
                points = points + die1 + die2
        # sum is even
        if initialSum % 2 == 0:
            print('The sum of ' +str(initialDie1) + ' ' + str(initialDie2) + ' is even so rolling dice 4 times')
            for evenRolls in range(4):
                evenRolls += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                print('Dice currently are:', die1, die2)
                points = points + die1 + die2
        # just adding the two dice together if the initialdie dont fall under any of the categories
        if initialSum % 2 != 0 and initialSum != 7 and initialDie1 != initialDie2:
             points += initialDie1 + initialDie2
        # displaying current points
        print('You have ' + str(points) + ' points')

        # ask user if they want to play again
        play = input('Do you wish to continue to play the game and get more points? (Enter Y/y to continue or any other character to end): ')

# displays final score when game ends
print('Your final score is ' + str(points) + '. Hope you had fun playing this amazing dice game!')
