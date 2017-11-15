'''Build a ladder of words using stacks and queues'''
#!/usr/bin/env python3

WORDS_OF_3 = set()
WORDS_OF_4 = set()
WORDS_OF_5 = set()


class Stack:
    '''Implementing Stack ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''Is stack empty?'''
        return self.items == []
    def size(self):
        '''Return stack size'''
        return len(self.items)
    def push(self, item):
        '''Add new item to stack'''
        self.items.append(item)
    def pop(self):
        '''Remove an item from stack'''
        return self.items.pop()
    def peek(self):
        '''Look at the top item'''
        return self.items[-1]
    def copy(self):
        '''Cloning a stack'''
        stack_clone = Stack()
        stack_clone.items = self.items[:]
        return stack_clone


class Queue:
    '''Implementing Queue ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''is the Queue empty'''
        return self.items == []
    def enqueue(self, item):
        '''Add an item'''
        self.items.insert(0, item)
    def dequeue(self):
        '''Remove an item'''
        return self.items.pop()
    def size(self):
        '''How big is it?'''
        return len(self.items)

def read_file(filename):
    '''Read a file into 3 sets'''
    ''' TODO: Populate sets WORDS_OF_#, WORDS_OF4, and WORDS_OF_5'''
    raise NotImplementedError

def diff_by_one(word1, word2):
    '''Differences between words'''
    ''' TODO: Return true if word1 and word differ by 1 letter'''
    raise NotImplementedError

def diff_by_one_all(word, all_words, used_words):
    '''Find all words that differ by 1 letter'''
    ''' TODO: Return a list of words from all_words that differ from word by 1 letter and have not been used yet'''
    raise NotImplementedError

def main():
    '''Main function'''
    ''' TODO: Read file words.txt into 3 sets'''

    word_start = 'stone'
    word_stop = 'water'
    ''' TODO: Check if words are of the same length. If they are, use a proper set, else raise an exception'''

    print("Let's turn '%s' into '%s'" % (word_start, word_stop))
    ''' TODO: Initialize the set of used words. It should contain the starting word to begin with'''
    ''' TODO: Create a new empty stack and add the start word to it'''
    ''' TODO: Create a new empty queue and add the initial stack to it'''
    found = False

    ''' TODO: Implement the algorithm
        1. Deque a stack from the queue
        2. Find all candidate words (similar to the stack top word)
        3. Clone (copy) current stack and add a candidate word to it
        4. Add the candidate word to a list of used words
        5. Enqueue the resulting stack
        6. Continue until one of the candidate words is the target or the queue becomes empty
    '''

    if found:
        print('Ladder found!')
        ''' TODO: Print the ladder'''
    else:
        print('Ladder not found')

if __name__ == '__main__':
    main()
