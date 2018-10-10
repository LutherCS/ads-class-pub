'''Recursion exercise code template'''

#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    if not b:
        return a
    return gcd(b, a % b)

def hourglass_ite(levels: int) -> None:
    for l in range(levels - 1, -1, -1):
        print('{:^{}}'.format('*' * (2 * l + 1), 2 * (levels - 1) + 1))
    for l in range(1, levels):
        print('{:^{}}'.format('*' * (2 * l + 1), 2 * (levels - 1) + 1))

def diamond_ite(levels: int) -> None:
    for l in range(levels - 1):
        print('{:^{}}'.format('*' * (2 * l + 1), 2 * (levels - 1) + 1))
    for l in range(levels - 1, -1, -1):
        print('{:^{}}'.format('*' * (2 * l + 1), 2 * (levels - 1) + 1))

def tree_11(level:int, levels: int) -> None:
    if level == levels:
        return
    print('{:^{}}'.format('*' * (2 * level + 1), 2 * (levels-1) + 1))
    tree_11(level + 1, levels)

def tree_21(level:int, levels: int) -> None:
    if level < 1:
        return
    print('{:^{}}'.format('*' * (2 * level + 1), 2 * (levels - 1) + 1))
    tree_21(level - 1, levels)

def tree_12(level:int, levels: int) -> None:
    if level == levels - 1:
        return
    print('{:^{}}'.format('*' * (2 * level + 1), 2 * (levels - 1) + 1))
    tree_12(level + 1, levels)

def tree_22(level:int, levels: int) -> None:
    if level < 1:
        return
    print('{:^{}}'.format('*' * (2 * (level - 1) + 1), 2 * (levels - 1) + 1))
    tree_22(level - 1, levels)

def hourglass_rec(levels: int) -> None:
    tree_21(levels-1, levels)
    print('{:^{}}'.format('*', 2 * (levels - 1) + 1))
    tree_11(1, levels)

def diamond_rec(levels: int) -> None:
    tree_12(0, levels)
    print('{:^{}}'.format('*' * (2 * (levels - 1) + 1), 2 * (levels - 1) + 1))
    tree_22(levels-1, levels)

def diamond_rec_2(levels: int) -> None:
    tree_11(0, levels)
    tree_21(levels-1, levels)


def main():
    '''Main function'''
    print('Hourglass (iterative)')
    hourglass_ite(5)
    print('Hourglass (recursive)')
    hourglass_rec(5)
    print('Diamond (iterative)')
    diamond_ite(5)
    print('Diamond (recursive)')
    diamond_rec(5)

if __name__ == '__main__':
    main()
