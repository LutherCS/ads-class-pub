# Stack 'em Up!

Complete the following tasks and submit your source file(s) to KATIE.

1. Implement function `rev_string_simple(string: str)` that reverses characters in a string **without using** a stack.
1. Implement function `rev_string_stack` that reverses characters in a string **using** a stack.
1. Implement function `par_checker_file` that reads a list of expressions (parentheses) from a file (one expression per line), checks whether parentheses in each expression are balanced, and prints the result. Idea: use the textbook implementation of the `par_checker` function and invoke it with a line as a parameter. Hint: you may have to strip a line of the EOL symbol(s).
1. Implement function `base_converter` that converts any decimal number to the specified base. The function should only convert decimals to *binary* (base 2), *octal* (base 8), and *hexadecimal* (base 16), throwing exceptions in all other cases. Read the number and the base from a file, one case per line. Key point: use try..except to catch exceptions. Hint: extend the textbook implementation of `base_converter`.
1. Implement function `rpn_calc` that evaluates an expression in *Reverse Polish Notation* and returns its result, if possible. The function should process basic arithmetic operations (addition, subtraction, multiplication, and division) and throw an exception if the expression is invalid. Idea: add exception handling to the textbook implementation of the evaluator.
