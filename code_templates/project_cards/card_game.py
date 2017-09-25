'''Card, Deck, and Player'''

#!/usr/bin/env python3

import random

random.seed(160)

NAME = {'T': 'Ten', 'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}
RANK = '23456789TJQKA'
SUIT = ['spades', 'clubs', 'diamonds', 'hearts']


class Card:
    '''Card class'''
    def __init__(self, init_rank, init_suit):
        '''Constructor'''
        self._rank = init_rank
        self._suit = init_suit

    @property
    def rank(self):
        '''Get card rank'''
        return self._rank

    @property
    def suit(self):
        '''Get card suit'''
        return self._suit

    def __gt__(self, other):
        '''Card comparison: greater than'''
        # TODO: Task 1: Compare cards by rank only, ignoring the suit
        raise NotImplementedError

    def __str__(self):
        '''__str__ implementation'''
        # TODO: Task 2: Print a card
        raise NotImplementedError


class Deck:
    '''Deck of cards'''
    def __init__(self):
        '''Constructor'''
        self._cards = []
        for rank in RANK:
            for suit in SUIT:
                self._cards.append(Card(rank, suit))

    def __iter__(self):
        '''Deck iterator'''
        return iter(self._cards)

    def __str__(self):
        '''__str__ implementation'''
        # TODO: Task 3: Print every card in the deck
        raise NotImplementedError

    def is_empty(self):
        '''Check if the deck is empty'''
        return len(self._cards) == 0

    def draw(self):
        '''Draw a card from the deck'''
        # TODO: Task 4: Remove the last (top) card from the _card amd return it to the calling method
        raise NotImplementedError

    def shuffle(self):
        '''Shuffle the deck'''
        # TODO: Task 5: Use random.shuffle to shuffle _cards
        raise NotImplementedError


class Player:
    '''Player class'''
    def __init__(self, init_name, init_skill):
        '''Constructor'''
        self._name = init_name
        self._skill = init_skill
        self._hand = []
        self._played = []
        self._discard = []


    def __str__(self):
        '''__str__implementation'''
        return self._name + ' (lvl ' + str(self._skill) + ')'

    def is_empty_hand(self):
        '''Is the hand empty?'''
        return len(self._hand) == 0

    def is_empty_discard(self):
        '''Is the discard pile empty?'''
        return len(self._discard) == 0

    def is_empty_played(self):
        '''Is the active pile empty?'''
        return len(self._played) == 0

    def draw_card(self, deck):
        '''Draw one card from the deck'''
        # TODO: Task 6: Draw 1 card from the deck and put it in player's hand
        raise NotImplementedError

    def show_hand(self):
        '''Show (print) player's hand'''
        for card in self._hand:
            print(card)

    def play_card(self):
        '''Play a card'''
        # TODO: Task 7: Moves one (top) card from the player's hand to the playing pile and returns it
        raise NotImplementedError

    def discard_card(self, card):
        '''Discard a card to a pile'''
        self._discard.append(card)

    def pick_discard(self):
        '''Take a discard pile'''
        # TODO: Task 8: Shuffle the discard pile and moves all discarded cards to the player's hand
        raise NotImplementedError

    def discard_played(self):
        '''Take a pile'''
        # TODO: Task 9: Move all played cards to the player's discard pile 
        raise NotImplementedError

    def win_table(self, other):
        '''Win all cards on the table'''
        # TODO: Task 10: Grab all played cards on the table and put them into the player's discard pile
        raise NotImplementedError

    @property
    def name(self):
        '''Get name'''
        return self._name

    @property
    def skill(self):
        '''Get skills'''
        return self._skill

    @property
    def hand(self):
        '''Player's hand'''
        return self._hand

    @hand.setter
    def hand(self, new_value):
        '''Player's hand'''
        self._hand = new_value

    @property
    def played(self):
        '''Player's played cards'''
        return self._played

    @played.setter
    def played(self, new_value):
        '''Player's played cards'''
        self._played = new_value

    @property
    def discard(self):
        '''Player's discard pile'''
        return self._discard

    @discard.setter
    def discard(self, new_value):
        '''Player's discarded cards'''
        self._discard = new_value


def main():
    '''Main function'''
    print("Let's play a game!")
    print('Checking the cards')
    for _ in range(5):
        card1 = Card(random.choice(RANK), random.choice(SUIT))
        card2 = Card(random.choice(RANK), random.choice(SUIT))
        if card1 > card2:
            print('{} beats {}'.format(card1, card2))
        elif card2 > card1:
            print('{} is beaten by {}'.format(card1, card2))
        else:
            print('{} and {} are equal'.format(card1, card2))
    print('-----')
    print('Making a new deck')
    main_deck = Deck()
    print(main_deck)
    print('-----')
    print('Shuffling the deck')
    main_deck.shuffle()
    print(main_deck)
    print('-----')
    print('Creating the players')
    player1 = Player("Alice", random.randint(1, 10))
    print(player1)
    player2 = Player("Bob", random.randint(1, 10))
    print(player2)
    for _ in range(5):
        player1.draw_card(main_deck)
        player2.draw_card(main_deck)
    print('-----')
    print("{}'s hand:".format(player1.name))
    player1.show_hand()
    print('-----')
    print("{}'s hand:".format(player2.name))
    player2.show_hand()
    print('-----')
    print('{} is playing {}'.format(player1, player1.play_card()))
    print("{}'s hand:".format(player1.name))
    player1.show_hand()
    print('-----')
    print('{} is playing {}'.format(player2, player2.play_card()))
    print("{}'s hand:".format(player2.name))
    player2.show_hand()
    print('-----')
    print(player1)
    print('Hand empty: {}'.format(player1.is_empty_hand()))
    print('Active pile empty: {}'.format(player1.is_empty_played()))
    print('Discard pile empty: {}'.format(player1.is_empty_discard()))
    print('Picking the played pile')
    player1.discard_played()
    print('Hand empty: {}'.format(player1.is_empty_hand()))
    print('Active pile empty: {}'.format(player1.is_empty_played()))
    print('Discard pile empty: {}'.format(player1.is_empty_discard()))
    print('-----')
    print('{} is playing {}'.format(player1, player1.play_card()))
    print("{}'s hand:".format(player1.name))
    player1.show_hand()
    print('Bob is winning the round')
    player2.win_table(player1)
    print(player2)
    print('Hand empty: {}'.format(player2.is_empty_hand()))
    print('Active pile empty: {}'.format(player2.is_empty_played()))
    print('Discard pile empty: {}'.format(player2.is_empty_discard()))
    print('-----')
    print('{} picking up discard pile'.format(player2))
    player2.pick_discard()
    print("{}'s hand:".format(player2.name))
    player2.show_hand()

if __name__ == "__main__":
    main()
