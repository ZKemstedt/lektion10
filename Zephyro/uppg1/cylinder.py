from math import pi


class Cylinder(object):
    """Represents a cylinder shape with height and radius"""

    def __init__(self, height: int, radius: int):
        self.height = height
        self.radius = radius

    def get_volume(self) -> float:
        return pi * self.height * self.radius ** 2

    def get_height(self) -> int:
        return self.height

    def get_width(self) -> int:
        return self.radius * 2
