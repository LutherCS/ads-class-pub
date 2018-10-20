'''
Testing the hashing methods
Roman Yasinovskyy, 2018
'''
#!/usr/bin/python3


import pytest
from exercises.hashing.hashing import hash_remainder
from exercises.hashing.hashing import hash_mid_sqr
from exercises.hashing.hashing import hash_folding
from exercises.hashing.hashing import hash_str
from exercises.hashing.hashing import hash_str_weighted


class Testhashing:
    '''Testing module hashing'''
    @classmethod
    def setup_class(self):
        self.keys_int = [10, 21, 32, 18, 17, 19, 42, 23, 99]
        self.keys_int_2 = [54, 26, 93, 17, 77, 31]
        self.keys_intstr = ['563-555-1234', '800-555-8080', '888-555-0000']
        self.keys_intstr_2 = ['436-555-4601']
        self.keys_str = ['pavel', 'bruce', 'talia', 'harvey', 'jim', 'alfred', 'lucius', 'jonathan', 'bane']
        self.keys_str_2 = ['algorithm', 'logarithm']

    def test_hash_remainder(self):
        result = [hash_remainder(x, 16) for x in self.keys_int]
        result_2 = [hash_remainder(x, 11) for x in self.keys_int_2]
        assert result == [10, 5, 0, 2, 1, 3, 10, 7, 3]
        assert result_2 == [10, 4, 5, 6, 0, 9]

    def test_hash_hash_mid_sqr(self):
        result = [hash_mid_sqr(x, 16) for x in self.keys_int]
        result_2 = [hash_mid_sqr(x, 11) for x in self.keys_int_2]
        assert result == [10, 12, 2, 0, 12, 4, 12, 4, 0]
        assert result_2 == [3, 1, 9, 6, 4, 8]

    def test_hash_folding(self):
        result = [hash_folding(x, 16) for x in self.keys_intstr]
        assert result == [0, 12, 4]
        result2 = [hash_folding(x, 11) for x in self.keys_intstr_2]
        assert result2 == [1]

    def test_hash_str(self):
        result = [hash_str(x, 16) for x in self.keys_str]
        assert result == [8, 1, 11, 15, 0, 14, 5, 3, 6]
        result = [hash_str(x, 11) for x in self.keys_str_2]
        assert result == [10, 10]

    def test_hash_str_weighted(self):
        result = [hash_str_weighted(x, 16) for x in self.keys_str]
        assert result == [12, 9, 8, 8, 3, 6, 9, 14, 12]
        result = [hash_str_weighted(x, 11) for x in self.keys_str_2]
        assert result == [8, 2]


if __name__ == '__main__':
    pytest.main(['test_hashing.py'])
