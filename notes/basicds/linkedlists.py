class Node:
    def __init__(self, init_value):
        self._value = init_value
        self._next = None
    
    def get_data(self):
        return self._value

    def set_data(self, new_data):
        self._value = new_data
    
    data = property(get_data, set_data)
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, new_next):
        self._next = new_next

    def __str__(self):
        return str(self._value)

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def is_empty(self) -> bool:
        return self._head is None
    
    def size(self) -> int:
        return self._size
    
    def add(self, new_node: object) -> None:
        if not self._head:
            self._head = new_node
        else:
            raise NotImplementedError
    
    def __str__(self):
        my_list = ''
        current = self._head
        while current:
            my_list += current.data
            current = current.next
        
        return my_list


def main():
    print('Working with nodes')
    n = Node('A')
    print(n.data)
    print(n.next)
    print(n)

    m = Node('B')
    n.next = m
    print(n.next)

    print('Working with lists')
    ll = LinkedList()
    print(ll.size())
    print(type(ll))
    print('Printing a list')
    print(ll)
    ll.add(Node('A'))
    print(ll)



if __name__ == '__main__':
    main()