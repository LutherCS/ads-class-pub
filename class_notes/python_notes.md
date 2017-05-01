

```python
exam = {'Alice':90, 'Bob':None, 'Chuck':80, 'Dave':85, 'Eve':None}
```


```python
for name, score in exam.items():
    if score:
        print('{} scored {}'.format(name, score))
    else:
        print('No result for student {}'.format(name))    
```

    No result for student Eve
    No result for student Bob
    Alice scored 90
    Dave scored 85
    Chuck scored 80



```python
for name, score in exam.items():
    if score and score > 80:
        if name == 'Alice':
            print('Alice!!!')
        print('{} scored {}'.format(name, score))
```

    Alice!!!
    Alice scored 90
    Dave scored 85



```python
def cond_1(lst):
    lst[0] = 10
    return sum(lst)
def cond_2(lst):
    lst[0] = 20
    return sum(lst)
```


```python
lst_init = [1, 2, 3]
print(lst_init)
if cond_1(lst_init) > 20 and cond_2(lst_init) > 20:
    print('AND is True')
print(lst_init)
```

    [1, 2, 3]
    [10, 2, 3]



```python
lst_init = [1, 2, 3]
print(lst_init)
if cond_1(lst_init) > 20 or cond_2(lst_init) > 20:
    print('OR is True')
print(lst_init)
```

    [1, 2, 3]
    OR is True
    [20, 2, 3]



```python

```
