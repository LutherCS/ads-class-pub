

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
class LinkedList:
    def __init__(self):
        self._head = None
        self._count = 0
    def is_empty(self):
        return self._count == 0
    def __len__(self):
        return self._count
    def add(self, new_node):
        if self._head == None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._count += 1
    def pop(self, position=None):
        pass
    def remove(self):
        pass
    def __str__(self):
        all_nodes = []
        current = self._head
        while current:
            all_nodes.append(current.data)
            current = current.next
        return str(all_nodes)
```


```python
import random
ll = LinkedList()
for _ in range(5):
    n = Node(random.randint(1, 10))
    ll.add(n)
    print("{}: {}".format(len(ll), ll))

```

    1: [8]
    2: [2, 8]
    3: [8, 2, 8]
    4: [7, 8, 2, 8]
    5: [9, 7, 8, 2, 8]



```python

```
