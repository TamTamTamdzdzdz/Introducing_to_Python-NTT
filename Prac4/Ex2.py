import time
import numpy as np


def convert(a):
    return np.apply_along_axis(lambda x: x / x.sum(), 1, a)


bef = time.time()
print(convert(np.arange(0, 9).reshape(3, 3)))
aft = time.time()
print(aft-bef)
