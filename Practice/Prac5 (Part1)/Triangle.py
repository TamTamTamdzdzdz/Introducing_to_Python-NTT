from Figure import *
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        try:
            if a<=0 or b<=0 or c<=0:
                raise LengthException
            elif a+b<=c or b+c<=a or c+a<=b:
                raise InvalidTriangleException
            else:
                self.a = a
                self.b = b
                self.c = c
        except LengthException as e:
            print(str(type(e)) + ' was raised')
        except InvalidTriangleException as e:
            print(print(str(type(e)) + ' was raised'))

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        a, b, c, s = self.a, self.b, self.c, (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - a) * (s - b)*(s - c))

    def get_height_a(self):
        return self.a

    def get_height_b(self):
        return self.b

    def get_height_c(self):
        return self.c

