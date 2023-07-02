from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side):

        self.width = side
        self.height = side

temp = Square(4)
print(temp.area())
