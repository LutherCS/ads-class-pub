'''Implementation of the Map ADT as HashTable'''

class HashTable:
    def __init__(self, size_init: int=16):
        '''Constructor'''
        self._size = size_init
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key: int):
        '''__getitem__'''
        return self.get(key)

    def __setitem__(self, key: int, value):
        '''__setitem__'''
        self.put(key, value)
    
    def __len__(self):
        '''__len__'''
        raise NotImplementedError
    
    def __contains__(self, key):
        '''__contains__'''
        raise NotImplementedError

    def __str__(self):
        '''__str__'''
        raise NotImplementedError

    def _hash(self, key: int, size: int):
        '''Simple hash function'''
        return key % size

    def _rehash(self, old_hash: int, size: int, step: int=1):
        '''Simple or quadratic rehash'''
        raise NotImplementedError

    def put(self, key: int, value):
        '''Add or update an item'''
        raise NotImplementedError

    def get(self, key: int):
        '''Retrieve an item'''
        raise NotImplementedError

    def keys(self):
        '''Return all keys'''
        raise NotImplementedError

    def values(self):
        '''Return all values'''
        raise NotImplementedError

    def items(self):
        '''Return all items'''
        raise NotImplementedError
