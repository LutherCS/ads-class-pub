'''
Testing the project Touchscreen Keyboard
Roman YAsinovskyy, 2018
'''

#!/usr/bin/python3

import pytest
import time
from projects.keyboard import spell_check

class TestTouchscreenKeyboardMethods:
    '''Testing the project Touchscreen Keyboard'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        pass
        
    def test_sample_output(self, capsys):
        filename = 'sample'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_sample_time(self, capsys):
        filename = 'sample'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_firsthalf_output(self, capsys):
        filename = 'all_firsthalf'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_firsthalf_time(self, capsys):
        filename = 'all_firsthalf'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_secondhalf_output(self, capsys):
        filename = 'all_secondhalf'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_secondhalf_time(self, capsys):
        filename = 'all_firsthalf'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_gen26_output(self, capsys):
        filename = 'gen26'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_gen26_time(self, capsys):
        filename = 'gen26'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_gen50_output(self, capsys):
        filename = 'gen50'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_gen50_time(self, capsys):
        filename = 'gen50'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_gen100_output(self, capsys):
        filename = 'gen100'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_gen100_time(self, capsys):
        filename = 'gen100'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_gen1000_output(self, capsys):
        filename = 'gen1000'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_gen1000_time(self, capsys):
        filename = 'gen1000'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_gen2500_output(self, capsys):
        filename = 'gen2500'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_gen2500_time(self, capsys):
        filename = 'gen2500'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_gen5000_output(self, capsys):
        filename = 'gen5000'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_gen5000_time(self, capsys):
        filename = 'gen5000'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

    def test_gen10000_output(self, capsys):
        filename = 'gen10000'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        spell_check(data_in)
        out, err = capsys.readouterr()
        with open('tests/projects/keyboard/{}.out'.format(filename)) as file_out:
            expected_output = ''.join(file_out.readlines())
        assert expected_output == out

    def test_gen10000_time(self, capsys):
        filename = 'gen10000'
        data_in = 'data/projects/keyboard/{}.in'.format(filename)
        start = time.time()
        spell_check(data_in)
        out, err = capsys.readouterr()
        stop = time.time()
        elapsed = stop - start
        assert elapsed < 2

if __name__ == '__main__':
    pytest.main(['test_keyboard.py'])
