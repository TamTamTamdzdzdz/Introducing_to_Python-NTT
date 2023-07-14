import math


def sin(x):
    bef, aft, n = 0, x, 1
    while abs(aft - bef) >= 10 ** -9:
        bef, aft, n = aft, aft + ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1), n + 1
    return round(aft, 6)


def cos(x):
    bef, aft, n = 0, 1, 1
    while abs(aft - bef) >= 10 ** -9:
        bef, aft, n = aft, aft + ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n), n + 1
    return round(aft, 6)


def exp(x):
    bef, aft, n = 0, 1, 1
    while abs(aft - bef) >= 10 ** -9:
        bef, aft, n = aft, aft + (x ** n) / math.factorial(n), n + 1
    return round(aft, 6)


# def my_sum_sin_cos(n):
#     res = round(0, 6)
#     for i in range(10):
#         res = res + sin(i + 1 + n) + cos(i + 2 + n)
#     return res
