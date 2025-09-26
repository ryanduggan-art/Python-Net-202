# Write your code here :-)
# Rock, Paper, Scissors, Lizard, Spock Game

import random, sys

print('ROCK, PAPER, SCISSORS, LIZARD, SPOCK - A  Game by Sheldon Cooper')

wins = 0
losses = 0
ties = 0

moves = ['r', 'p', 's', 'l', 'sp']
names = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS', 'l': 'LIZARD', 'sp': 'SPOCK'}

# rules: each move beats the list of moves
rules = {
    'r': ['s', 'l'], # rock crushes scissors and lizard
    'p': ['r', 'sp'], # paper covers rock and disproves spock
    's': ['p', 'l'], # scissors cuts paper and decapitates lizard
    'l': ['sp', 'p'], # lizard poisons spock and eats paper]
    'sp': ['s', 'r'], # spock smashes scissors and vaporizes rock
}

while True:  # main game loop
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    # Player input loop
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, (l)izard, (sp)ock or (q)uit')
        player_move = input('>').lower()
        if player_move == 'q':
            sys.exit()
        if player_move in moves:
            break
        print('Type one of r, p, s, l, sp, or, q.')

    # show choices
    print(f"{names[player_move]}, versus...")
    computer_move = random.choice(moves)
    print(names[computer_move])

    # determin outcome

    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif computer_move in rules[player_move]:
        print('You win!')
        wins += 1
    else:
        print("You lose!")
        losses += 1
