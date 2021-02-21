# some description here

import pandas as pd
import numpy as np

x = np.random.random(10)

print(x)


def pripri(x):
    for i, _ in enumerate(x):
        x[i] = i * x[i]


pripri(x)
print(x)


def sum_array(x):
    return np.sum(x) + 55


print(sum_array(x))

if x == True:
    pass
else:
    print("Error")

