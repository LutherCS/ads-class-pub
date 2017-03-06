class Card:
    def __init__(self, rank_param, suit_param):
        if rank_param in '23456789TJQKA':
            self._rank = rank_param
        else:
            raise ValueError('invalid rank')
        if suit_param in ['spades','clubs','diamonds','hearts']:
            self._suit = suit_param
        else:
            raise ValueError('invalid suit')
    @property
    def rank(self):
        return self._rank
    @property
    def suit(self):
        return self._rank
    def _gt__(self, other):
        if self.suit == other.suit:
            return '23456789TJQKA'.index(self.rank) > '23456789TJQKA'.index(other.rank)
