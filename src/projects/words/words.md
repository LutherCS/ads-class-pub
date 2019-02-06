## Word Ladders

Complete the following programming project and submit your source code (as a single archive file) to KATIE.

## Task

Create word ladders. The user will type in (or hard-code) a beginning and an ending word. Your program must find the series of words that differ by only a single letter that leads from the beginning word to the ending word. For example, to turn the word STONE into WATER, one series of words is:

```
STONE
SHONE
SHINE
SHINS
SHIES
SHYER
SAYER
HAYER
HATER
WATER
```

## Algorithm

We will use an algorithm that employs both a `Stack` and a `Queue`. Here's how the algorithm works:

1. Add the starting word to a set of used words.

2. Get the starting word and search through the source of new words to find all words that are one letter different and have not already been used. For example, suppose the current word is **bend**. Words **send** and **band** would qualify because they would have the same letters in 3 of the four places if only one letter is changed. The word **ends** would not qualify even though it has three letters that are the same, but they are in different positions.

3. Create `stacks` for each pair of words containing the starting word (pushed first) and the word that is one letter different (pushed on top).

4. Add these new words to your set of used words so you don't use them again.

5. Enqueue each of these stacks into a `queue`. You now have created a queue of stacks!

6. Now dequeue the first stack from the queue, look at its top word and compare it with the ending word. If they are equal, then you are done and this stack represents the word ladder. Otherwise, find all the unused words that are one letter different from the word on top of the stack. For each of these words do the following:

    1. Make a clone of the current stack and push this word onto the clone.
    2. Add the new words to the set of used words.
    3. Enqueue this new stack

Make sure that you don't re-use any words or you will create an infinite loop.

The attached input dictionary is simply a text file with 12,000 words. You will need to read this file of words and organize it into three structures, one of three letter words, one of four letter words, and one of five letter words.

## Approach

1. Write a function that reads the *words.txt* file and creates three sets of words.

2. Write a function that takes a particular word and the set of words that are the same length. This function should return all words that differ by one letter.

3. Implement the `Stack` and `Queue` classes as we have done in class, or follow the book. Implement a `clone` method for your `Stack` class. It is really important to get the `clone` method right. A correct `clone` method will create a brand new stack, with the same set of words pushed onto the new stack in the same order as the stack you are cloning. Many people get this wrong by making a new stack but using something like `newstack.items = self.items`. This statement makes the items of the `newstack` reference the same list as the current stack, which means that if you push something on to `newstack` it will also be pushed onto the old stack as well.

4. Implement the word ladder solution using all of the parts above.

## Functions

* `read_file(filename: str) -> dict`: reads a file of words (default */data/projects/words/words.txt*) and adds them to a proper set. Returns a dictionary with word length as a key and the respective set size as a value.

* `distance(word1: str, word2: str) -> int`: takes two words as arguments and returns the distance between them. The distance is calculated as follows: if two words have different letters in the same position, increment difference by 1.

* `diff_by_one_all(word: str, all_words: set, used_words: set) -> list`: takes the current word, a set of all words, and a set of used words. Returns a list of all possible candidate words (i.e. distance from the current word is **1**) that have not been used yet.

## Grading

1. Read the words from a file into 3 sets.
2. The Stack `clone` method is implemented.
3. Stack class is used properly.
4. Queue class is used properly.
5. A function finding all similar words is implemented properly.
6. The algorithm is implemented correctly.
7. The algorithm is implemented correctly (this is an important task, so I counted it twice).
8. The algorithm is implemented correctly (this is an important task, so I counted it thrice).
9. The word ladder is printed.
10. Pass all tests.