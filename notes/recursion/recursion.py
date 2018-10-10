def some_method(n):
    if n < 1:
        return 0
    else:
        return n + some_method(n - 1)

def some_method_iter(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def list_sum(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        # return lst.pop() + list_sum(lst)
        return lst[0] + list_sum(lst[1:])

def list_sum_2(lst):
    s = 0
    for i in lst:
        s += i
    return s


def main():
    # result = some_method(5)
    # print(result)
    print(list_sum([1, 32, 3, 6]))


if __name__ == '__main__':
    main()
