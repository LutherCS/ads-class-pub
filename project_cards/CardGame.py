'''Cards classes'''

NAMES = {'T': 'Ten', 'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}
RANK = '23456789TJQKA'
SUIT = ['spades', 'clubs', 'diamonds', 'hearts']

class Card:
    '''Card class'''
    def __init__(self, rank_param, suit_param):
        if rank_param in '23456789TJQKA':
            self._rank = rank_param
        else:
            raise ValueError('invalid rank')
        if suit_param in ['spades', 'clubs', 'diamonds', 'hearts']:
            self._suit = suit_param
        else:
            raise ValueError('invalid suit')
    @property
    def rank(self):
        '''return card's rank'''
        return self._rank
    @property
    def suit(self):
        '''return card's suit'''
        return self._suit
    def _gt__(self, other):
        '''comparing cards of the same suit'''
        if self.suit == other.suit:
            return '23456789TJQKA'.index(self.rank) > '23456789TJQKA'.index(other.rank)
    def __str__(self):
        '''return card as a string'''
        return NAMES.get(self.rank, self.rank) + " of " + self.suit


class Deck:
    '''Deck class'''
    def __init__(self):
        self._card_list = []
        for s in SUIT:
            for r in RANK:
                self._card_list.append(Card(r, s))


class Player:
    '''Player class'''
    def __init__(self, name_param, hand_size_param):
        pass
