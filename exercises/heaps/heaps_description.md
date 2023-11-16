# Is it a heap or is it a pile?

Complete the following tasks:

1. Show each step of turning list `[91, 27, 16, 20, 14, 98, 33, 63, 56, 30]` into a _min_ heap.

   - The following is an example of heapifying `[55, 73, 17, 41, 83, 89, 7, 28, 10, 69]`.

   | Step | Heap as a list                        |
   | ---- | ------------------------------------- |
   | 0    | 55, 73, 17, 41, 83, 89, 7, 28, 10, 69 |
   | 1    | 55, 73, 17, 41, 69, 89, 7, 28, 10, 83 |
   | 2    | 55, 73, 17, 10, 69, 89, 7, 28, 41, 83 |
   | 3    | 55, 73, 7, 10, 69, 89, 17, 28, 41, 83 |
   | 4    | 55, 10, 7, 28, 69, 89, 17, 73, 41, 83 |
   | 5    | 7, 10, 17, 28, 69, 89, 55, 73, 41, 83 |

2. Show each step of turning list `[30, 56, 63, 33, 98, 14, 20, 16, 27, 91]` into a _max_ heap.

   - The following is an example of heapifying `[69, 10, 28, 7, 89, 83, 41, 17, 73, 55]`.

   | Step | Heap as a list                        |
   | ---- | ------------------------------------- |
   | 0    | 69, 10, 28, 7, 89, 83, 41, 17, 73, 55 |
   | 1    | 69, 10, 28, 73, 89, 83, 41, 17, 7, 55 |
   | 2    | 69, 10, 83, 73, 89, 28, 41, 17, 7, 55 |
   | 3    | 69, 89, 83, 73, 55, 28, 41, 17, 7, 10 |
   | 4    | 89, 69, 83, 73, 55, 28, 41, 17, 7, 10 |
   | 5    | 89, 73, 83, 69, 55, 28, 41, 17, 7, 10 |

3. Show each intermediate step of adding 1 to the following heap: `[0, 20, 6, 34, 35, 51, 54, 36, 78, 92]`.

   - The following is the solution.

   | Step | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
   | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

4. Show each intermediate step of removing an item (0) from the following heap: `[0, 20, 6, 34, 35, 51, 54, 36, 78, 92]`.

   - The following is the solution.

   | Step | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
   | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

5. Show each intermediate step of sorting `[594, 850, 281, 952, 129, 348, 264, 972, 598, 758]` using _HeapSort_.
