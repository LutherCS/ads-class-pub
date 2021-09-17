# README

## What is this repository for

- Algorithms and Data Structures class
- Class notes
- Code templates

## How do I get set up

Windows users may have to substitute _python_ with _py -3_ for the following commands to work. You should keep the same file structure as **this** repository and run all the commands from its top directory (i.e. ads-class-pub).

- Clone the repository.

```bash
git clone https://github.com/LutherCS/ads-class-pub.git
```

- Get updates.

```bash
git pull origin
```

- Install _pythonds3_ to use textbook implementations of various data structures and algorithms.

```bash
python -m pip install -U pythonds3
```

- Install linters _pylint_ and _mypy_.

```bash
python -m pip install -U pylint mypy
```

- Install formatter _black_.

```bash
python -m pip install -U black
```

- Install testing framework _pytest_ and its plugin _pytest-timeout_.

```bash
python -m pip install -U pytest pytest-timeout
```

- Install _colorama_ to colorize output.

```bash
python -m pip install -U colorama
```

## How do I run my code

- Run project _hello_

```bash
python projects/hello/hello.py
```

- Run project _hello_ that takes file _hello\_in.txt_ as input

```bash
python projects/hello/hello.py projects/hello/hello_in.txt
```

The source should be modified as follows (sys.argv contains all the arguments passed to the application, including the application file name itself as sys.argv[0]):

```python
import sys

def main(filename):
    print(f"Processing file {filename}")

    if __name__ == '__main__':
        main(sys.argv[1])
```

- Test project _hello_

```bash
python -m pytest projects/hello/hello_test.py
```

- Run exercise _hello_

```bash
python exercises/hello/hello.py
```

- Test exercise _hello_

```bash
python -m pytest exercises/hello/hello_test.py
```

## References

### Text Editors and IDEs

[Popular development environments](https://insights.stackoverflow.com/survey/2018) include the following:

- [Visual Studio Code](https://code.visualstudio.com/) | [setup](https://code.visualstudio.com/docs/languages/python)
- [Sublime Text](https://www.sublimetext.com/) | [setup](https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/)
- [vim](http://www.vim.org/) | [setup](https://realpython.com/vim-and-python-a-match-made-in-heaven/)
- [Atom](https://atom.io/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Jupyter Notebook](http://jupyter-notebook.readthedocs.io/en/latest/notebook.html)
- [Wing IDE](https://wingware.com/)

### Tools and Utilities

- [An Introduction to the Linux Terminal | DigitalOcean](https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal)
- [git - the simple guide - no deep shit!](http://rogerdudler.github.io/git-guide/)
- [Installing Packages — Python Packaging User Guide](https://packaging.python.org/tutorials/installing-packages/)
- [Pipenv: A Guide to the New Python Packaging Tool – Real Python](https://realpython.com/pipenv-guide/)
- [pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/latest/)

### Python Basics

- [The Python Standard Library — Python 3.7.0 documentation](https://docs.python.org/3/library/index.html)
- [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
- [Python Style Guidelines - The Chromium Projects](https://www.chromium.org/chromium-os/python-style-guidelines)
- [mattharrison/Tiny-Python-3.6-Notebook: This repository contains the text for the Tiny Python 3.6 Notebook.](https://github.com/mattharrison/Tiny-Python-3.6-Notebook)
- [crazyguitar/pysheeet: Python Cheat Sheet](https://github.com/crazyguitar/pysheeet)

### Exception Handling

- [8. Errors and Exceptions — Python 3.6.0 documentation](https://docs.python.org/3/tutorial/errors.html)
- [Python Exceptions Handling](https://www.tutorialspoint.com/python/python_exceptions.htm)

### Object-Oriented Programming

- [Python @property: How to Use it and Why? - Programiz](https://www.programiz.com/python-programming/property)
- [Introduction to Python descriptors – IBM Developer](https://developer.ibm.com/tutorials/os-pythondescriptors/)
- [Python Tutorial: Properties vs. getters and setters](https://www.python-course.eu/python3_properties.php)
- [Descriptor HowTo Guide — Python 3.7.2 documentation](https://docs.python.org/3/howto/descriptor.html)
- [Object-Oriented Programming (OOP) in Python 3 – Real Python](https://realpython.com/python3-object-oriented-programming/)
- [Jupyter Notebook Viewer - The Tao of Python](http://nbviewer.jupyter.org/github/akittas/presentations/blob/master/pythess/tao_mro/tao_of_python.ipynb)
- [3. Data model — Python 3.7.0 documentation](https://docs.python.org/3/reference/datamodel.html)
- [Underscores in Python](https://shahriar.svbtle.com/underscores-in-python)
- [Python3 Tutorial: Magic Methods](http://www.python-course.eu/python3_magic_methods.php)
- [Python Class Examples: Init and Self - Dot Net Perls](https://www.dotnetperls.com/class-python)
- [The self variable in python explained | Python Tips](https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/)
- [OOP - Inheritance](http://ccm.net/contents/422-oop-inheritance)
- [An Introduction to Classes and Inheritance (in Python) - Jessica Hamrick](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
- [Learn Python the Hard Way - Read for Free](https://learnpythonthehardway.org/book/ex44.html)
- [Python3 Tutorial: Inheritance](http://www.python-course.eu/python3_inheritance.php)

### Algorithm Analysis

- [Analysis of Algorithms](http://www.greenteapress.com/thinkpython/html/thinkpython022.html)
- [A Gentle Introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
- [Analysis of Algorithms](http://aofa.cs.princeton.edu/10analysis/)

### Basic Data Structures

- [VisuAlgo - Linked List (Single, Doubly), Stack, Queue, Deque](https://visualgo.net/en/list)

### Recursion

- [In plain English, what is recursion? - Software Engineering Stack Exchange](https://softwareengineering.stackexchange.com/questions/25052/in-plain-english-what-is-recursion)
- [An Introduction to Recursion, Part 1 – topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-recursion-part-1/)
- [An Introduction to Recursion: Part 2 – topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-recursion-part-2/)

### Searching Algorithms

- [Data Structures and Algorithms Hash Table](https://www.tutorialspoint.com/data_structures_algorithms/hash_data_structure.htm)
- [Basics of Hash Tables Tutorials & Notes | Data Structures | HackerEarth](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)

### Sorting Algorithms

- [Sorting algorithms visualized with animated color palette | FlowingData](https://flowingdata.com/2017/10/26/sorting-algorithms-visualized-with-rainbow-color-palette/)
- [Sorting Algorithm Animations | Toptal](https://www.toptal.com/developers/sorting-algorithms)
- [VisuAlgo - Sorting (Bubble, Selection, Insertion, Merge, Quick, Counting, Radix)](https://visualgo.net/bn/sorting)

### Trees

- [Binary Trees](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html)
- [Binary Trees](http://cslibrary.stanford.edu/110/BinaryTrees.html)
- [Binary Tree -- from Wolfram MathWorld](http://mathworld.wolfram.com/BinaryTree.html)

### Graphs

- [Data Structures and Algorithms Graph Data Structure](https://www.tutorialspoint.com/data_structures_algorithms/graph_data_structure.htm)
- [A Gentle Introduction to Data Structures: How Graphs Work](https://medium.freecodecamp.org/a-gentle-introduction-to-data-structures-how-graphs-work-a223d9ef8837)
- [Graph Search, Shortest Paths, and Data Structures | Coursera](https://www.coursera.org/learn/algorithms-graphs-data-structures)
