#!/usr/bin/env python3
"""
`keyboard` testing

@authors: Roman Yasinovskyy
@version: 2021.9
"""

import pathlib
import pytest

from keyboard import spell_check

TIME_LIMIT = 4

FILENAMES = (
    "sample",
    "all_firsthalf",
    "all_secondhalf",
    "gen26",
    "gen50",
    "gen100",
    "gen1000",
    "gen2500",
    "gen5000",
    "gen10000",
)


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize("filename", FILENAMES)
def test_output(filename, capsys):
    """Testing the output"""
    if not pathlib.Path(f"{filename}.in.txt").exists():
        filename = f"projects/keyboard/{filename}"
    data_in = f"{filename}.in.txt"
    spell_check(data_in)
    out, err = capsys.readouterr()
    with open(f"{filename}.out.txt") as file_out:
        expected_output = file_out.read()
    assert expected_output == out
    assert not err


if __name__ == "__main__":
    pytest.main(["-v", __file__])
