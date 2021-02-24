#!/usr/bin/env python3
"""
`keyboard` testing

@authors: Roman Yasinovskyy
@version: 2021.2
"""

import importlib
import pathlib
import sys

import pytest

try:
    importlib.util.find_spec(".".join(pathlib.Path(__file__).parts[-3:-1]), "src")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[3]}/")
finally:
    from src.projects.keyboard import spell_check

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
    data_in = f"data/projects/keyboard/{filename}.in"
    spell_check(data_in)
    out, err = capsys.readouterr()
    with open(f"tests/projects/keyboard/{filename}.out") as file_out:
        expected_output = file_out.read()
    assert expected_output == out
    assert not err


if __name__ == "__main__":
    pytest.main(["-v", __file__])
