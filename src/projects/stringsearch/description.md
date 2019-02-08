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

## How to submit your solution

- Submit your modified `nonrepeat.py` to KATIE.
    - There is no need to submit data and test files, I already have them.
