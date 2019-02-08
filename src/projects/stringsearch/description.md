# Where is this snowflake?

Write a program to find the first non-repeated character in a string.


## How to setup your development environment

- Make sure you are using **python3** (at least 3.6 is available on all major platforms)
- Install VisualStudioCode (other IDEs are fine too)
- Modify the file `nonrepeat.py` in *src/projects/stringsearch/* and add your code there.
    - **Current implementation is slow and incorrect!**

- `__init__.py` turns `stringsearch` into a module and allows other programs and modules to import from it. The provided file should be sufficient.
- Install *pylint*, *black*, *mypy*, *pytest*

    - Windows (Python installed from the App Store)
    ```
    python3 -m pip install pylint, black, mypy, pytest
    ```

    - Windows (Python installed from the downloaded executable)
    ```
    py -3 -m pip install pylint, black, mypy, pytest
    ```

    - Linux (install for the current user)
    ```
    python3 -m pip install --user pylint, black, mypy, pytest
    ```

    - Linux (install for all users)
    ```
    sudo python3 -m pip install pylint, black, mypy, pytest
    ```


## How to format, run, and test your solution

- `black`
```
python3 -m black src/projects/stringsearch/nonrepeat.py
```

- `pylint`
```
python3 -m pylint src/projects/stringsearch/nonrepeat.py
```

- `mypy`
```
python3 -m mypy src/projects/stringsearch/nonrepeat.py
```

- `pytest`
```
python3 -m pytest tests/projects/stringsearch/test_nonrepeat.py
```

- Use terminal to run
```
python3 src/projects/stringsearch/nonrepeat.py
```
 
You may have to use the following command on Windows:

```
py -3 src/projects/stringsearch/nonrepeat.py
```

## How to submit your solution

- Submit your modified `nonrepeat.py` to KATIE.
    - There is no need to submit data and test files, I already have them.


## References

- [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
- [Pylint - code analysis for Python | www.pylint.org](https://www.pylint.org/)
- [pylint | Read the Docs](https://readthedocs.org/projects/pylint/)
- [Consistent Python code with Black · Matt Layman](https://www.mattlayman.com/blog/2018/python-code-black/)
- [The uncompromising code formatter — Black 18.9b0 documentation](https://black.readthedocs.io/en/stable/)
- [mypy - Optional Static Typing for Python](http://mypy-lang.org/)
- [Welcome to Mypy documentation! — Mypy 0.670+dev.054da214f13248952e294e4a19485367fb0f7420.dirty documentation](https://mypy.readthedocs.io/en/latest/)
- [pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/latest/)
- [Basic Linux Commands for Beginners | Linux | Maker Pro](https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners)
- [https://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html](https://www.cs.princeton.edu/courses/archive/spr05/cos126/cmd-prompt.html)
- [Git Tutorials and Training | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials)
