# Hashing it out

Complete the following tasks:

1. Implement a hash function for _integers_ using the _simple remainder_ method.
2. Implement a hash function for _integers_ using the _mid-square method_ (use 2 middle digits, pad with leading 0, if necessary).
3. Implement a hash function for _integers_ represented as _strings_ (e.g. SSN or phone numbers) using the _folding_ method (extract two digits at a time ignoring non-digits, the last item may be a single-digit number).
4. Implement the hash function for _strings_ using _sum of ASCII values_ of all characters.
5. Implement the hash function for _strings_ using _character value_ and its _position_ as a weight (coefficient).

## What to do

`python3` should be `python3.9` or newer.

- Read _exercises/hashing/description.md_ (this file).
- Modify and run _exercises/hashing/hashing.py_.

```bash
python3 exercises/hashing/hashing.py
```

- Compare your output to that provided in _exercises/hashing/hashing_output.txt_.
- Test your implementation.

```bash
python3 -m pytest exercises/hashing/test_hashing.py
```
