

```python
class Cat:
    def __init__(self, current_mood=None):
        self._mood = current_mood
    def __str__(self):
        return 'The cat is ' + self._mood
```


```python
class Node:
    def __init__(self, node_data=None):
        self._data = node_data
        self._next = None
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, node_data):
        self._data = node_data
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, node_next):
        self._next = node_next
    def __str__(self):
        return str(self._data)
```


```python
c1 = Cat('Grumpy')
c2 = Cat("Confused")
cat_node_1 = Node(c1)
cat_node_2 = Node(c2)
print(cat_node_1)
print(cat_node_2)
```

    The cat is Grumpy
    The cat is Confused



```python
n1 = Node()
print('n1 value is', n1)
n1.data = 'CS'
print('n1 value is', n1)
n2 = Node(160)
print('n2 value is', n2)
n3 = Node('2017-03-01')
print('n3 value is', n3)
print()
n1.next = n2
n2.next = n3
print(n1.next)
print(n1.next.next)
print(n1.next.next.next)
#print(n1.next.next.next.next)

```

    n1 value is None
    n1 value is CS
    n2 value is 160
    n3 value is 2017-03-01
    
    160
    2017-03-01
    None



```python
from abc import ABC, abstractmethod
class LinkedList(ABC):
    @abstractmethod
    def __init__(self):
        self._head = None
        self._count = 0
    def is_empty(self):
        return self._count == 0
    def __len__(self):
        return self._count
    @abstractmethod
    def add(self, new_node):
        pass
    @abstractmethod
    def append(self, new_node):
        pass
    @abstractmethod
    def insert(self, new_node):
        pass
    @abstractmethod
    def index(self, value):
        pass
    @abstractmethod
    def remove(self):
        pass
    def pop(self, position=None):
        pass
    def __getitem__(self, rng):
        if isinstance(rng, int):
            #return a single node
            pass
        elif isinstance(rng, slice):
            #return a slice
            slice_lst = UnorderedLinkedList()
            slice_rng = list(range(rng.start, rng.stop))
            slice_count = 0
            current = self._head
            while current and slice_count < rng.start:
                current = current.next
                slice_count += 1
            while current and slice_count < rng.stop:
                slice_lst.append(Node(current.data))
                current = current.next
                slice_count += 1
            return slice_lst

    def __str__(self):
        all_nodes = []
        current = self._head
        while current:
            all_nodes.append(current.data)
            current = current.next
        return str(all_nodes)
```


```python
class UnorderedLinkedList(LinkedList):
    def __init__(self):
        #LinkedList.__init__(self)
        super().__init__()
    def add(self, new_node):
        '''Add a new node at the beginning of a list'''
        new_node.next = self._head
        self._head = new_node
        self._count += 1

    def append(self, new_node):
        '''Add a new node at the end of a list'''
        if not self._head:
            self._head = new_node
            self._count += 1
            return
        current  = self._head
        while current.next:
            current = current.next
        current.next = new_node
        self._count += 1

    def insert(self, new_node):
        pass

    def index(self, value):
        pass

    def remove(self, value):
        '''Remove a node with the specified value from a list'''
        prev = None
        current = self._head
        while current and current.data != value:
            prev = current
            current = current.next
        if current:
            if prev:
                prev.next = current.next
            else:
                self._head = current.next
            del current
            self._count = self._count - 1
```


```python
import random
ull = UnorderedLinkedList()
for _ in range(10):
    n = Node(random.randint(1, 10))
    ull.append(n)
    print("{}: {}".format(len(ull), ull))
print('node removal')
ull.remove(5)
print("{}: {}".format(len(ull), ull))
print(ull[1:3])

```

    1: [3]
    2: [3, 8]
    3: [3, 8, 5]
    4: [3, 8, 5, 10]
    5: [3, 8, 5, 10, 8]
    6: [3, 8, 5, 10, 8, 1]
    7: [3, 8, 5, 10, 8, 1, 7]
    8: [3, 8, 5, 10, 8, 1, 7, 9]
    9: [3, 8, 5, 10, 8, 1, 7, 9, 5]
    10: [3, 8, 5, 10, 8, 1, 7, 9, 5, 7]
    node removal
    9: [3, 8, 10, 8, 1, 7, 9, 5, 7]
    [8, 10]

