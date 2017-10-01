'''Snap! game implementation'''

#!/usr/bin/env python3

import random
from cards import Card, Deck, Player
random.seed(42)


def play_game(player1, player2):
    '''Game main loop'''
    pass

def main():
    '''Main function'''
    player1 = Player("Alice", 5)
    player2 = Player("Bob", 5)
    print('{} ({}) and {} ({}) are going to play 100 games!'.format(player1.name, player1.skill, player2.name, player2.skill))
    print('{:^10}{:^10}{:^10}'.format('Game', 'Winner', 'Rounds'))

if __name__ == "__main__":
    main()
