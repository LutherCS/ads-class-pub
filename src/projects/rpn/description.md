# Reverse Polish Notation

Complete the following tasks:

## Tasks

1. Read _Reverse Polish notation_ expressions from the files _rpn_input_1.txt_ and _rpn_input_2.txt_, one expression per line. Throw an exception and quit gracefully (with a meaningful error message) if the file does not exist.
1. Print each expression (line) as it appears in the file (i.e. in Reverse Polish notation).
1. Use the `Stack` class (import from `pythonds3` or copy/paste the implementation code) to evaluate each expression and print its result, if the expression is valid.
1. Print the source of an error (invalid operation, an insufficient number of operands, incomplete expression etc.) if the expression is invalid.
1. Process the following operators: `+`, `-`, `*`, `/`, `%`.
1. Process the following advanced operators: `//` (integer division), `**` (power of). Note that these operations require you to process two characters to work properly and should not be confused with simple division and multiplication.
1. Continue reading from the file until done. Your program should print an error message but not crash if any expression is invalid.
1. Calculate and print _checksum_ - sum of all valid results.
1. Add your name and the assignment number as a comment to the source file.
1. Use exception handling `try..except` in order to catch errors.

## Optional task

Implement bitwise operators `&`, `|`, and `^`.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/projects/rpn/description.md_ (this file).
- Modify _src/projects/rpn/rpn.py_.
- Run _src/projects/rpn/rpn_main.py_.

```bash
python3 src/projects/rpn/rpn_main.py
```

- Compare your output to that provided in _tests/projects/rpn/rpn_output.txt_.
- Test your implementation.

```bash
python3 -m pytest tests/projects/rpn/test_rpn.py
```
