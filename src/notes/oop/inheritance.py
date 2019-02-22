'''
Examples of inheritance
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    # @abstractmethod
    def __init__(self, legs_init_value):
        self._limbs = legs_init_value
    
    def __str__(self):
        return 'Animal has {} legs'.format(self._limbs)

    def get_legs(self):
        return self._limbs

    def set_legs(self, new_value):
        raise ValueError('Use proper method to grow a leg')
    
    legs = property(get_legs, set_legs)

    def grow_a_limb(self):
        self._limbs = self._limbs + 1

    @abstractmethod
    def eat(self):
        ...


class Deer(Animal):
    def __init__(self):
        super().__init__(4)
    
    def __str__(self):
        return 'Deer has {} legs'.format(self._limbs)

    def eat(self):
        print("Happy deer")


class LegError(Exception):
    def __init__(self, *args, **kwags):
        super().__init__(self, *args, **kwags)

class Snake(Animal):
    def __init__(self):
        super().__init__(0)
    
    def grow_a_limb(self):
        raise LegError("I CANNOT!!!")
    
    def eat(self):
        print("Snake is always unhappy")

def main():
    a = Animal(6)
    print(a)
    a.grow_a_limb()
    print(a)
    d = Deer()
    print(d)
    d.grow_a_limb()
    print(d)
    s = Snake()
    print(s)
    try:
        s.grow_a_limb()
    except:
        pass
    print(s)
    d.eat()
    s.eat()



if __name__ == '__main__':
    main()