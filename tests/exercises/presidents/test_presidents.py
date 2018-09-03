'''
Testing the module presidents
Karina Hoff, 2018
'''
#!/usr/bin/python3


import pytest
from exercises.presidents.presidents import get_most_alive_year
from exercises.presidents.presidents import get_most_alive_all_years
from exercises.presidents.presidents import get_number_of_presidents_alive
from exercises.presidents.presidents import get_names_of_presidents_alive
from exercises.presidents.presidents import print_all_names


class TestMethods:
    '''Testing module '''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(cls):
        '''Setting up'''
        cls.d = {
            1: ['Alice Aardvark'],
            2: ['Alice Aardvark', 'Charles (Chuck) Cheetah'],
            3: ['Alice Aardvark', 'Charles (Chuck) Cheetah', 'Bob B. Beaver'],
            4: ['Charles (Chuck) Cheetah']
        }

    def test_get_number_of_presidents_alive(cls):
        assert get_number_of_presidents_alive(cls.d, 1) == 1
        assert get_number_of_presidents_alive(cls.d, 2) == 2
        assert get_number_of_presidents_alive(cls.d, 3) == 3
        assert get_number_of_presidents_alive(cls.d, 4) == 1

    def test_get_names_of_presidents_alive(cls):
        assert get_names_of_presidents_alive(cls.d, 1) == ['Alice Aardvark']
        assert get_names_of_presidents_alive(cls.d, 2) == ['Alice Aardvark', 'Charles (Chuck) Cheetah']
        assert get_names_of_presidents_alive(cls.d, 3) == ['Alice Aardvark', 'Bob B. Beaver', 'Charles (Chuck) Cheetah']
        assert get_names_of_presidents_alive(cls.d, 4) == ['Charles (Chuck) Cheetah']

    def test_get_most_alive_year(cls):
        assert get_most_alive_year(cls.d) == 3

    def test_get_most_alive_all_years(cls):
        assert get_most_alive_all_years(cls.d) == [3]

    def test_print_all_names(cls, capsys):
        expected_output = "Alice Aardvark\n" + \
                          "Bob B. Beaver\n" + \
                          "Charles (Chuck) Cheetah\n"
        print_all_names(cls.d, 3)
        out, err = capsys.readouterr()
        assert expected_output in out


if __name__ == '__main__':
    pytest.main(['test_presidents.py'])
