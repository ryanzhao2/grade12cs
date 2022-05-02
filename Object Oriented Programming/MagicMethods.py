# import random
# class Die:
#     def __init__(self, sides):
#         self._dice_sides = sides
#
#
#     def roll(self):
#         value = random.randint(1, self._dice_sides)
#         return value
#
#     def __str__(self):
#         return f'Die 1: {self.roll()}'
#
#     def __eq__(self, other):
#         return self.roll() == other.roll()
#
#     def __lt__(self, other):
#         return self.roll() < other.roll()
#
#     def __gt(self, other):
#         return self.roll() > other.roll()
#
# die1 = Die(7)
# die2 = Die(7)
#
# print(die1 == die2)
# print(die1 < die2)
# print(die1)
# print(die2)

class Colour:

    def __init__(self, r, g, b):
        self._red = r
        self._green = g
        self._blue = b

    def red(self):
        return self._red

    def green(self):
        return self._green

    def blue(self):
        return self._blue

    def __str__(self):
        return f'str({self._red}, {self._green}, {self._blue})'

    def __repr__(self):
        return f'reprColour({self._red}, {self._green}, {self._blue})'

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __eq__(self, other):
        pass

    def luminosity(self):
        pass

    def saturation(self):
        pass
import MagicMethods as a
col = a.Colour(1, 1, 1)

a_list = (col, col, col)
print(a_list)

print(col)