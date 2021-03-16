# Recursion is Recursive

Complete the following tasks:
Hint: read [PyFormat: Using % and .format() for great good!](https://pyformat.info/) in order to achieve the required output.
Idea for the iterative solutions: try to come up with a formula that connects the row number and the number of stars in it. You may need more than one loop.
Idea for the recursive solutions: you may need additional function(s) to print top and bottom of the figure.

1. Implement a _recursive_ function to find the greatest common divisor of two numbers (i.e. `gcd(1860, 2020)` is 20, `gcd(1861, 2021)` is 1).

2. Implement an _iterative_ function that, when invoked as `diamond_ite(n)`, prints a diamond figure with `2n-1` lines. Each line should have an odd number of asterisks with `2n-1` asterisks in the the widest (middle) line. For example, calling `diamond_ite(5)` prints the following diamond figure:

   ```text
       *
      ***
     *****
    *******
   *********
    *******
     *****
      ***
       *
   ```

3. **This is a tricky task**. Implement a _recursive_ function that, when invoked as `diamond_rec(n)`, prints a diamond figure with `2n-1` lines. Each line should have an odd number of asterisks with `2n-1` asterisks in the the widest (middle) line. For example, calling `diamond_rec(5)` prints the following diamond figure:

   ```text
       *
      ***
     *****
    *******
   *********
    *******
     *****
      ***
       *
   ```

4. Implement an _iterative_ function that, when invoked as `hourglass_ite(n)`, prints an hourglass figure with `2n-1` lines. Each line should have an odd number of asterisks with `2n-1` asterisks in the the widest (top and bottom) lines. For example, calling `hourglass_ite(5)` prints the following hourglass figure:

   ```text
   *********
    *******
     *****
      ***
       *
      ***
     *****
    *******
   *********
   ```

5. Implement a _recursive_ function that, when invoked as `hourglass_rec(n)`, prints an hourglass figure with `2n-1` lines. Each line should have an odd number of asterisks with `2n-1` asterisks in the the widest (top and bottom) lines. For example, calling `hourglass_rec(5)` prints the following hourglass figure:

   ```text
   *********
    *******
     *****
      ***
       *
      ***
     *****
    *******
   *********
   ```

## What to do

`python3` should be `python3.9` or newer.

- Read _src/exercises/recursion/description.md_ (this file).
- Modify _src/exercises/recursion/recursion.py_.
- Run _src/exercises/recursion/recursion_main.py_.

```bash
python3 src/exercises/recursion/recursion_main.py
```

- Compare your output to that provided in _tests/exercises/recursion/recursion_output.txt_.
- Test your implementation.

```bash
python3 -m pytest tests/exercises/recursion/test_recursion.py
```
