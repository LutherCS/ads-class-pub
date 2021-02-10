"""https://twitter.com/Al_Grigor/status/1357028887209902088"""


the_data = "aaaabbbcca"
expected = [("a", 4), ("b", 3), ("c", 2), ("a", 1)]

from timeit import timeit
from datetime import datetime

def solve1(data):
    return [("a", 4), ("b", 3), ("c", 2), ("a", 1)]

start = datetime.now()
print(solve1(the_data))
stop = datetime.now()
assert solve1(the_data) == expected
print(f"Found the solution in {stop - start} us")
# print(f"Solved in {timeit(f'the_data'), setup='from __main__ import the_data, solve1'):3f} us")
print("You did it!!!!")

def solve2(data):
    character = data[0]
    c_count = 1
    result = []
    for c_next in data[1:]:
        if character == c_next:
            c_count = c_count + 1
        else:
            result.append((character, c_count))
            c_count = 1
            character = c_next
    result.append((character, c_count))
    return result


print(solve1(the_data))
stop = datetime.now()
assert solve2(the_data) == expected, solve2(the_data)
print(f"Found the solution in {stop - start} us")
print("You did it again!!!!")

from itertools import groupby
def solve3(data):
    result = []
    for character, obj in groupby(data):
        result.append((character, len(list(obj))))
    return result

print(solve3(the_data))
stop = datetime.now()
assert solve3(the_data) == expected, solve3(the_data)
print(f"Found the solution in {stop - start} us")
print("You did it again and again!!!!")