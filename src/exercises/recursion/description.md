# Recursion is Recursive

Complete the following tasks:
Hint: read [PyFormat: Using % and .format() for great good!](https://pyformat.info/) in order to achieve the required output.
Idea for the iterative solutions: try to come up with a formula that connects the row number and the number of stars in it. You may need more than one loop.

1. Implement a **recursive** function to find the greatest common divisor of two numbers (i.e. gcd(1860, 2020) is 20).

2. Implement an **iterative** function that, when invoked as `hourglass_ite(5)`, prints the following hourglass figure:

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

3. Implement an **iterative** function that, when invoked as `diamond_ite(5)`, prints the following diamond figure:

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

4. Implement a **recursive** function that, when invoked as `hourglass_rec(5)`, prints the following hourglass figure:

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

5. This is a tricky task. Implement a **recursive** function that, when invoked as `diamond_rec(5)`, prints the following diamond figure:

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
