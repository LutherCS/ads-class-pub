# Map ADT

Complete the following programming project.

Use the textbook implementation of the `HashTable` class and extend it, assuming integer keys.

1. `__init__()`. Initialize `HashMap` object of size `size_init` (16 by default). The class data members are as follows:

   - `_size` (max size)
   - `_keys` (initially a list of length `_size` with values evaluating to `False`)
   - `_values` (initially a list of length `_size` with values evaluating to `False`)

1. `__setitem__(key, value)`. Alias to `put`.

   - Add (if _key_ is not in the collection) a _value_ to the collection.
   - Update (if _key_ is already in the collection) a _value_ in the collection.
   - Raise a `MemoryError` exception if the table is full (a suitable position cannot be found after `_size` attempts).

1. `__getitem__(key)`. Alias to `get`.

   - Return a _value_ mapped to the provided _key_.
   - Raise a `KeyError` if the provided _key_ is not in the collection.

1. `__len__()`. Return the number of key-value pairs stored in the collection. Not to be confused with `_size` (a fixed maximum size of the collection).

1. `__contains__`. Return `True` for a statement of the form `key in map`, if the given `key` is in the collection, `False` otherwise.

1. `__str__`. Return string representation of the collection. Example: `{1: 'ant', 2: 'bee'}`

1. `_hash(key, size)`. Return `key` modulo `size`.

1. `_rehash`. Implement quadratic probing as a rehash technique.

1. `keys()`. Returns all keys in the map as a list.

1. `values()`. Returns all values in the map as a list.

1. `items()`. Returns all non-empty (key, value) tuples in the map as a list.
