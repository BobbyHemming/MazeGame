import numpy


class Vector:
    def __init__(self, x_or_pair, y):
        if y is None:
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:
            self.x = x_or_pair
            self.y = y

    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        else:
            return False

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'{(self.x, self.y)}'

    def __eq__(self, other):
        if other != 0 and self.x == other.x and self.y == other.y:
            return True
        elif other == 0 and self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def __dne__(self, other):
        if self.x == other.x and self.y == other.y:
            return False
        elif other == 0 and self.x == 0 and self.y == 0:
            return False
        else:
            return True


