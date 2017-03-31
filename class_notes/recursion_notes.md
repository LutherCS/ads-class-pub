
# Recursion


```python
def my_sum(lst):
    """Sum all the items in a list recursively"""
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        return my_sum(lst[1:]) + lst[0]
```


```python
my_lst = [7, 42, 73]
print(my_sum(my_lst))
```

    122


## Calculating the factorial


```python
def fact_iter(n):
    """Iterative implementations of the factorial"""
    result = 1
    for num in range(1, n+1):
        result *= num
    return result

def fact_rec_simple(n):
    """Simple recursive implementations of the factorial"""
    if n < 2:
        return 1
    else:
        return n * fact_rec_simple(n-1)

known_fact = {}
def fact_rec_memo(n):
    """Recursive implementations of the factorial using memoization"""
    if n < 2:
        return 1
    else:
        if n not in known_fact:
            known_fact[n] = n * fact_rec_memo(n-1)
    return known_fact[n]
    
from functools import lru_cache
@lru_cache(maxsize=None)
def fact_rec_cached(n):
    """Recursive implementations of the factorial using functools"""
    if n < 2:
        return 1
    else:
        return n * fact_rec_cached(n-1)
```


```python
from timeit import timeit
print("|{:^10}|{:^10}|{:^10}|{:^10}|".format("Iterative", "Simple", "Memoized", "Cached"))
print("-"*45)
print("|{:^10}|{:^10}|{:^10}|{:^10}|".format(fact_iter(5), fact_rec_simple(5), fact_rec_memo(5), fact_rec_cached(5)))
print("-"*45)
print("|{:^10.2f}|{:^10.2f}|{:^10.2f}|{:^10.2f}|".format(timeit('fact_iter(5)', number=10, globals=globals()) * 1000000,
                                           timeit('fact_rec_simple(5)', number=10, globals=globals()) * 1000000,
                                           timeit('fact_rec_memo(5)', number=10, globals=globals()) * 1000000,
                                           timeit('fact_rec_cached(5)', number=10, globals=globals()) * 1000000))
print(fact_rec_cached.cache_info())
```

    |Iterative |  Simple  | Memoized |  Cached  |
    ---------------------------------------------
    |   120    |   120    |   120    |   120    |
    ---------------------------------------------
    |  13.24   |  11.75   |   4.54   |   3.07   |
    CacheInfo(hits=112, misses=5, maxsize=None, currsize=5)


## Fibonacci


```python
def fibo_iter(n):
    """Iterative implementations of the Fibonacci"""
    fibo1 = 1
    fibo2 = 1
    result = 1
    for num in range(1, n):
        result = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = result
    return result

def fibo_rec_simple(n):
    """Simple recursive implementations of the Fibonacci"""
    if n < 2:
        return 1
    else:
        return fibo_rec_simple(n-1) + fibo_rec_simple(n-2)

known_fibo = {}
def fibo_rec_memo(n):
    """Recursive implementations of the Fibonacci using memoization"""
    if n < 2:
        return 1
    else:
        if n not in known_fibo:
            known_fibo[n] = fibo_rec_memo(n-1) + fibo_rec_memo(n-2)
    return known_fibo[n]
    
from functools import lru_cache
@lru_cache(maxsize=None)
def fibo_rec_cached(n):
    """Recursive implementations of the Fibonacci using functools"""
    if n < 2:
        return 1
    else:
        return fibo_rec_cached(n-1) + fibo_rec_cached(n-2)
```


```python
n = 10
print("{:^10}|{:^10}|{:^10}|{:^10}".format("Iterative", "Simple", "Memoized", "Cached"))
print("-"*41)
print("{:^10}|{:^10}|{:^10}|{:^10}".format(fibo_iter(n), fibo_rec_simple(n), fibo_rec_memo(n), fibo_rec_cached(n)))

```

    Iterative |  Simple  | Memoized |  Cached  
    -----------------------------------------
        89    |    89    |    89    |    89    



```python

```
