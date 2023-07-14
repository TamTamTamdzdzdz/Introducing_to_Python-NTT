import time
import numpy as np


def convert(a):
    return np.apply_along_axis(lambda x: x / x.sum(), 1, a)
    #apply_along_axis là hàm áp dụng 1 hàm bất kì vào trục của ma trận
    #lambda x:x/sum() là chia 1 số cho tổng của hàm
    # 1 là axis là áp dụng theo hàng
    # a là ma trận cần chuyển
print(convert(np.arange(0, 9).reshape(3, 3)))



