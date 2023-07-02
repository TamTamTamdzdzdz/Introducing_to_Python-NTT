from Figure import *
import math


class Circle(Figure):
    def __init__(self, radius):
        try:
            if radius > 0:
                self.radius=radius
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')


    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

