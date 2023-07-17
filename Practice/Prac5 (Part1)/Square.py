from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side):

        self.width = side
        self.height = side

        def set_width(self, new_width):
            self.height=new_width
            return super().set_width(new_width)

        def set_height(self, new_height):
            self.width=new_height
            return super().set_height(new_height)

s = Square(4)
s.set_height(5)
print(s.area())
