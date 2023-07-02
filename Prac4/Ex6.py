import trig
import math

n=int(input())
def my_sum_sin_cos(n):
    res=0
    for i in range(10):
        res+=trig.sin(n+2*i+1)+trig.cos(n+2*i+2)

    return res






def math_sum_sin_cos(n):
    res = 0
    for i in range(10):
        res += round(math.sin(n + 2*i+1),6)+round(math.cos(n+2*i+2),6)
    return res


print(
    f"{'Your own implementation:':<29}{round(my_sum_sin_cos(n),6):>4}",
    f"\n{'Math module implementation:':<29}{round(math_sum_sin_cos(n),6):>4}",
)