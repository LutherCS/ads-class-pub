#!/usr/bin/env python3
"""
Testing project rpn
@authors: Roman Yasinovskyy, Karina Hoff
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
    from src.projects.rpn import StackError, TokenError, do_math, postfix_eval, rpn_calc


@pytest.mark.parametrize(
    "expression, expected",
    [("2 3 + =", 5), ("2 1 - =", 1), ("1 2 - 3 * 3 + =", 0), ("1 2 - 1 * =", -1)],
)
def test_postfix_eval(expression, expected):
    """Test correct postfix expressions"""
    assert postfix_eval(expression) == expected


@pytest.mark.parametrize(
    "filename, expected", [("rpn_input_1.txt", 18.61), ("rpn_input_2.txt", 8118)]
)
def test_checksum(filename, expected):
    """Test correct postfix expressions"""
    assert pytest.approx(rpn_calc(f"data/projects/rpn/{filename}"), 0.01) == expected


@pytest.mark.parametrize(
    "expression, err_message",
    [
        ("=", "Stack is empty"),
        ("1 2 =", "Stack is not empty"),
        ("1 2 3 + =", "Stack is not empty"),
        ("1 2 + 3 =", "Stack is not empty"),
    ],
)
def test_postfix_eval_stack_error(expression, err_message):
    """Test incorrect postfix expressions: Stack Error"""
    with pytest.raises(StackError) as excinfo:
        postfix_eval(expression)
    exception_message = excinfo.value.args[0]
    assert exception_message == err_message


@pytest.mark.parametrize(
    "expression, err_message, err_token",
    [("a b + =", "Unknown token", "a"), ("1 2 @ =", "Unknown token", "@")],
)
def test_postfix_eval_token_error(expression, err_message, err_token):
    """Test incorrect postfix expressions: Unknown Token Error"""
    with pytest.raises(TokenError) as excinfo:
        postfix_eval(expression)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"{err_message}: {err_token}"


@pytest.mark.parametrize(
    "operation, operand1, operand2, expected",
    [("+", 2, 3, 5), ("-", 2, 3, -1), ("*", 2, 3, 6), ("/", 10, 2, 5)],
)
def test_do_math_simple_int_success(operation, operand1, operand2, expected):
    """Test simple math expressions"""
    assert do_math(operation, operand1, operand2) == expected


@pytest.mark.parametrize(
    "operation, operand1, operand2, expected", [("/", 2, 3, 2 / 3)]
)
def test_do_math_simple_float_success(operation, operand1, operand2, expected):
    """Test simple math expressions"""
    assert do_math(operation, operand1, operand2) == pytest.approx(expected, 0.001)


@pytest.mark.parametrize(
    "operation, operand1, operand2, err_message",
    [
        ("/", 2, 0, "division by zero"),
        ("%", 2, 0, "integer division or modulo by zero"),
    ],
)
def test_do_math_simple_error(operation, operand1, operand2, err_message):
    """Test simple math expressions"""
    with pytest.raises(ZeroDivisionError) as excinfo:
        do_math(operation, operand1, operand2)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"{err_message}"


@pytest.mark.parametrize("symbol", [1, "a"])
def test_do_math_syntax_error(symbol):
    """Test incorrect simple math expressions"""
    with pytest.raises(SyntaxError) as excinfo:
        do_math(symbol, "/", 2)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"invalid syntax"


@pytest.mark.parametrize(
    "operation, operand1, operand2, expected",
    [("//", 2, 3, 0), ("//", 3, 2, 1), ("**", 2, 3, 8), ("**", 5, 6, 15625)],
)
def test_do_math_advanced(operation, operand1, operand2, expected):
    """Test simple math expressions"""
    assert do_math(operation, operand1, operand2) == expected


@pytest.mark.parametrize(
    "operation, operand1, operand2, expected",
    [
        ("&", 5, 6, 4),
        ("&", 51, 61, 49),
        ("|", 5, 6, 7),
        ("|", 51, 61, 63),
        ("^", 5, 6, 3),
        ("^", 51, 61, 14),
    ],
)
def test_do_math_bitwise(operation, operand1, operand2, expected):
    """Test simple math expressions"""
    assert do_math(operation, operand1, operand2) == expected


@pytest.mark.parametrize(
    "operation, operand1, operand2, err_message",
    [
        ("//", 2, 0, "integer division or modulo by zero"),
        ("//", 0, 0, "integer division or modulo by zero"),
    ],
)
def test_do_math_advanced_error(operation, operand1, operand2, err_message):
    """Test simple math expressions"""

    with pytest.raises(ZeroDivisionError) as excinfo:
        do_math(operation, operand1, operand2)
    exception_message = excinfo.value.args[0]
    assert exception_message == f"{err_message}"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
