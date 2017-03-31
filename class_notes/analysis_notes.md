
# Algorithm Analysis #


```python
%matplotlib inline
import matplotlib.pyplot as plt
import time
import random
#timelist = []
#sizes = list(range(1000, 10000, 100))
```


```python
sum = 0
t = time.process_time()
for i in range(1000):
    sum = sum + 1
for j in range(1000):
    sum = sum + 1
elapsed_time = time.process_time() - t
print('elapsed time is {}'.format(elapsed_time))
#plt.plot(sizes[:len(timelist)], timelist)
```

    elapsed time is 0.0008111300000024357



```python
sum = 0
t = time.process_time()
for i in range(1000):
    for j in range(1000):
        sum = sum + 1
elapsed_time = time.process_time() - t
print('elapsed time is {}'.format(elapsed_time))
#plt.plot(sizes[:len(timelist)], timelist)
```

    elapsed time is 0.12662281700001188



```python
sum = 0
t = time.process_time()
x = 1
y = 2
z = 3
for i in range(1000000):
    sum = sum + 1
elapsed_time = time.process_time() - t
print('elapsed time is {}'.format(elapsed_time))
```

    elapsed time is 0.14170022000001836



```python
sum = 0
t = time.process_time()
x = 1
for i in range(1000000):
    sum = sum + 1
elapsed_time = time.process_time() - t
print('elapsed time is {}'.format(elapsed_time))
```

    elapsed time is 0.13875273300004665



```python

```
