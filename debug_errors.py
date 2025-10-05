	
#Debug the following code and point out errors that were corrected to make it run successfully.

import random
import logging  # was not in the original code

# logging.disable(logging.CRITICAL)  # STOPS ALL ERRORS

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')  # was not in the original code

logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of guess')  # was not in original code
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input().lower()

logging.debug('Start of coin toss')  # was not in original code
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# we need to convert heads/tails to 0/1, or visa versa
if toss == 0:
    toss = "tails'"
else:
    toss == 1
    toss = 'heads'

logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')  # not in original code

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
