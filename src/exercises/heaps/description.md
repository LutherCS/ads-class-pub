# Is it a heap or is it a pile?

Complete the following tasks:

1. Show each step of turning list `[42, 35, 71, 34, 76, 39, 77, 47, 6, 20]` into a _min_ heap.
   - The following is an example of heapifying `[55, 73, 17, 41, 83, 89, 7, 28, 10, 69]`.

   | Step | List                                  |
   | ---- | ------------------------------------- |
   | 0    | 55, 73, 17, 41, 83, 89, 7, 28, 10, 69 |
   | 1    | 55, 73, 17, 41, 69, 89, 7, 28, 10, 83 |
   | 2    | 55, 73, 17, 10, 69, 89, 7, 28, 41, 83 |
   | 3    | 55, 73, 7, 10, 69, 89, 17, 28, 41, 83 |
   | 4    | 55, 10, 7, 28, 69, 89, 17, 73, 41, 83 |
   | 5    | 7, 10, 17, 28, 69, 89, 55, 73, 41, 83 |

2. Show each step of turning list `[42, 35, 71, 34, 76, 39, 77, 47, 6, 20]` into a _max_ heap.
   - The following is an example of heapifying `[69, 10, 28, 7, 89, 83, 41, 17, 73, 55]`.

   | Step | List                                  |
   | ---- | ------------------------------------- |
   | 0    | 69, 10, 28, 7, 89, 83, 41, 17, 73, 55 |
   | 1    | 69, 10, 28, 73, 89, 83, 41, 17, 7, 55 |
   | 2    | 69, 10, 83, 73, 89, 28, 41, 17, 7, 55 |
   | 3    | 69, 89, 83, 73, 55, 28, 41, 17, 7, 10 |
   | 4    | 89, 69, 83, 73, 55, 28, 41, 17, 7, 10 |
   | 5    | 89, 73, 83, 69, 55, 28, 41, 17, 7, 10 |

3. Implement a binary heap as a **max** heap, rather than a min heap. Use the textbook implementation of the min heap for details.
   1. Implement method `insert` (and `perc_up`, if necessary)
   1. Implement method `delete` (and `perc_down`, if necessary)
   1. Implement method `heapify` (and `perc_down`, if necessary)

## What to do

`python3` should be `python3.9` or newer.

- Read _src/exercises/heaps/description.md_ (this file).
- Complete tasks 1 and 2 in a new file (markdown or plain text should work just fine)
- Modify _src/exercises/heaps/heaps.py_.
- Run _src/exercises/heaps/heaps_main.py_.

```bash
python3 src/exercises/heaps/heaps_main.py
```

- Compare your output to that provided in _tests/exercises/heaps/heaps_output.txt_.
- Test your implementation.

```bash
python3 -m pytest tests/exercises/heaps/test_heaps.py
```
