'''Stack as a dictionary'''

#!/usr/bin/env python3


class Stack:
    def __init__(self):
        self.items = {}
        self.top = 0

    def is_empty(self):
        return self.items == {}

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items[self.top] = item
        self.top += 1

    def pop(self):
        boo = self.items.pop(self.top - 1)
        self.top -= 1
        return boo

    def peek(self):
        # if self.top == 0:
        #     raise Exception('Empty Stack')
        # return self.items[self.top-1]

        # try:
        #     return self.items[self.top-1]
        # except:
        #     raise Exception('Empty Stack')

        # if len(self.items) > 0:
        #     return self.items[self.top-1]
        # else:
        #     raise Exception('Empty Stack')

        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            raise Exception('Empty Stack')


def main():
    s = Stack()
    s.push('a')
    print(s.peek())
    # s.push('alice')
    # s.push('bob')
    # while not s.is_empty():
        # print(s.pop())

if __name__ == '__main__':
    main()
