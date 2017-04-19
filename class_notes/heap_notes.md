

```python
import heapq
lst = [14, 35, 2, 3, 12, 9, 4, 12, 7, 13, 14, 5, 42, 6]
print(lst)
heapq.heapify(lst)
print(lst)
heapq.heappush(lst, 1)
print(lst)
print(heapq.heappop(lst))
print(lst)
```

    [14, 35, 2, 3, 12, 9, 4, 12, 7, 13, 14, 5, 42, 6]
    [2, 3, 4, 7, 12, 5, 6, 12, 35, 13, 14, 9, 42, 14]
    [1, 3, 2, 7, 12, 5, 4, 12, 35, 13, 14, 9, 42, 14, 6]
    1
    [2, 3, 4, 7, 12, 5, 6, 12, 35, 13, 14, 9, 42, 14]



```python
class BinaryHeap:
    """Heap class implementation"""
    def __init__(self, n=0):
        """Class constructor"""
        self._items = []
        self._limit = n

    def is_empty(self):
        """Is the heap empty"""
        return self._items == []

    def is_full(self):
        """Is the heap full"""
        return len(self._items) >= self._limit

    def __len__(self):
        """How big is the heap"""
        return len(self._items)
    
    def __str__(self):
        """Convert to string"""
        return str(self._items)

    def insert(self, item):
        """Add new item to te heap"""
        self._items.append(item)
        self.perc_up(len(self._items)-1)
    
    def perc_up(self, cur_idx):
        """Percolate up"""
        while (cur_idx - 1) // 2 >= 0:
            par_idx = (cur_idx - 1) // 2
            if self._items[cur_idx] < self._items[par_idx]:
                self._items[cur_idx], self._items[par_idx] = self._items[par_idx], self._items[cur_idx]
            else:
                return
            cur_idx = par_idx

    def get_min_child(self, par_idx):
        """Get the smaller child's index"""
        if 2 * par_idx + 2 > len(self._items) - 1:
            return 2 * par_idx + 1
        else:
            if self._items[2 * par_idx + 1] < self._items[2 * par_idx + 2]:
                return 2 * par_idx + 1
            else:
                return 2 * par_idx + 2    

    def perc_down(self, cur_idx):
        """Percolate down"""
        while 2*cur_idx + 1 < len(self._items):
            smaller_child_idx = self.get_min_child(cur_idx)
            if self._items[cur_idx] > self._items[smaller_child_idx]:
                self._items[cur_idx], self._items[smaller_child_idx] = self._items[smaller_child_idx], self._items[cur_idx]
            else:
                return
            cur_idx = smaller_child_idx
            
    def delete(self):
        """Remove the top of the heap"""
        self._items[0], self._items[len(self._items)-1] = self._items[len(self._items)-1], self._items[0]
        res = self._items.pop()
        self.perc_down(0)
        return res
        

    def heapify(self, lst):
        """Heapify a list"""
        self._items = lst[:]
        cur_idx = len(self._items) // 2 - 1
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1
```


```python
bin_heap = BinaryHeap()
lst = [14, 35, 2, 3, 12, 9, 4, 12, 7, 13, 14, 5, 42, 6]
print(lst)
bin_heap.heapify(lst)
print(bin_heap)
bin_heap.insert(1)
print(bin_heap)
print(bin_heap.delete())
print(bin_heap)
```

    [14, 35, 2, 3, 12, 9, 4, 12, 7, 13, 14, 5, 42, 6]
    [2, 3, 4, 7, 12, 5, 6, 12, 35, 13, 14, 9, 42, 14]
    [1, 3, 2, 7, 12, 5, 4, 12, 35, 13, 14, 9, 42, 14, 6]
    1
    [2, 3, 4, 7, 12, 5, 6, 12, 35, 13, 14, 9, 42, 14]

