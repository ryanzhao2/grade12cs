# import random
# class Die:
#     def __init__(self, num_sides):
#         self._num_sides = num_sides
#         self._current_value = 1
#
#     def roll(self):
#         self._current_value = random.randint(1, self._num_sides)
#
#     def value(self):
#         return self._current_value
#
#     def __lt__(self, other):
#         return self._current_value < other.value()
#
#     def __gt__(self, other):
#         return self._current_value > other.value()
#
#     def __eq__(self, other):
#         return self._current_value == other.value()
#
#     # def __repr__(self):
#     #     return f'Die(num_sides={self._num_sides})'
#
#     def __str__(self):
#         return str(self._current_value)
#
# #example of a program to use the Die class
# die1 = Die(7)
# die2 = Die(7)
#
# #use the equality function
# print(die1 == die2)
#
# #use the less than function
# print(die1 < die2)
#
# print((die1, ''))

#
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

    def __add__(self, other):
        red = self._red
        green = self._green
        blue = self._blue

        new_colour = Colour(red, green, blue)
        return new_colour

    def __str__(self):
        return str(f'({self._red}, {self._green}, {self._blue})')

    def __repr__(self):
        return f'Colour(red={self._red}, green={self._green}, blue={self._blue})'

    def __sub__(self, other):
        pass

    def __eq__(self, other):
        pass

    def luminosity(self):
        pass

    def saturation(self):
        pass

colour1 = Colour(21, 50, 3)
print(colour1)
print([colour1])

