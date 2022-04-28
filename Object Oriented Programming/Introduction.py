class Planet:

    def __init__(self, name, t, orbit, moons):
        self._name = name
        self._type = t
        self._orbit_days = orbit
        self._number_of_moons = moons

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
