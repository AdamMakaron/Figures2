import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

    def info(self):
        return f"Circle with radius {self.radius}, perimeter {self.perimeter()}, area {self.area()}"
