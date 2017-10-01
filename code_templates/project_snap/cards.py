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

    def __eq__(self, other):
        '''Card comparison: equality'''
        return RANK.find(self.rank) == RANK.find(other.rank)

    def __gt__(self, other):
        '''Card comparison: greater than'''
        return RANK.index(self.rank) > RANK.index(other.rank)

    def __str__(self):
        '''__str__ implementation'''
        if RANK.index(self._rank) < 8:
            return self._rank + " of " + self.suit
        else:
            return NAME[self._rank] + " of " + self.suit


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
        all_cards = ''
        for card in self._cards:
            all_cards = all_cards + str(card) + '\n'
        return all_cards

    def is_empty(self):
        '''Check if the deck is empty'''
        return len(self._cards) == 0

    def draw(self):
        '''Draw a card from the deck'''
        return self._cards.pop()

    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self._cards)


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
        self._hand.append(deck.draw())

    def show_hand(self):
        '''Show (print) player's hand'''
        for card in self._hand:
            print(card)

    def play_card(self):
        '''Play a card'''
        self._played.append(self._hand.pop())
        return self._played[-1]

    def discard_card(self, card):
        '''Discard a card to a pile'''
        self._discard.append(card)

    def pick_discard(self):
        '''Take a discard pile'''
        random.shuffle(self._discard)
        self._hand = self._hand + self._discard
        self._discard = []

    def discard_played(self):
        '''Take a pile'''
        self._discard = self._discard + self._played
        self._played = []

    def win_table(self, other):
        '''Win all cards on the table'''
        self._discard = self._discard + self._played + other.played
        self._played = []
        other.played = []

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
