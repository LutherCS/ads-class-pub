print("Python 3 review")

x = 5
print(x)
print(type(x))
print(f"Variable x is of type {type(x)} and its value is {x}")

even_numbers_up_to_10 = []
for i in range(10):
    if i % 2 == 0:
        even_numbers_up_to_10.append(i)

print(even_numbers_up_to_10)
assert even_numbers_up_to_10 == [0, 2, 4, 6, 8]
print("Well done!")

another_list = [i for i in range(10) if i % 2 == 0]
assert another_list == [0, 2, 4, 6, 8], another_list
print("List comprehension worked!")

set_of_numbers = {i for i in range(10) if i % 2 == 0}
assert set_of_numbers == {0, 2, 4, 6, 8}, set_of_numbers
print("Set comprehension worked!")

