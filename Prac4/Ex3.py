import time

import numpy as np


def system_solver(a):
    b = np.array(a)
    return np.reshape((np.linalg.solve(b[:, :-1], b[:, -1])), (len(a), 1))

bef=time.time()
print(system_solver([[1,  3, -2,  5], [3,  5,  6,  7], [2,  4,  3,  8]]))
aft=time.time()
print(aft-bef)
