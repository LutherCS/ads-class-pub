print("Hello there!")

class Marker:
    def __init__(self, color_param, length_param, resource_param=10):
        self._color = color_param
        self._length = length_param
        self._resource = resource_param
    
    def __str__(self):
        return f"This is a {self._color} marker with the resource of {self._resource}"
    
    def __lt__(self, other):
        return self._resource < other._resource

    def __add__(self, other):
        self._color = self._color + "-" + other._color
        return self

    def write(self):
        print(f"Writing in {self._color}")
        self._resource -= 1
    
a_marker = Marker("Blue", 1)
print(a_marker)
b_marker = Marker("Black", 1.5, 7)
print(b_marker)

if a_marker < b_marker:
    print("A is less than B")
else:
    print("B is less than A")

a_marker.write()
print(a_marker)
a_marker.write()
print(a_marker)

a_marker = a_marker + b_marker
print(a_marker)

