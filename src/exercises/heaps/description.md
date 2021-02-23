# Is it a heap or is it a pile?

Complete the following tasks:

1. Show each step of turning list **[60, 32, 46, 41, 45, 34, 50, 21, 10, 28]** into a **min** heap. The result should be **[10, 21, 34, 32, 28, 46, 50, 60, 41, 45]**.

| Step | List                                   |
| ---- | -------------------------------------- |
| 0    | 60, 32, 46, 41, 45, 34, 50, 21, 10, 28 |
| 1    | 60, 32, 46, 41, 28, 34, 50, 21, 10, 45 |
| 2    | 60, 32, 46, 10, 28, 34, 50, 21, 41, 45 |
| 3    | 60, 32, 34, 10, 28, 46, 50, 21, 41, 45 |
| 4    | 60, 10, 34, 21, 28, 46, 50, 32, 41, 45 |
| 5    | 10, 21, 34, 32, 28, 46, 50, 60, 41, 45 |

1. Implement a binary heap as a **max** heap, rather than a min heap.

1. Create a **max** heap with a limited size. In other words, the heap only keeps track of _n_ largest items. If the heap grows in size to its limit, the smallest item is dropped (removed from a heap). If a new item is smaller than the smallest heap item, the new element is not added.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/exercises/heaps/description.md_ (this file).
- Modify _src/exercises/heaps/heaps.py_.
- Test your implementation.

```bash
python3 -m pytest tests/exercises/heaps/test_heaps.py
```
