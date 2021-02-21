# some description here

from numpy.core.defchararray import array
import pandas as pd
import numpy as np

x = np.random.random(10)

print(x)


def pripri(x: array):
    for i, _ in enumerate(x):
        print(i, x[i])


pripri(x)
