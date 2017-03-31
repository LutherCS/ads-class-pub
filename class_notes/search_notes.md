

```python
class Student:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def __eq__(self, other):
        return self._name == other.name

roster = [Student('zack'), Student('bob'), Student('chuck')]
name = Student('zack')

def search(lst, val):
    for n in lst:
        if n == val:
            return True
    return False

print(search(roster, name))
```

    True



```python
class Map:
    '''Map ADT implementation'''
    def __init__(self, size=8):
        '''Create a Map object'''
        self._items = [None] * size
        self._size = size
        # Hint: use this to keep track of all the keys
        self._keys = set()

    def rehash(self, key, k=0):
        '''Re-hash function'''
        return (key % self._size + k * k) % self._size

    def get(self, key):
        '''Given a key, return the value stored in the map or None otherwise'''
        pass

    def put(self, key, val):
        '''Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value'''
        #Store key:value as a tuple (key, value) in the list of items
        pos = self.rehash(key)
        #Adding a new item
        if not self._items[pos]:
            self._items[pos] = (key, val)
            self._keys.add(key)
        else:
            #Resolving a collision
            for k in range(self._size):
                pos = self.rehash(key, k)
                #Found an empty spot
                if not self._items[pos]:
                    self._items[pos] = (key, val)
                    break
                #Found an item to update
                elif self._items[pos][0] == key:
                    self._items[pos] = (key, val)
                    break

    def __contains__(self, key):
        '''Return True for a statement of the form key in map, if the given key is in the map, False otherwise'''
        return key in self._keys

    def __len__(self):
        '''Return the number of key-value pairs stored in the map'''
        return self._size - self._items.count(None)

    def __str__(self):
        '''Return the string representation of the map object'''
        return str([i for i in self._items if i])

```


```python
m = Map()
m.put(33, "Alice")
print(m)
print("Items in the map: {}".format(len(m)))
m.put(25, "Chuck")
m.put(35, "Bob")
print(m)
print("Items in the map: {}".format(len(m)))
print("Key 33 in the map: {}".format(33 in m))
print("Key 34 in the map: {}".format(34 in m))
m.put(35, "Dave")
print(m)
print("Items in the map: {}".format(len(m)))
```

    [(33, 'Alice')]
    Items in the map: 1
    [(33, 'Alice'), (25, 'Chuck'), (35, 'Bob')]
    Items in the map: 3
    Key 33 in the map: True
    Key 34 in the map: False
    [(33, 'Alice'), (25, 'Chuck'), (35, 'Dave')]
    Items in the map: 3

