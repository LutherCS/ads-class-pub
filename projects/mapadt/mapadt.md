# Map ADT

Complete the following programming project and submit your source code (as a single archive file) to KATIE.

Use the textbook implementation of the `HashTable` class and extend it.

1. `__init__()`. Map constructor.

2. `__len__()`. Return the number of key-value pairs stored in the collection.

3. `get(key)`. Return a *value* by the *key* or `None` if the provided *key* is not in the collection. Same as `__getitem__`.

4. `put(key, value)`. Same as `__setitem__`.

* Add (if *key* is not in the collection) a *value* to the collection.

* Update (if *key* is already in the collection) a *value* in the collection.

* Raise an exception if the table is full (a suitable position cannot be found after *size* attempts).

5. `__contains__`. Return `True` for a statement of the form `key in map`, if the given *key* is in the collection, `False` otherwise.

6. `__str__`. Return string representation of the collection.

7. `_hash(key, size)`. Return *key* modulo *size*.

8. `_rehash`. Implement quadratic probing as a rehash technique.

9. `keys()`. Returns all keys in the map as a list.

10. `values()`. Returns all values in the map as a list.

11. `items()`. Returns all non-empty (key, value) tuples in the map as a list.
