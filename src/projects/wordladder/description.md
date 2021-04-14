# Word Ladders

Complete the following programming project.

## Task

Create word ladders. The user will type in (or hard-code) a beginning and an ending word. Your program must find the series of words that differ by only a single letter that leads from the beginning word to the ending word. For example, to turn the word _stone_ into _water_, one series of words is:

```text
stone
shone
shine
shins
shies
shyer
sayer
hayer
hater
water
```

## Algorithm

We will use an algorithm that employs both a `Stack` and a `Queue`. You may use those data structures explicitly or mimic their functionality using Python's `deque`. Here's how the algorithm works:

1. Add the starting word to a set of used words.

2. Get the starting word and search through the source of new words to find all words that are one letter different and have not already been used. For example, suppose the current word is _bend_. Words _send_ and _band_ would qualify because they would have the same letters in 3 of the four places if only one letter is changed. The word _ends_ would not qualify even though it has three letters that are the same, but they are in different positions.

3. Create a `stack` for each pair of words containing the starting word (pushed first) and the word that is one letter different (pushed on top).

4. Add these new words to your set of used words so you don't use them again.

5. Enqueue each of these stacks into a `queue`. You have created a queue of stacks!

6. Now dequeue the first stack from the queue, look at its top word and compare it with the ending word. If they are equal, then you are done and this stack represents the word ladder. Otherwise, find all the unused words that are one letter different from the word on top of the stack. For each of these words do the following:

   1. Make a clone of the current stack and push this word onto the clone.
   2. Add the new words to the set of used words.
   3. Enqueue this new stack

Make sure that you don't re-use any words or you will create an infinite loop.

The attached input dictionary is simply a text file with 12,000 words. You will need to read this file of words and organize it into three structures, one of three-letter words, one of four-letter words, and one of five-letter words.

## Approach

1. Implement the functionality as methods of the class `Solver`.
2. Initialize an object of class `Solver` by reading the words from the provided file (e.g. _words.txt_) and putting them into a corresponding set.
3. Method `distance` takes two words and returns the number of different letters in the corresponding positions.
   - `distance("abc", "abd")` should return 1 ("c" and "d" are different)
   - `distance("cbc", "abd")` should return 2 (only "b" is the same).
4. Method `diff_by_one` takes a particular word, the set of words of the same length, and the set of _used_ words (those should not be considered to avoid infinite loop). This methid returns a list of all possible candidate words (i.e. distance from the current word is `1`) that have not been used yet.
5. Build the word ladder solution using all of the parts above.

Whether you are using a `Stack` or a `deque` object, make sure you are creating a deep copy (clone) of those objects and not shallow copies. A properly created `clone` is a brand new stack, with the same set of words pushed onto the new stack in the same order as the stack you are cloning. Many people get this wrong by making a new stack but using something like `newstack.items = self.items`. This statement makes the items of the `newstack` reference the same list as the current stack, which means that if you push something on to `newstack` it will also be pushed onto the old stack as well.

## What to do

`python3` should be `python3.9` or newer.

- Read _src/projects/wordladder/description.md_ (this file).
- Modify _src/projects/wordladder/wordladder.py_.
- Run _src/projects/wordladder/wordladder_main.py_.

```bash
python3 src/projects/wordladder/wordladder_main.py
```

- Compare your output to that provided in _tests/projects/wordladder/wordladder_output.txt_.
- _tests/projects/wordladder/wordladder_output_debug.txt_ shows some intermediate steps when turning _stone_ into _water_.
- Test your implementation.

```bash
python3 -m pytest tests/projects/wordladder/test_wordladder.py
```
