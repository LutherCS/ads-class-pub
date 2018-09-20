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
    return self.items[self.top]

def main():
    s = Stack()
    s.push('alice')
    s.push('bob')
    while not s.is_empty():
        print(s.pop())

if __name__ == '__main__':
    main()
