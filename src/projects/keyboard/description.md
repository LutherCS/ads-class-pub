# Touchscreen Keyboard

[Kattis](https://open.kattis.com/problems/touchscreenkeyboard)

Nowadays, people do not use hardware keyboards but touchscreens. Usually, they touch on the wrong letters with their chunky fingers, because screen space is precious and the letters therefore too small.

Usually, a spell checker runs after typing a word and suggests other words to select the correct spelling from. Your job is to order that list so that more likely words are on top.

The typical touchscreen keyboard looks like this:

```text
qwertyuiop
asdfghjkl
zxcvbnm
```

You should use the distance between the letters to type a word: the distance is the sum of the horizontal and vertical distance between the typed and proposed letter. Assume you typed a _w_, the distance to _e_ is 1, while the distance to _z_ is 3.

The typed word and the list of words from the spell checker all have the same length. The distance between two words is the sum of the letter distances. So the distance between _ifpv_ and _icpc_ is 3.

## Input

The first line of the input specifies the number of test cases _t_ (0 < t < 20). Each test case starts with a string and an integer _l_ on one line. The string gives the word that was typed using the touchscreen keyboard, while _l_ specifies the number of entries in the spell checker list (0 < l ≤ 10). Then follow _l_ lines, each with one word of the spell checker list. You may safely assume that all words of one test case have the same length and no word is longer than 10000 characters (only lowercase 'a' - 'z'). Furthermore, each word appears exactly once in the spell checker list on one test case.

## Output

For each test case, print the list of words sorted by their distance ascending. If two words have the same distance, sort them alphabetically. Print the distance of each word in the same line.

### Sample input (data/projects/keyboard/sample.in)

```text
2
ifpv 3
iopc
icpc
gcpc
edc 5
wsx
edc
rfv
plm
qed
```

### Sample output (tests/projects/keyboard/sample.out)

```text
icpc 3
gcpc 7
iopc 7
edc 0
rfv 3
wsx 3
qed 4
plm 17
```

## What to do

`python3` should be `python3.9` or newer.

- Read _src/projects/keyboard/description.md_ (this file).
- Modify _src/projects/keyboard/keyboard.py_.
- Run _src/projects/keyboard/keyboard.py_.

```bash
python3 src/projects/keyboard/keyboard.py
```

- Compare your output to that provided in _tests/projects/keyboard/_.
- Test your implementation.

```bash
python3 -m pytest tests/projects/keyboard/test_keyboard.py
```
