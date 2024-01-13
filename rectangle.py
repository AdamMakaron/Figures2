class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def info(self):
        return f"Rectangle with length {self.length}, width {self.width}, perimeter {self.perimeter()}, area {self.area()}"
