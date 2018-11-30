'''
Testing the module movies
Karina Hoff, 2018
'''

#!/usr/bin/python3

import pytest
from projects.kevinbacon.kevinbacon import read_file, find_max_kbn_actors, main


class TestMoviesMethods:
    '''Testing module movies'''

    @classmethod
    def setup_class(cls):
        '''Setting up'''
        cls.graph = read_file(sys.path[0] + "/projects/moviestat/movie_actors_small.txt")
        kevin = cls.graph.get_vertex("Kevin Bacon")
        cls.graph.bfs(kevin)        
        
    def test_read_file(self):
        assert len(self.graph) == 216251
        connections = 0
        for v in self.graph:
            connections += len(v.get_neighbors())
        assert connections == 3162842
        
    def test_find_max_kbn_actors(self):
        assert self.graph != None
        expected_lst = ["Jason Wyssman",
                        "Joe Maccarthey",
                        "Jordan (V) Hale",
                        "Robert G. Heron",
                        "Jordin Billington",
                        "Tom (IV) O'Rourke",
                        "Philip Davies",
                        "Darren Shields" ]
        lst = find_max_kbn_actors(self.graph)
        for actor in expected_lst:
            assert actor in lst

    def test_main(self, capsys, monkeypatch):
        # check functionality of input
        expected_output1 = "1) Julie Andrews acted with Colin Firth in Relative Values (2000)\n" + \
                        "2) Colin Firth acted with Kevin Bacon in Where the Truth Lies (2005)\n" + \
                        "\n" + \
                        "Julie Andrews's Kevin Bacon number is 2\n"
        # path can vary; just check number here
        expected_output2 = "Chris Bannow's Kevin Bacon number is 4\n"
        # try one or more inputs
        inputs = ['Julie Andrews', 'Chris Bannow', '']
        input_gen = (actor for actor in inputs)
        monkeypatch.setattr('builtins.input', lambda prompt: next(input_gen))
        main()
        out, err = capsys.readouterr()
        assert expected_output1 in out
        assert expected_output2 in out


if __name__ == '__main__':
    pytest.main(['test_kbmovies.py'])
