'''
Examples of inheritance
'''

class Animal:
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


class Deer(Animal):
    def __init__(self):
        super().__init__(4)
    
    def __str__(self):
        return 'Deer has {} legs'.format(self._limbs)


def main():
    a = Animal(6)
    print(a)
    a.grow_a_limb()
    print(a)
    d = Deer()
    print(d)
    d.grow_a_limb()
    print(d)


if __name__ == '__main__':
    main()