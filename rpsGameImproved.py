# more efficient Rock Paper Scissors game

import random, sys

print('ROCK, PAPER, SCISSORS - A  Game by Ryan Duggan')

wins = 0
losses = 0
ties = 0

moves = ['r', 'p', 's']
names = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}

while True:  # main game loop
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    # Player input loop
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        player_move = input('>').lower()
        if player_move == 'q':
            sys.exit()
        if player_move in moves:
            break
        print('Type one of r, p, s, or, q.')

    # show choices
    print(names[player_move], "versus...")

    computer_move = random.choice(moves)
    print(names[computer_move])

    # determin outcome

    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
        (player_move == 'p' and computer_move == 'r') or \
        (player_move == 's' and computer_move == 'p'):
        print("You win!")
        wins += 1
    else:
        print("You lose!")

        losses += 1
