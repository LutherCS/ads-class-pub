'''
Testing the module movie_stats
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from movie_stats import MovieStats

# Change the file name to fit your system
FILENAME = 'movie_actors_small.txt'

class TestMovieStatsMethods(unittest.TestCase):
    '''Testing module movie_stats'''
    def setUp(self):
        '''Setting up'''
        self.stats = MovieStats(FILENAME)

    def test_get_cast(self):
        '''Test get_cast'''
        self.assertEqual(len(self.stats.get_cast('A Few Good Men')), 9)
        self.assertEqual(len(self.stats.get_cast('Godfather')), 13)
        self.assertEqual(len(self.stats.get_cast('The Shawshank Redemption')), 9)

    def test_get_titles_by_year(self):
        '''Test get_titles_by_year'''
        self.assertEqual(len(self.stats.get_titles_by_year(1992)), 1256)
        self.assertEqual(len(self.stats.get_titles_by_year(2017)), 262)
        self.assertEqual(len(self.stats.get_titles_by_year(1970)), 0)

    def test_get_titles_by_cast(self):
        '''Test get_titles_by_cast'''
        self.assertEqual(len(self.stats.get_titles_by_cast(20)), 416)
        self.assertEqual(len(self.stats.get_titles_by_cast(40)), 15)
        self.assertEqual(len(self.stats.get_titles_by_cast(80)), 2)

    def test_get_titles_by_actor(self):
        '''Test get_titles_by_actor'''
        self.assertEqual(len(self.stats.get_titles_by_actor('Kevin Bacon')), 34)
        self.assertEqual(len(self.stats.get_titles_by_actor('Tim Robbins')), 25)
        self.assertEqual(len(self.stats.get_titles_by_actor('Roman Yasinovskyy')), 0)

    def test_get_most_crowded_movie(self):
        '''Test get_most_crowded_movie'''
        self.assertEqual(self.stats.get_most_crowded_movie(), 'Monty Python Live (Mostly)')

    def test_get_most_prolific_year(self):
        '''Test get_most_prolific_year'''
        self.assertEqual(self.stats.get_most_prolific_year(), 2014)


if __name__ == '__main__':
    unittest.main(verbosity=2)
