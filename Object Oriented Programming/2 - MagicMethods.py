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
#     def __repr__(self):
#         return f'Die(num_sides={self._num_sides})'
#
#     def __str__(self):
#         return str(self._current_value)
#
# #example of a program to use the Die class
# die1 = Die(7)
# die1.roll()
# die2 = Die(7)
# die2.roll()
# #use the equality function
# print(die1 == die2)
#
# #use the less than function
# print(die1 < die2)
#
# print((die1, ''))


class Colour:

    def __init__(self, r, g, b):
        r = max(0, r)
        r = min(r, 255)
        g = max(0, g)
        g = min(g, 255)
        b = max(0, b)
        b = min(b, 255)
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
        red = self._red + other.red()
        green = self._green + other.green()
        blue = self._blue + other.blue()

        new_colour = Colour(red, green, blue)
        return new_colour

    def __str__(self):
        return str(f'({self._red}, {self._green}, {self._blue})')

    def __repr__(self):
        return f'Colour(red={self._red}, green={self._green}, blue={self._blue})'

    def __sub__(self, other):
        red = abs(self._red - other.red())
        green = abs(self._green - other.green())
        blue = abs(self._blue - other.blue())

        new_colour = Colour(red, green, blue)
        return new_colour

    def __eq__(self, other):
        if self._red == other.red() and self._green == other.green() and self._blue == other.blue():
            return True
        return False

    def hex(self):
        return f'{self._red:X}{self._green:X}{self._blue:X}'

    def luminosity(self):
        max_value = max(self._red, self._green, self._blue)
        min_value = min(self._red, self._green, self._blue)
        formula = 0.5 * ((max_value / 255) + (min_value / 255))
        return formula

    def saturation(self):
        max_value = max(self._red, self._green, self._blue)
        min_value = min(self._red, self._green, self._blue)
        if self.luminosity() <= 0.5:
            formula = (((max_value / 255) - (min_value / 255)) / ((max_value / 255) + (min_value / 255)))
        elif self.luminosity() > 0.5:
            formula = (((max_value / 255) - (min_value / 255)) / ((2 - (max_value / 255) - (min_value / 255))))
        else:
            formula = 0
        return formula



colour1 = Colour(125, 34, 77)
colour2 = Colour(105, 230, 152)
print(colour1 + colour2)
print(colour1.hex())
print(colour1.luminosity())
print(colour1.saturation())
print(colour1 == colour2)
print([colour1])

