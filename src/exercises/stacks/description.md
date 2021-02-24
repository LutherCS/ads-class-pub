# Stack 'em Up

Complete the following tasks:

1. Implement function `rev_string_stack` that reverses characters in a string *using a stack*.
1. Implement function `par_checker_ext` to process the following:
   - parentheses `(` and `)`
   - curly braces `{` and `}`
   - brackets `[` and `]`
   - angle brackets `<` and `>`
1. Implement function `par_checker_file` that reads a list of expressions (parentheses) from a file (one expression per line), checks whether parentheses in each expression are balanced, and prints the result. Idea: use the textbook implementation of the `par_checker` function and invoke it with a line as a parameter. Hint: you may have to strip a line of the EOL symbol(s).
1. Implement function `base_converter` that converts any decimal number to the specified base. The function should only convert decimals to _binary_ (base 2), _octal_ (base 8), and _hexadecimal_ (base 16), throwing `ValueError` in all other cases. Key point: use `try..except` to catch exceptions. Hint: extend the textbook implementation of `base_converter`.
1. Implement function `rpn_calc` that evaluates an expression in _Reverse Polish Notation_ and returns its result, if possible. The function should process basic arithmetic operations (addition, subtraction, multiplication, and division) and throw an exception if the expression is invalid. Idea: add exception handling to the textbook implementation of the evaluator.

## What to do

- Read _src/exercises/stacks/description.md_ (this file).
- Modify _src/exercises/stacks/stacks.py_.
- Run _src/exercises/stacks/stacks_main.py_.

```bash
python3 src/exercises/stacks/stacks_main.py
```

- Compare your output to that provided in _tests/exercises/stacks/stacks_output.txt_.
- Test your implementation.

```bash
python -m pytest tests/exercises/stacks/test_stacks.py
```
