import math
class Planet:

    def __init__(self, name, t, orbit, moons, radius):
        self._name = name
        self._type = t
        self._orbit_days = orbit
        self._number_of_moons = moons
        self._moon_list = []
        self._planet_radius = radius



    def name(self):
        return self._name

    def change_type(self, new):
        self._type = new

    def orbit_day(self):
        return self._orbit_days

    def change_orbit_day(self, new):
        self._orbit_days = new

    def num_moons(self):
        return self._number_of_moons

    def change_number_moons(self, new):
        self._number_of_moons = new

    def add_moon(self):
        self._moon_list.append(self._name)
        return self._moon_list

    def calculate_circumference(self):
        circumference = self._planet_radius * 2 * math.pi
        return circumference



e = Planet("earth", "terrestrial", 365, 10, 3)

print(e.name())
print(e.orbit_day())

e.change_orbit_day(366)
print(e.orbit_day())
print(e.add_moon())
print(e.calculate_circumference())

# class Sun:
#     def __init__(self, name, radius, mass, temperature):
#         self._name = name
#         self._radius = radius
#         self._mass = mass
#         self._temp = temperature
#
#     def name(self):
#         return self._name
#
#     def radius(self):
#         return self._radius
#
#     def temperature(self):
#         return self._temp
#
#     def volume(self):
#         vol = 4/3 * math.pi * (self._radius ** 3)
#         return vol
#
#     def surface_area(self):
#         sa = 4 * math.pi * (self._radius ** 2)
#         return sa
#
#     def change_name(self, new):
#         self._name = new
#
#     def change_radius(self, new):
#         self._radius = new
#
#     def __str__(self):
#         return f'1'
#
#     def __repr__(self):
#         return f'Sun({self._radius}, {self._name})'
#
# print("\n\nTesting Sun\n")
#
# s = Sun('sun', 696340, 1.989, 5600)
# s.name()
# print(s)
# print([s])
#
# print(f'Radius is {s.radius()}')
# print(f'Temperature is {s.temperature()}')
# print(f'Volume should be 1.414336139666311e+18 = {s.volume()}')
# print(f'Surface Area should be 6093299852082.22 = {s.surface_area()}')
#
# s.change_name('The Sun')
# print(f'\nThe new name should be The Sun = {s.name()}')
#
# s.change_radius(1000)
# print(f'\nRadius is {s.radius()}')
# print(f'Volume should be 4188790204.7863903 = {s.volume()}')
# print(f'Surface Area should be 12566370.614359172 = {s.surface_area()}')
#
#
# print("\n\n\nTesting Tau Ceti\n")
# tau_ceti = Sun('tau ceti', 551690, 1.557, 5071)
#
#
# print(f'Radius is {tau_ceti.radius()}')
# print(f'Temperature is {tau_ceti.temperature()}')
# print(f'Volume should be 7.033539733032631e+17 = {tau_ceti.volume()}')
# print(f'Surface Area should be 3824723884626.855 = {tau_ceti.surface_area()}')
#
# tau_ceti.change_name('Tau Ceti')
# print(f'\nThe new name should be Tau Ceti = {tau_ceti.name()}')
#

class DigitalClockDisplay:

    def __init__(self, hour, minute):
        self._hour_limit = 24
        self._hour = hour

        self._minute_limit = 60
        self._minute = minute

    def display(self):
        if int(self._hour) > 12:
            self._hour = int(self._hour) - 12
        if len(str(self._minute)) == 1 and len(str(self._hour)) > 1:
            digital = f'{self._hour}:0{self._minute}'
        elif len(str(self._hour)) == 1 and len(str(self._minute)) > 1:
            digital = f'0{self._hour}:{self._minute}'
        elif len(str(self._hour)) > 1 and len(str(self._minute)) > 1:
            digital = f'{self._hour}:{self._minute}'
        else:
            digital = f'0{self._hour}:0{self._minute}'
        return str(digital)

    def time_tick(self):
        self._minute = int(self._minute)
        self._hour = int(self._hour)
        self._hour += (int(self._minute) + 1) // int(self._minute_limit)
        if self._hour >= self._hour_limit:
            self._hour = self._hour - self._hour_limit
        #self._hour = self._hour % self._hour_limit
        #self._minute = (int(self._minute) + 1) % self._minute_limit
        self._minute = (int(self._minute) + 1)
        if self._minute >= self._minute_limit:
            self._minute = self._minute - self._minute_limit

    def set_minute(self, minute):
        if minute < self._minute_limit:
            self._minute = minute

    def set_hour(self, hour):
        if hour < self._hour_limit:
            self._hour = hour

    def set_time(self, hour, minute):
        self.set_minute(minute)
        self.set_hour(hour)

print("\n\nTesting Digital Clock Display\n")

my_clock = DigitalClockDisplay(10, 20)
print(f'Display should read 10:20 = {my_clock.display()}')

my_clock = DigitalClockDisplay(8, 10)
print(f'Display should read 08:10 = {my_clock.display()}')

my_clock = DigitalClockDisplay(18, 8)
print(f'Display should read 18:08 = {my_clock.display()}')

print("\n\nTest set time function")
my_clock.set_time(23, 59)
print(f'Display should read 23:59 = {my_clock.display()}')

my_clock.set_time(24, 0)
print(f'Display should read 23:00 = {my_clock.display()}')

my_clock.set_time(23, 61)
print(f'Display should read 23:00 = {my_clock.display()}')

my_clock.set_time(3, 59)
print(f'Display should read 04:10 = {my_clock.display()}')

print("\n\nTesting Time Tick")
my_clock.time_tick()
my_clock.time_tick()
my_clock.time_tick()
my_clock.time_tick()
my_clock.time_tick()
print(f'Display should read 23:05 = {my_clock.display()}')
