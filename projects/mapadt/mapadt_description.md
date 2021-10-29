# Map ADT

Complete the following programming project.

Use the textbook implementation of the `HashTable` class and extend it, assuming integer keys.

1. `__init__()`. Initialize `HashMap` object of size `size_init` (16 by default). The class data members are as follows:

   - `_size` (max size)
   - `_keys` (initially a list of length `_size` with values evaluating to `False`)
   - `_values` (initially a list of length `_size` with values evaluating to `False`)

2. `__setitem__(key, value)`. Alias to `put`.

   - Add (if _key_ is not in the collection) a _value_ to the collection.
   - Update (if _key_ is already in the collection) a _value_ in the collection.
   - Raise a `MemoryError` exception if the table is full (a suitable position cannot be found after `_size` attempts).

3. `__getitem__(key)`. Alias to `get`.

   - Return a _value_ mapped to the provided _key_.
   - Raise a `KeyError` if the provided _key_ is not in the collection.

4. `__len__()`. Return the number of key-value pairs stored in the collection. Not to be confused with `_size` (a fixed maximum size of the collection).

5. `__contains__`. Return `True` for a statement of the form `key in map`, if the given `key` is in the collection, `False` otherwise.

6. `__str__`. Return string representation of the collection. Example: `{1: 'ant', 2: 'bee'}`

7. `_hash(key, size)`. Return `key` modulo `size`.

8. `_rehash`. Implement quadratic probing as a rehash technique.

9. `keys()`. Returns all keys in the map as a list.

10. `values()`. Returns all values in the map as a list.

11. `items()`. Returns all non-empty (key, value) tuples in the map as a list.

## What to do

`python3` should be `python3.9` or newer.

- Read _projects/mapadt/mapadt_description.md_ (this file).
- Modify and run _projects/mapadt/mapadt.py_.

```bash
python3 projects/mapadt/mapadt.py
```

- Compare your output to that provided in _projects/mapadt/mapadt_output.txt_.
- Test your implementation.

```bash
python3 -m pytest projects/mapadt/mapadt_test.py
```
