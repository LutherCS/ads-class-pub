
# Stack ADT
 * Stack
 * push
 * pop
 * peek
 * size
 * is_empty


```python
class Stack():
    '''Stack as a Python list'''
    def __init__(self):
        self._items = []
    
    def push(self, new_item):
        '''Add a new item'''
        self._items.append(new_item)
    
    def peek(self):
        '''Look at the top item'''
        if len(self._items) > 0:
            return self._items[-1]
        else:
            raise IndexError('The stack (list) is empty')
    
    def __len__(self):
        '''Get stack size'''
        return len(self._items)
    
    def size(self):
        '''Get stack size'''
        return len(self._items)
    
    def pop(self):
        '''Remove the top item'''
        if len(self._items) > 0:
            return self._items.pop()
        else:
            raise IndexError('The stack (list) is empty')
    
    def is_empty(self):
        '''Check if the stack is empty'''
        return self._items == []
```


```python
import time
s = Stack()
s.push('CS')
s.push(160)
print(s.peek())
print(s.pop())
s.pop()
try:
    print(s.peek())
except IndexError as ie:
    print('Caught an error: {}'.format(ie))
t = time.process_time()
n = 1000000
for i in range(n):
    s.push(i)
print("Added {} items to a stack in {} sec".format(n, time.process_time() - t))
```

    160
    160
    Caught an error: The stack (dict) is empty
    Added 1000000 items to a stack in 0.5260622419999983 sec



```python
class Stack():
    '''Stack as a Python dictionary'''
    def __init__(self):
        self._items = {}
        self._top = -1
    
    def push(self, new_item):
        '''Add a new item'''
        self._top = self._top + 1
        self._items[self._top] = new_item
    
    def peek(self):
        '''Look at the top item'''
        if len(self._items) > 0:
            return self._items[self._top]
        else:
            raise IndexError('The stack (dict) is empty')
    
    def __len__(self):
        '''Get stack size'''
        return len(self._items)
    
    def size(self):
        '''Get stack size'''
        return len(self._items)
    
    def pop(self):
        '''Remove the top item'''
        if len(self._items) > 0:
            result = self._items[self._top]
            del self._items[self._top]
            self._top = self._top - 1
            return result
        else:
            raise IndexError('The stack (dict) is empty')
    
    def is_empty(self):
        '''Check if the stack is empty'''
        return self._items == {}
```


```python
import time
s = Stack()
s.push('CS')
s.push(160)
print(s.peek())
print(s.pop())
s.pop()
try:
    print(s.peek())
except IndexError as ie:
    print('Caught an error: {}'.format(ie))
t = time.process_time()
n = 1000000
for i in range(n):
    s.push(i)
print("Added {} items to a stack in {} sec".format(n, time.process_time() - t))
```

    160
    160
    Caught an error: The stack (dict) is empty
    Added 1000000 items to a stack in 0.5252935169999979 sec



```python

```
