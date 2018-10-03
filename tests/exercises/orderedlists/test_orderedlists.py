'''
Testing the module orderedlists
Karina Hoff, 2018
'''

#!/usr/bin/python3

import random
import pytest
from exercises.orderedlists.orderedlists import Node, OrderedList

class TestOrderedListMethods:
    '''Testing module ordered_list'''

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.nStr = Node('Hello')
        self.nInt = Node(1861)
        self.nFloat = Node(1.8)
        self.nComplex = Node(1.8J)
        self.ord_lst = OrderedList()
        self.ord_lst2 = OrderedList()
        for val in [1, 8, 6, 1, 2, 0, 1, 8]:
            self.ord_lst2.add(val)

    def test_node_init(self):
        '''Test Node __init__ method'''
        assert self.nStr.data
        assert self.nInt.data
        assert self.nFloat.data
        assert self.nComplex.data
        
    def test_node_init_error(self):
        '''Test Node __init__ error'''
        with pytest.raises(Exception) as excinfo:
            _ = Node()  # pylint: disable=no-value-for-parameter
        exception_message = excinfo.value.args[0]
        assert exception_message == "__init__() missing 1 required positional argument: 'init_data'"
        
    def test_node_data_getter(self):
        '''Test Node data property getter'''
        assert self.nStr.data == 'Hello'
        assert isinstance(self.nStr.data, str)

        assert self.nInt.get_data() == 1861
        assert isinstance(self.nInt.get_data(), int)

        assert self.nFloat.get_data() == 1.8
        assert isinstance(self.nFloat.get_data(), float)

        assert self.nComplex.get_data() == 1.8J
        assert isinstance(self.nComplex.get_data(), complex)

    def test_node_data_setter(self):
        '''Test Node data property setter'''
        self.nStr.set_data('Goodbye')
        assert self.nStr.get_data() == 'Goodbye'
        assert isinstance(self.nStr.get_data(), str)

        self.nInt.set_data(2018)
        assert self.nInt.get_data() == 2018
        assert isinstance(self.nInt.get_data(), int)

        self.nFloat.set_data(3.2)
        assert self.nFloat.get_data() == 3.2
        assert isinstance(self.nFloat.get_data(), float)

        self.nComplex.set_data(3.2J)
        assert self.nComplex.get_data() == 3.2J
        assert isinstance(self.nComplex.get_data(), complex)

    def test_node_data_setter2(self):
        '''Test Node data setter'''
        self.nStr.set_data(2018)
        assert self.nStr.get_data() == 2018
        assert isinstance(self.nStr.get_data(), int)

        self.nInt.set_data(3.2)
        assert self.nInt.get_data() == 3.2
        assert isinstance(self.nInt.get_data(), float)    

        self.nFloat.set_data(3.2J)
        assert self.nFloat.get_data() == 3.2J
        assert isinstance(self.nFloat.get_data(), complex)

        self.nComplex.set_data('Luther')
        assert self.nComplex.get_data() == 'Luther'
        assert isinstance(self.nComplex.get_data(), str)        

    def test_node_next_getter(self):
        '''Test Node next property getter'''
        for node in [self.nStr, self.nInt, self.nFloat, self.nComplex]:
            assert node.next == None

    def test_node_next_setter(self):
        '''Test Node next property setter'''
        self.nStr.next = self.nInt
        assert self.nStr.next == self.nInt

    def test_node_str(self):
        '''Test Node __str__ method'''
        assert str(self.nStr) == 'Hello'
        assert str(self.nInt) == '1861'
        assert str(self.nFloat) == '1.8'
        assert str(self.nComplex) == '1.8j'

    def test_OrderedList_getitem(self):
        '''Test OrderedList __getitem__ method'''
        self.ord_lst.append('boo')
        self.ord_lst.append('foo')
        self.ord_lst.append('buzz')
        assert self.ord_lst[1] == 'buzz'

    def test_OrderedList_getitem_error(self):
        '''Test OrderedList __getitem__ error'''
        with pytest.raises(Exception) as excinfo:
            self.ord_lst.__getitem__()  # pylint: disable=no-value-for-parameter
        exception_message = excinfo.value.args[0]
        assert exception_message == "__getitem__() missing 1 required positional argument: 'position'"        

        with pytest.raises(Exception) as excinfo:
            self.ord_lst.__getitem__(0)
        exception_message = excinfo.value.args[0]
        assert exception_message == "The list is empty"

    def test_OrderedList_len(self):
        '''Test OrderedList __len__'''
        assert len(self.ord_lst) == 0
        assert len(self.ord_lst2) == 8

    def test_OrderedList_str(self):
        '''Test OrderedList __str__'''
        assert str(self.ord_lst) == '[]'
        assert str(self.ord_lst2) == '[0, 1, 1, 1, 2, 6, 8, 8]'

    def test_OrderedList_is_empty(self):
        '''Test OrderedList is_empty method'''
        assert self.ord_lst.is_empty()
        assert not self.ord_lst2.is_empty()

    def test_OrderedList_size(self):
        '''Test OrderedList size method'''
        assert self.ord_lst.size() == 0
        assert self.ord_lst2.size() == 8

    def test_OrderedList_add(self):
        '''Test OrderedList add method'''
        for val in [1, 8, 6, 1, 2, 0, 1, 8]:
            self.ord_lst.add(val)
        assert len(self.ord_lst) == 8
        assert str(self.ord_lst) == '[0, 1, 1, 1, 2, 6, 8, 8]'
        assert not self.ord_lst.is_empty()
        assert self.ord_lst.size() == 8

    def test_OrderedList_append(self):
        '''Test OrderedList append method'''
        for val in [1, 8, 6, 1, 2, 0, 1, 8]:
            self.ord_lst.append(val)
        assert len(self.ord_lst) == 8
        assert str(self.ord_lst) == '[0, 1, 1, 1, 2, 6, 8, 8]'
        assert not self.ord_lst.is_empty()
        assert self.ord_lst.size() == 8

    def test_OrderedList_insert(self):
        '''Test OrderedList insert method'''
        for val in [1, 8, 6, 1, 2, 0, 1, 8]:
            self.ord_lst.insert(random.randint(0, len(self.ord_lst)), val)
        assert len(self.ord_lst) == 8
        assert str(self.ord_lst) == '[0, 1, 1, 1, 2, 6, 8, 8]'
        assert not self.ord_lst.is_empty()
        assert self.ord_lst.size() == 8

    def test_OrderedList_pop(self):
        '''Test OrderedList pop method'''
        popped_vals = []
        for _ in range(4):
            popped_vals.append(self.ord_lst2.pop())
        assert popped_vals == [8, 8, 6, 2]
        assert len(self.ord_lst2) == 4
        assert str(self.ord_lst2) == '[0, 1, 1, 1]'
        assert not self.ord_lst2.is_empty()
        assert self.ord_lst2.size() == 4

    def test_OrderedList_search(self):
        '''Test OrderedList search method'''
        assert not self.ord_lst.search(0)
        assert self.ord_lst2.search(0)
        assert self.ord_lst2.search(1)
        assert not self.ord_lst2.search(23)

    def test_OrderedList_index(self):
        '''Test OrderedList index method'''
        assert self.ord_lst.index(0) == -1
        assert self.ord_lst2.index(0) == 0
        assert self.ord_lst.index(23) == -1

       
if __name__ == '__main__':
    pytest.main(['test_orderedlists.py'])
