	
#Debug the following code and point out errors that were corrected to make it run successfully.

import random # corrected spelling of random
import logging  # was not in the original code

# logging.disable(logging.CRITICAL)  # STOPS ALL ERRORS 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')  # was not in the original code

logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'): # corrected 'guessing' to 'guess' to match the declared variabled 'guess'
    logging.debug('Start of guess')  # was not in original code
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input().strip().lower() #added .strip().lower() to remove excess space and force to lower-case as a best-practice measure

logging.debug('Start of coin toss')  # was not in original code
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# we need to convert heads/tails to 0/1, or visa versa
if toss == 0:  #corrected order of if / else, replaced '=' with '==' so the comparison runs properly
    toss = 'tails'
else: # corrected else syntax, removed unneeded '= 1' condition from else since we're only working with two possibities. 
    toss = 'heads'

logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')  # not in original code

if toss == guess: # another instance of correcting '=' to '=='
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().strip().lower()#added .strip().lower() to remove excess space and force to lower-case as a best-practice measure 
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.') # removed stray 'Write your code here' comment
