import numpy as np


def system_solver(a):
    b = np.array(a)
    # hàm linalg.solve là hàm giải hệ phương trình
    # b[:,:-1] là ma trận A, b[:,-1] là ma trận b với a là ma trận [A|b]
    return np.reshape((np.linalg.solve(b[:, :-1], b[:, -1])), (len(a), 1))

a = np.array([[1, 3, -2, 5],
	          [3, 5, 6, 7],
	          [2, 4, 3, 8]])
print(system_solver(a))

