#!/usr/bin/env python3


class Student:
    '''Class Student'''
    def __init__(self, some_name: str, year_in_school: str):
        '''Initialize class attributes'''
        self._name = some_name
        self._year = year_in_school
    
    def __str__(self):
        '''Object as a string'''
        return self._name + ' is a ' + self._year + ' student'
    
    def __repr__(self):
        '''Object representation'''
        return('Student({}, {})'.format(self._name, self._year))
    
    def __lt__(self, other):
        '''Object comparison'''
        return self._name < other._name
    
    def __eq__(self, other):
        '''Object equality'''
        return self._year == other._year

    def study(self) -> None:
        '''Method example'''
        print('Go away, I\'m studying!!!')
    
    @classmethod
    def eat(cls) -> None:
        '''Class method example'''
        print('All students are eating now.')

    @property
    def name(self):
        '''name property getter'''
        return self._name
    
    @name.setter
    def name(self, value):
        '''name property setter'''
        self._name = value
    
    def get_year(self):
        '''year property getter'''
        return self._year
    
    def set_year(self, value):
        '''year property setter'''
        self._year = value
    
    year = property(get_year, set_year)

def foo():
    '''Function example'''
    print('Boo!')

def main():
    '''Main function'''
    print('---New objects creation---')
    s1 = Student('Alice', 'Sophomore')
    s2 = Student('Bob', 'First year')
    s3 = Student('Chuck', 'Sophomore')
    roster = [s1, s2, s3]
    print('---Implicit __str__ invocation---')
    for s in sorted(roster):
        print(s)
        s.study()
    print('---Object comparison---')
    if s1 == s2:
        print('{} and {} are equal'.format(s1.name, s2.name))
    else:
        print('{} and {} are NOT equal'.format(s1.name, s2.name))
    if s1 == s3:
        print('{} and {} are equal'.format(s1.name, s3.name))
    else:
        print('{} and {} are NOT equal'.format(s1.name, s3.name))
    print('---Class method invocation---')
    Student.eat()
    print('---Function assignment---')
    print('---CONFUSION ALERT---')
    s1.study()
    s1.study = foo
    s1.study()
    print('---END OF CONFUSION ALERT---')


if __name__ == '__main__':
    main()
