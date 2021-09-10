print("Using tuple")
t_cat  = (4, False, True, 'orange')
print(f"This {t_cat[3]} cat has {t_cat[0]} legs")

print("Using namedtuple")
from collections import namedtuple

Cat = namedtuple("Cat", ["legs", "hair", "claws", "color"])
b_cat = Cat(legs=4, hair=True, claws=True, color="blue")
print(f"This {b_cat.color} cat has {b_cat.legs} legs")
c_cat = Cat(5, True, True, "white")
print(f"This {c_cat.color} cat has {c_cat.legs} legs")

print("Using dictionary")
d_cat = {"legs": 2, "hair": True, "claws": False, "color": "purple"}
print(f"This {d_cat['color']} cat has {d_cat['legs']} legs")

print("Using dataclass")
from dataclasses import dataclass

@dataclass
class Cat:
    legs: int
    hair: bool
    claws: bool
    color: str

e_cat = Cat(4, False, True, "calico")
print(f"This {e_cat.color} cat has {e_cat.legs} legs")
print(e_cat)
f_cat = Cat(4, False, True, "calico")
if e_cat == f_cat:
    print("SAME!")
else:
    print("different")

print("Using class")
class Cat:
    def __init__(self, legs_init:int=4, color_init:str=None) -> None:
        self.legs = legs_init
        self.hair = True
        self.claws = True
        if color_init:
            self.color = color_init
        else:
            raise ValueError("WHAT IS THE COLOR?!?!?!?!?")
    
    def sleep(self):
        print("I'm dreaming. Go away!")
    
    def noise(self, some_noise):
        if self.claws:
            return some_noise
        return "Brrrr"
    
    def __str__(self) -> str:
        return f"This {self.color} cat has {self.legs} legs"
    
    def __add__(self, other):
        return Cat(self.legs + other.legs, self.color + "-" + other.color)
        # return Cat(max(self.legs, other.legs), "black")

    def __repr__(self) -> str:
        return f"Cat({self.legs}, {self.color})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Cat):
            raise TypeError("Can only compare cats and other cats")
        return self.legs == o.legs
    
    def __lt__(self, o: object) -> bool:
        return self.legs < o.legs

class Dog:
    def __init__(self, name:str) -> None:
        self._name = name
        self._legs = 4
    
    @property
    def legs(self):
        return self._legs

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name
    
    name = property(get_name, set_name)

    def rename(self, new_name):
        self._name = new_name
    def __str__(self) -> str:
        return f"{self._name} has {self._legs} legs"


a_cat = Cat(4, "white")
b_cat = Cat(4, "black")

if a_cat == b_cat:
    print("SAME!")
else:
    print("different")


a_dog = Dog("Max")

# if a_cat == a_dog:
#     print("WHAAAATTTT?")
# else:
#     print("cats and dogs")
print(a_dog.__dict__)
print(a_dog)

a_dog.rename("Peanuts")
# a_dog.legs = 12
print(a_dog.legs)
print(a_dog.name)
a_dog.name = "Max"
print(a_dog.name)


t_cat = Cat(3, 'green')
# print(t_cat)
b_cat = Cat(4, 'yellow')
# print(b_cat)
c_cat = t_cat + b_cat
print(c_cat)

clowder = [t_cat, b_cat, c_cat]

print("Printing a bunch of cat")
print(clowder)
print([str(c) for c in clowder])

a_cat.sleep()
print(a_cat.noise("Purrrrr"))

another_cat = Cat(color_init='black', legs_init=4)
print(type(a_cat))

print(a_cat)
print(f"This {a_cat.color} cat has {a_cat.legs} legs")

print(another_cat)
print(f"This {another_cat.color} cat has {another_cat.legs} legs")

if a_cat == another_cat:
    print("SAME!")
else:
    print("different")