# Hashing it out

Complete the following tasks:

1. Implement a hash function for **integers** using the _simple remainder_ method.
2. Implement a hash function for **integers** using the _mid-square method_ (use 2 middle digits, pad with leading 0, if necessary).
3. Implement a hash function for **integers** using the _folding method_ (extract two digits at a time, the last item may be a single-digit number).
4. Implement the hash function for **string** using _sum of values_ of all characters.
5. Implement the hash function for **strings** using _character value and its position as a weight_.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/exercises/hashing/description.md_ (this file).
- Modify _src/exercises/hashing/hashing.py_.
- Run _src/exercises/hashing/hashing_main.py_.

```bash
python3 src/exercises/hashing/hashing_main.py
```

- Compare your output to that provided in _tests/exercises/hashing/hashing_output.txt_.
- Test your implementation.

```bash
python3 -m pytest tests/exercises/hashing/test_hashing.py
```
