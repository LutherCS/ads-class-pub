# •••---•••

This assignment is a good practice working with trees. You are to write a class Coder that allows you to _encode_ and _decode_ [Morse code](https://en.wikipedia.org/wiki/Morse_code). Morse code is a common code that is used to encode messages consisting of letters and digits. Each letter consists of a series of dots and dashes; for example, the code for the letter _a_ is `•–` and the code for the letter _b_ is `–•••`.

## Approach

Build a tree similar to the following (ours is going to be smaller as our alphabet is smaller):

![Morse Code tree](https://upload.wikimedia.org/wikipedia/commons/c/ca/Morse_code_tree3.png)

Store each letter of the alphabet in a node of a binary tree. The root node is at level 0 and stores no letter. The left node at level 1 stores the letter _e_ (code is `•`), and the right node stores the letter _t_ (code is `–`). The 4 nodes at level 2 store the letters with codes `••`, `•–`, `–•`, and `––`. Other nodes follow the same pattern.

To build the tree, read the file _data/projects/morse/morse.txt_ in which each line consists of a letter followed by its code. The letters should be placed properly in the tree. To find the position for a letter in the tree, scan the code and branch left for a _dot_ and branch right for a _dash_.

_Encode_ a message by replacing each letter with its code.

_Decode_ a message using the Morse code tree.

## Algorithm

### Build (initialize) the tree

1. Create an empty _Binary Tree_.
2. Split every line in a file into a letter and its code.
3. Follow the code string to find a proper place for a letter based on the code.

### Find the proper place for a letter

1. Start with the root of the tree as your current node.
2. Repeat steps 3-6 for every symbol in the code.
3. If a symbol is a _dot_, check if the left child is empty (`None`). If it is, insert a new node with '' (empty string) as a key.
4. If a symbol is a _dot_, change the current node to the left child of the current node.
5. If a symbol is a _dash_, check if the right child is empty (`None`). If it is, insert a new node with '' (empty string) as a key.
6. If a symbol is a _dash_, change the current node to the right child of the current node.
7. Assign the letter as a value to the current node.

### Find a letter in the tree by its code

1. Start with the root of the tree as your current node.
2. Repeat steps 3-4 for every symbol in the code.
3. If a symbol is a _dot_, change the current node to the left child of the current node.
4. If a symbol is a _dash_, change the current node to the right child of the current node.
5. Return the value of the current node.

### Decode (letters are separated by spaces)

1. Start with an empty message.
2. For every letter in the coded message, find it in the tree and append to the message.
3. Return the resulting message.

### Encode

1. Start with an empty code message.
2. For every word in the message do the following
   - For every letter in a word find the path to its node in the tree and append it (path) to the code
3. Return the resulting morse code

### Find the path to a letter

1. A function should take a tree, a letter, and a path as parameters.
2. If a tree is empty, return `False`
3. If the tree root key is the letter, return the path
4. In other cases return the result of recursive search in the left subtree (starting path `•`) or the right subtree (starting path `-`).

## Grading criteria

1. An initial tree is properly built based on the values read from the file.
2. Letter insertion function is properly implemented.
3. Letter retrieval function is properly implemented.
4. Recursive code retrieval function is properly implemented.
5. Pass all unit tests.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/projects/morse/description.md_ (this file).
- Modify _src/projects/morse/morse.py_.
- Run _src/projects/morse/morse_main.py_.

```bash
python3 src/projects/morse/morse_main.py
```

- Compare your output to that provided in _tests/projects/morse/morse_output.txt_.
- Test your implementation.

```bash
python3 -m pytest tests/projects/morse/test_morse.py
```
