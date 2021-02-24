#!/usr/bin/env python3
"""
`stacks` testing

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
    from src.exercises.stacks import (
        StackError,
        TokenError,
        base_converter,
        par_checker,
        par_checker_ext,
        par_checker_file,
        rev_string,
        rpn_calc,
    )


@pytest.mark.parametrize(
    "string, expected", [("abxaby", "ybaxba"), ("y", "y"), ("aaa", "aaa"), ("", "")]
)
def test_rev_string(string, expected):
    """Testing rev_string method"""
    assert rev_string(string) == expected


@pytest.mark.skip("Textbook implementation")
@pytest.mark.parametrize(
    "string, expected",
    [("((()))", True), ("(()", False), ("()(())", True), ("))((", False)],
)
def test_par_checker(string, expected):
    """Testing par_checker method"""
    assert par_checker(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [("{{([][])}()}", True), ("[{()]", False), ("([{}<>][])", True), (")][(", False)],
)
def test_par_checker_ext(string, expected):
    """Testing par_checker_ext method"""
    assert par_checker_ext(string) == expected


def test_par_checker_file(capsys):
    """Testing par_checker_file method"""
    expected_output = (
        "(()()((()))))()()()()((())()((()))()()()))()(((((((()()))()))())))) is NOT balanced\n"
        + "((())) is balanced\n"
        + "(())) is NOT balanced\n"
        + "((() is NOT balanced\n"
        + "(() is NOT balanced\n"
        + "() is balanced\n"
        + ") is NOT balanced"
    )
    par_checker_file("data/exercises/stacks/parentheses.txt")
    out, _ = capsys.readouterr()
    assert out.strip() == expected_output


@pytest.mark.parametrize(
    "number, base, expected",
    [
        (10, 2, "1010"),
        (127, 2, "1111111"),
        (256, 2, "100000000"),
        (10, 8, "12"),
        (127, 8, "177"),
        (256, 8, "400"),
        (10, 16, "A"),
        (127, 16, "7F"),
        (256, 16, "100"),
    ],
)
def test_base_converter(number, base, expected):
    """Testing base_converter method"""
    assert base_converter(number, base) == expected


@pytest.mark.parametrize(
    "number, base",
    [(160, 1), (160, 6), (160, 0)],
)
def test_base_converter_error(number, base):
    """Testing base_converter method errors"""
    with pytest.raises(ValueError) as excinfo:
        base_converter(number, base)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == f"Cannot convert to base {base}."


@pytest.mark.parametrize(
    "expression, expected",
    [("3 2 1 + *", 9), ("1 2 3 + -", -4), ("3 2 1 / *", 6.0), ("2 1 / 3 *", 6.0)],
)
def test_rpn_calc(expression, expected):
    """Testing rpn_calc method"""
    assert rpn_calc(expression) == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("1 2 3 / -", 1 / 3),
        ("1 3 / 2 +", 7 / 3),
        ("2 3 / 1 *", 2 / 3),
        ("2 1 3 / *", 2 / 3),
    ],
)
def test_rpn_calc_float(expression, expected):
    """Testing rpn_calc method with floating point results"""
    assert pytest.approx(rpn_calc(expression)) == expected


@pytest.mark.parametrize(
    "expression, err_message",
    [("3 2 1 +", "Stack is not empty"), ("3 2 1 + - *", "Stack is empty")],
)
def test_rpn_calc_stack_err(expression, err_message):
    """Testing rpn_calc method throwing Stack error"""
    with pytest.raises(StackError) as excinfo:
        rpn_calc(expression)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == err_message


@pytest.mark.parametrize(
    "expression, err_message, token",
    [("3 2 **", "Unknown token", "**"), ("a b +", "Unknown token", "a")],
)
def test_rpn_calc_token_err(expression, err_message, token):
    """Testing rpn_calc method throwing Token error"""
    with pytest.raises(TokenError) as excinfo:
        rpn_calc(expression)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == f"{err_message}: {token}"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
