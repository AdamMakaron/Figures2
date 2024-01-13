import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def info(self):
        return f"Triangle with sides {self.a}, {self.b}, and {self.c}, perimeter {self.perimeter()}, area {self.area()}"
