print("Hello there!")

from abc import ABC, abstractmethod

class Marker(ABC):
    @abstractmethod
    def __init__(self, color_param, length_param, resource_param=10):
        self._color123 = color_param
        self._length = length_param
        self._resource = resource_param
    
    @property
    def color(self):
        return self._color123

    def get_resource(self):
        return self._resource

    def set_resource(self, new_value):
        self._resource = new_value

    resource = property(get_resource, set_resource)

    def __str__(self):
        return f"This is a {self._color123} marker with the resource of {self._resource}"
    
    def __lt__(self, other):
        return self._resource < other._resource

    def __add__(self, other):
        self._color123 = self.color + "-" + other.color
        return self

    def write(self):
        print(f"Writing in {self.color}")
        self._resource -= 1

class RefillableMarker(Marker):
    def __init__(self, color_param, length_param, size_param, resource_param=10):
        super().__init__(color_param, length_param, resource_param)
        self._size = size_param
    
    def __str__(self):
        return "Refillable!" + super().__str__() + f". It's size is {self._size}"

g_marker = Marker("Red", 2, 20)
print(g_marker)

r_marker = RefillableMarker("Black", 5, "Medium")
print(r_marker)

# a_marker = Marker("Blue", 1)
# print(a_marker)
# b_marker = Marker("Black", 1.5, 7)
# print(b_marker)

# if a_marker < b_marker:
#     print("A is less than B")
# else:
#     print("B is less than A")

# a_marker.write()
# print(a_marker)
# a_marker.write()
# print(a_marker)

# a_marker = a_marker + b_marker
# print(a_marker)

# a_marker._color = "Green"
# print(a_marker)

# print(f"a_marker is {a_marker.color}")
# # a_marker.color = "Red"

# print(f"a_marker has a resource of {a_marker.resource}")
# a_marker.resource = 77
# print(f"After refilling a_marker has a resource of {a_marker.resource}")


