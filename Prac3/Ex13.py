import math
def euclidian_distance(v1: list, v2: list):
    res = 0
    for i in range(len(v1)):
        res += (v1[i] - v2[i]) ** 2
    return res ** 0.5

def manhattan_distance(v1: list, v2: list):
    res = 0
    for i in range(len(v1)):
        res += abs(v1[i] - v2[i])
    return res
def cosine_distance(v1: list, v2: list):
    res = 0
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for i in range(len(v1)):
        numerator += v1[i] * v2[i]
        denominator1 += v1[i] ** 2
        denominator2 += v2[i] ** 2
    res = numerator / (denominator1 ** 0.5 * denominator2 ** 0.5)
    return res
def vector_distance(v1, v2, **kwargs):
    # for value in kwargs.values():
    # kwargs[norm]=kwargs.get(norm,'euclidian')
    value=kwargs.get('norm','euclidian')
    if value == 'manhattan':
        return round(manhattan_distance(v1, v2),9)
    elif value== 'cosine':
        return round(cosine_distance(v1, v2),9)
    else:

        return round(euclidian_distance(v1, v2),9)



print(vector_distance([1, 2], [4, 6]))

print(vector_distance([1, 2], [4, 6], norm='manhattan'))
print(vector_distance([1, 2], [4, 6], norm='cosine'))