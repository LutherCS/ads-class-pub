#!/usr/bin/env python3
"""
`water` testing

@authors: Roman Yasinovskyy, Karina Hoff
@version: 2021.3
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
    from src.projects.water import State, search


@pytest.mark.parametrize("jug_1, jug_2", [(1, 2), (2, 0)])
def test_State_init(jug_1, jug_2):
    """Testing State.__init__"""
    state = State(jug_1, jug_2)
    assert isinstance(state, State)
    assert state is not None


def test_State_init_empty_error():
    """Testing State.__init__ error"""
    with pytest.raises(TypeError) as excinfo:
        state = State()  # pylint: disable=no-value-for-parameter, unused-variable
    exception_message = excinfo.value.args[0]
    assert (
        exception_message
        == "__init__() missing 2 required positional arguments: 'jug_1' and 'jug_2'"
    )


def test_State_init_type_error():
    """Testing State.__init__ error"""
    with pytest.raises(TypeError) as excinfo:
        state = State(1.0, 2.0)
    exception_message = excinfo.value.args[0]
    assert (
        exception_message == "__init__() should return None, not 'NotImplementedType'"
    )


@pytest.mark.parametrize("jug_1, jug_2, issue_jug", [(6, 0, 1), (0, 4, 2)])
def test_State_init_value_error(jug_1, jug_2, issue_jug):
    """Testing State.__init__ error"""
    with pytest.raises(ValueError) as excinfo:
        state = State(jug_1, jug_2)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"The proposed value exceeds jug {issue_jug} capacity"


@pytest.mark.parametrize("jug_1, jug_2", [(1, 2), (2, 0)])
def test_state_eq(jug_1, jug_2):
    """Testing State.__eq__"""
    state_1 = State(jug_1, jug_2)
    state_2 = State(jug_1, jug_2)
    assert state_1 == state_2
    assert state_1 is not state_2


@pytest.mark.parametrize("jug_1, jug_2, expected", [(1, 2, "(1, 2)"), (2, 0, "(2, 0)")])
def test_state_str(jug_1, jug_2, expected):
    """Testing State.__str__"""
    state = State(jug_1, jug_2)
    assert str(state) == expected


@pytest.mark.parametrize("jug_1, jug_2", [(1, 2), (2, 0)])
def test_state_clone(jug_1, jug_2):
    """Testing State.__clone__"""
    state_1 = State(jug_1, jug_2)
    state_2 = state_1.clone()
    assert state_1 == state_2
    assert state_1 is not state_2


@pytest.mark.parametrize("jug_1, jug_2, expected", [(1, 2, "(5, 2)"), (5, 3, "(5, 3)")])
def test_state_fill_jug_1(jug_1, jug_2, expected):
    """Testing State.fill_jug_1"""
    state = State(jug_1, jug_2)
    state.fill_jug_1()
    assert str(state) == expected


@pytest.mark.parametrize("jug_1, jug_2, expected", [(1, 2, "(1, 3)"), (5, 3, "(5, 3)")])
def test_state_fill_jug_2(jug_1, jug_2, expected):
    """Testing State.fill_jug_2"""
    state = State(jug_1, jug_2)
    state.fill_jug_2()
    assert str(state) == expected


@pytest.mark.parametrize("jug_1, jug_2, expected", [(1, 2, "(0, 2)"), (0, 3, "(0, 3)")])
def test_state_empty_jug_1(jug_1, jug_2, expected):
    """Testing State.empty_jug_1"""
    state = State(jug_1, jug_2)
    state.empty_jug_1()
    assert str(state) == expected


@pytest.mark.parametrize("jug_1, jug_2, expected", [(1, 2, "(1, 0)"), (5, 0, "(5, 0)")])
def test_state_empty_jug_2(jug_1, jug_2, expected):
    """Testing State.empty_jug_2"""
    state = State(jug_1, jug_2)
    state.empty_jug_2()
    assert str(state) == expected


@pytest.mark.parametrize(
    "jug_1, jug_2, expected",
    [
        (0, 1, "(0, 1)"),
        (1, 1, "(0, 2)"),
        (2, 2, "(1, 3)"),
        (5, 0, "(2, 3)"),
        (5, 2, "(4, 3)"),
        (5, 3, "(5, 3)"),
    ],
)
def test_state_pour_jug_1_to_jug_2(jug_1, jug_2, expected):
    """Testing State.pour_jug_1_to_jug_2"""
    state = State(jug_1, jug_2)
    state.pour_jug_1_to_jug_2()
    assert str(state) == expected


@pytest.mark.parametrize(
    "jug_1, jug_2, expected",
    [
        (1, 0, "(1, 0)"),
        (1, 1, "(2, 0)"),
        (4, 2, "(5, 1)"),
        (0, 3, "(3, 0)"),
        (4, 3, "(5, 2)"),
        (5, 3, "(5, 3)"),
    ],
)
def test_state_pour_jug_2_to_jug_1(jug_1, jug_2, expected):
    """Testing State.pour_jug_2_to_jug_1"""
    state = State(jug_1, jug_2)
    state.pour_jug_2_to_jug_1()
    assert str(state) == expected


@pytest.mark.parametrize(
    "jug_1_start, jug_2_start, jug_1_goal, jug_2_goal",
    [
        (0, 0, 4, 0),
        (0, 1, 4, 0),
        (0, 2, 4, 0),
        (0, 3, 4, 0),
        (1, 0, 4, 0),
        (1, 1, 4, 0),
        (1, 2, 4, 0),
        (1, 3, 4, 0),
        (2, 0, 4, 0),
        (2, 1, 4, 0),
        (2, 2, 4, 0),
        (2, 3, 4, 0),
        (3, 0, 4, 0),
        (3, 1, 4, 0),
        (3, 2, 4, 0),
        (3, 3, 4, 0),
        (4, 0, 4, 0),
        (4, 1, 4, 0),
        (4, 2, 4, 0),
        (4, 3, 4, 0),
        (5, 0, 4, 0),
        (5, 1, 4, 0),
        (5, 2, 4, 0),
        (5, 3, 4, 0),
    ],
)
def test_search_default(jug_1_start, jug_2_start, jug_1_goal, jug_2_goal):
    """Testing search to (4, 0)"""
    result = []
    search(State(jug_1_start, jug_2_start), State(jug_1_goal, jug_2_goal), result)
    assert result[0] == State(jug_1_start, jug_2_start)
    assert result[-1] == State(jug_1_goal, jug_2_goal), print(result)


@pytest.mark.parametrize(
    "jug_1_start, jug_2_start, jug_1_goal, jug_2_goal",
    [
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (0, 0, 0, 2),
        (0, 0, 2, 0),
        (0, 0, 3, 0),
        (0, 0, 0, 3),
        (0, 0, 4, 0),
        (0, 0, 5, 0),
    ],
)
def test_search_simple(jug_1_start, jug_2_start, jug_1_goal, jug_2_goal):
    """Testing search from (0, 0)"""
    result = []
    search(State(jug_1_start, jug_2_start), State(jug_1_goal, jug_2_goal), result)
    assert result[0] == State(jug_1_start, jug_2_start)
    assert result[-1] == State(jug_1_goal, jug_2_goal), print(result)


@pytest.mark.parametrize(
    "jug_1_start, jug_2_start, jug_1_goal, jug_2_goal",
    [
        (1, 1, 1, 0),
        (1, 1, 0, 1),
        (2, 2, 0, 2),
        (2, 2, 2, 0),
        (3, 3, 3, 0),
        (3, 3, 0, 3),
        (4, 3, 4, 0),
        (5, 3, 5, 0),
    ],
)
def test_search_advanced(jug_1_start, jug_2_start, jug_1_goal, jug_2_goal):
    """Testing search between various states"""
    result = []
    search(State(jug_1_start, jug_2_start), State(jug_1_goal, jug_2_goal), result)
    assert result[0] == State(jug_1_start, jug_2_start)
    assert result[-1] == State(jug_1_goal, jug_2_goal), print(result)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
