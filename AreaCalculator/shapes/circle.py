import math
from .shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

