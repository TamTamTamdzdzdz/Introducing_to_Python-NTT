from Figure import *


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


