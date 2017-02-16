
# Object-oriented programming #
*In-class code examples*

## Simple Classes ##
Use constructor method __init__ to create a new instance of a class and initialize its data members.

Use "magic" functions __str__, __eq__, etc to specify common behavior.

Use self to access the object itself.

Start a name with a single underscore _ to signify a "private" (not really) member.

If necessary, end method parameters with a single underscore to avoid confusion.


```python
#!/usr/bin/env python3
#encoding: UTF-8

class Student:
    def __init__(self, initial_name):
        self._name = initial_name
        
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name
    
    def __str__(self):
        return 'Hi, I\'m ' + self._name + '!'
    
    def __eq__(self, other):
        return self._name == other.get_name()
        
    def __add__(self, other):
        if isinstance(other, Student):
            return Student(self._name + ' ' + other.get_name())
        else:
            print('hey! don\'t do this!')

```

### Using objects ###
Use getters and setters to access object data members.


```python
s1 = Student('Alice')
print(s1.get_name())
s2 = Student('Charles')
print(s2.get_name())
print(s1, id(s1))
print(s2, id(s2))
if s1 == s2:
    print('they are equal')
else:
    print('something else')
    
print(s1 + s2)
s3 = Student('Doug')
print(s1 + s2 + s3)
```

    Alice
    Charles
    Hi, I'm Alice! 140033085709280
    Hi, I'm Charles! 140033085709448
    something else
    Hi, I'm Alice Charles!
    Hi, I'm Alice Charles Doug!


### Very simple class ###
Very simple constructor demo.


```python
class Wall:
    def __init__(self):
        self.color = 'white'

```


```python
my_front_wall = Wall()
print(my_front_wall.color)
```

    white


## Class with properties ##
Use @property decorator or property function to provide an interface to class members.


```python
class Course:
    def __init__(self, id_, dept_, number_, semester_, year_, section_, title_):
        self._id = id_
        self._dept = dept_
        self._number = number_
        self._semester = semester_
        self._year = year_
        self._section = section_
        self._title = title_
    
    @property
    def semester(self):
        return self._semester
    
    @semester.setter
    def semester(self, new_value):
        if new_value in ['FA', 'JT', 'SP', 'SU']:
            self._semester = new_value
        else:
            raise ValueError('bad value of the semester. Use a valid value')
    
    #semester = property(get_semester, set_semester)
   
    def __str__(self):
        return self._dept + '-' + str(self._number)
```


```python
my_course = Course(123, 'CS', 160, 'SP', 2017, 'A', 'ADS')
print(my_course)

```

    CS-160


## Using exceptions ##
try..except..finally


```python
try:
    print(my_course.get_semester())
except AttributeError as attribute_err:
    print(attribute_err)
```

    'Course' object has no attribute 'get_semester'



```python
try:
    my_course.set_semester('SU')
except AttributeError as attribute_err:
    print(attribute_err)
```

    'Course' object has no attribute 'set_semester'



```python
print(my_course.semester)
```

    SP



```python
print(my_course.semester)
try:
    my_course.semester = 'Hello'
except ValueError as value_err:
    print('there was a problem')
    print(value_err)
finally:
    print(my_course.semester)
```

    SP
    there was a problem
    bad value of the semester. Use a valid value
    SP



```python
import random
for _ in range(5):
    x = random.randint(0, 1)
    try:
        print("1/{} = {}".format(x, 1/int(x)))
    except ZeroDivisionError as zerodiv_err:
        print(zerodiv_err)
print("The program didn't crash!")
```

    division by zero
    1/1 = 1.0
    1/1 = 1.0
    1/1 = 1.0
    division by zero
    The program didn't crash!


## Inheritance ##
Classes can inherit members from other class(es)


```python
import random

class Fruit:
    def __init__(self, color_, price_=0.99):
        self._color = color_
        self._price = price_
    
    def __str__(self):
        return 'costs ' + str(self._price)

class Apple(Fruit):
    def __init__(self, color_, price_, variety_):
        super().__init__(color_, price_)
        self._variety = variety_
    
    def make_a_pie(self):
        return "Tasty pie"
    
    def __str__(self):
        return 'this ' + self._color + ' ' + self._variety + ' apple ' + super().__str__()

class Orange(Fruit):
    def __init__(self, color_, price_, origin_):
        super().__init__(color_, price_)
        self._origin = origin_
        
    def make_juice(self):
        return "Tasty juice"
    
    def __str__(self):
        return 'this ' + self._color + ' ' + self._origin + ' orange ' + super().__str__()
```

### Working with a hierarchy of classes ###


```python
a = Apple('red', .50, 'Honey Crisp')
print(a)
print(a.make_a_pie())
o = Orange('orange', 1.00, 'Iowa')
print(o)
print(o.make_juice())
```

    this red Honey Crisp apple costs 0.5
    Tasty pie
    this orange Iowa orange costs 1.0
    Tasty juice


### Using isinstance() and issubclass() ###


```python
print(type(a))
print(isinstance(a, Apple))
print(issubclass(type(a), Fruit))
```

    <class '__main__.Apple'>
    True
    True

