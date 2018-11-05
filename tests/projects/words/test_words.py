'''
Testing the module words
Karina Hoff, 2018
'''

#!/usr/bin/python3

"""Testing the Word Ladder project"""
import pytest
from projects.words.words import Stack, Queue, read_file, distance, diff_by_one_all


class TestWordsMethods:
    '''Testing module words'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        pass
        
    def test_read_file(self):
        '''Test read_file functino'''
        assert read_file("data/projects/words/words.txt") == {3: 1294, 4: 4994, 5: 5757}
    
    def test_distance(self):
        '''Test distance function'''
        w1 = 'Hello'
        w2 = 'Hello'
        assert distance(w1, w2) == 0
        w1 = 'Hello'
        w2 = 'Jello'
        assert distance(w1, w2) == 1
        w1 = 'Hello'
        w2 = 'Happy'
        assert distance(w1, w2) == 4
    
    def test_diff_by_one_all(self):
        '''Testing diff_by_one_all function'''
        #no used words
        word = 'Hello'
        all_words = ['Jello', 'Happy']
        used_words = []
        assert diff_by_one_all(word, all_words, used_words) == ['Jello']
        #used words
        word = 'Hello'
        all_words = ['Jello', 'Happy']
        used_words = ['Jello']
        assert diff_by_one_all(word, all_words, used_words) == []
        

if __name__ == '__main__':
    pytest.main(['test_words.py'])
