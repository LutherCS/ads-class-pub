# Reverse Polish Notation

Complete the following programming project and submit your source code (as a single file) to KATIE.

## Tasks

1. Read Reverse Polish notation expressions from the files *rpn_input_1.txt* and *rpn_input_2.txt*, one expression per line. Throw an exception and quit gracefully (with a meaningful error message) if the file does not exist.

1. Print each expression (line) as it appears in the file (ie. in Reverse Polish notation).

1. Use the *Stack* class (implement your own or use *pythonds3*) to evaluate each expression and print its result, if the expression is valid.

1. Print the source of an error (invalid operation, an insufficient number of operands, incomplete expression etc.) if the expression is invalid.

1. Process the following operators: `+`, `-`, `*`, `/`, `%`.

1. Process the following advanced operators: `//` (integer division), `**` (power of). Note that these operations require you to process two characters to work properly and should not be confused with simple division and multiplication.

1. Continue reading from the file until done. Your program should print an error message but not crash if any expression is invalid.

1. Calculate and print **checksum** - sum of all valid results.

1. Add your name and the assignment number as a comment to the source file.

1. Use exception handling `try..except` in order to catch errors.
