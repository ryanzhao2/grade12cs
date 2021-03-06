# class Planet:
#     def __init__(self, name, radius, mass, distance):
#         self._name = name
#         self._radius = radius
#         self._mass = mass
#         self._distance = distance
#
#     def __str__(self):
#         return f'strname = {self._name}, mass = {self._mass}'
#
#     def __repr__(self):
#         return f'reprPlanet(name = {self._name}, mass = {self._mass})'
#
# import Tests as a
# earth = a.Planet("earth", 6378.1, 1, 149.6)
# mercury = a.Planet("mercury", 578.1, 5, 213.6)
# saturn = a.Planet("saturn", 278.1, 8, 209.6)
#
# planet_list = [earth, mercury, saturn]
#
# print(planet_list)
#
# for p in planet_list:
#     print(2, p)
#
#
# class Zhao:
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def age(self):
#         return self._age
#
#     def __str__(self):
#         return f'Name: {self._name} Age: {self._age}'
#
#     def __repr__(self):
#         return f'Zhao(Name: {self._name} Age: {self._age})'
#
#     def __lt__(self, other):
#         return self._age < other.age()
#
#     def __eq__(self, other):
#         return self._age == other.age()
#
#     def __gt__(self, other):
#         return self._age > other.age()
#
# ryan = Zhao('Ryan', 16)
# angela = Zhao('Angela', 21)
# hong = Zhao('hong', 52)
# jing = Zhao('jing', 52)
#
# print(list([ryan, angela, hong, jing]))
#
# print(ryan, angela, hong, jing)
# family_list = [ryan, angela, hong, jing]
# family_list.sort(reverse=True)
# print(family_list)

class Mousepad:

    def __init__(self, store, brand, price, size):
        self._store = store
        self._brand = brand
        self._price = price
        self._size = size

    def size(self):
        return self._size

    def __lt__(self, other):
        return self._size < other.size()

    def __eq__(self, other):
        return self._size == other.size()

    def __gt__(self, other):
        return self._size > other.size()

    def __str__(self):
        return f'{self._brand}'

    def __repr__(self):
        return f'Mousepad(sorted={self._brand})'

m1 = Mousepad('bestbuy', 'razer', 30, 90)
m2 = Mousepad('amazon', 'steelseries', 40, 91)
m3 = Mousepad('walmart', 'nobrand', 10, 50)

print(m1)
m_list = [m1, m2, m3]
m_list.sort(reverse=True)
print(m_list)