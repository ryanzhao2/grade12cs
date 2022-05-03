class Planet:
    def __init__(self, name, radius, mass, distance):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._distance = distance

    def __str__(self):
        return f'strname = {self._name}, mass = {self._mass}'

    def __repr__(self):
        return f'reprPlanet(name = {self._name}, mass = {self._mass})'

import Tests as a
earth = a.Planet("earth", 6378.1, 1, 149.6)
mercury = a.Planet("mercury", 578.1, 5, 213.6)
saturn = a.Planet("saturn", 278.1, 8, 209.6)

planet_list = [earth, mercury, saturn]

print(planet_list)

for p in planet_list:
    print(2, p)

