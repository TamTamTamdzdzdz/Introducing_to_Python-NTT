import math


class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass


class LengthException(Exception):
    pass


class InvalidTriangleException(Exception):
    pass

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
            print(str(type(e)) + ' was raised')

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        a, b, c, s = self.a, self.b, self.c, (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - a) * (s - b)*(s - c))

    def get_height_a(self):
        return float(self.area())*2/self.a

    def get_height_b(self):
        return float(self.area())*2/self.b

    def get_height_c(self):
        return float(self.area())*2/self.c
    
class Rectangle(Figure):
    def __init__(self, width, height):

        try:
            if width >0 and height>0:
                self.width = width
                self.height = height
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):

        return self.width * self.height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

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

rec = Rectangle(-1, 2)
tri = Triangle(3, 4, 7)
