#! /usr/env/bin python3


class Stack:
    def __init__(self):
        self.items = {}

    def is_empty(self):
        return self.items == {}

    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def push(self, item):
        top = len(self.items)
        self.items[top] = item

    def pop(self):
        top = len(self.items)
        return self.items.pop(top - 1)

    def peek(self):
        top = len(self.items)
        return self.items.get(top - 1)


def main():
    s = Stack()
    s.push("a")
    print(s.peek())
    s.push("b")
    print(len(s))
    print(s.pop())
    print(s.is_empty())
    print(s.size())


if __name__ == "__main__":
    main()
