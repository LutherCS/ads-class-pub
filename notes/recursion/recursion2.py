def a():
    a()

# a()

def b():
    c()

def c():
    b()

# b()


def sumn(nums: list) -> int:
    if len(nums) == 0:
        return 0
    return nums[0] + sumn(nums[1:])
    # elif len(nums) == 1:
    #     return nums[0]
    # elif len(nums) == 2:
    #     return nums[0] + nums[1]
    # else:
    #     return nums[0] + sumn(nums[1:])

def sumi(nums: list) -> int:
    s = 0
    for i in nums:
        s = s + i
    return s

result = sumn([160, 170, 2, 4])
assert result == 336
print(f"Expected: 336")
print(f"Recursive: {result}")
result = sumi([160, 170, 2, 4])
assert result == 336
print(f"Iterative: {result}")
