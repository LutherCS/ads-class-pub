# Is it a heap or is it a pile?

Complete the following exercises and submit your source code to KATIE as a single file (archive).

1. Implement function *height*, member of the class BinaryTree, that returns the height of a tree.

2. Implement function *size*, member of the class BinaryTree, that returns the number of nodes in a tree.

3. Show each step of turning list **[60, 32, 46, 41, 45, 34, 50, 21, 10, 28]** into a **min** heap. The result should be **[10, 21, 34, 32, 28, 46, 50, 60, 41, 45]**.

Step | List
---|---
0 | 60, 32, 46, 41, 45, 34, 50, 21, 10, 28
1 | 60, 32, 46, 41, 28, 34, 50, 21, 10, 45
2 | 
3 | 
4 | 
5 | 10, 21, 34, 32, 28, 46, 50, 60, 41, 45


4. Implement a binary heap as a **max** heap, rather than a min heap.

5. Create a **max** heap with a limited size. In other words, the heap only keeps track of *n* largest items. If the heap grows in size to its limit, the smallest item is dropped (removed from a heap). If a new item is smaller than the smallest heap item, the new element is not added.
