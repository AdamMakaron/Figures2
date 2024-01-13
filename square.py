from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def info(self):
        return f"Square with side length {self.length}, perimeter {self.perimeter()}, area {self.area()}"