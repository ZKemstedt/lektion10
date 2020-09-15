from random import randint
from cylinder import Cylinder


class Stack():
    def __init__(self, n_cylinders: int):
        self.cylinders = [Cylinder(randint(0, 10), 
                                   randint(0, 5))
                          for _ in range(n_cylinders)]

    def get_stack_height(self) -> int:
        return sum([cyl.get_height() for cyl in self.cylinders])

    def get_stack_width(self) -> int:
        return max(self.cylinders, key=lambda c: c.get_width()).get_width()

    def get_stack_volume(self) -> float:
        return sum([cyl.get_volume() for cyl in self.cylinders])
