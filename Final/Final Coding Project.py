import csv

convertables = []
sedans = []
def all_automobiles(file):
    with open(file, 'r', encoding='utf-8') as automobile_data:
        dict = {}
        automobile_data.readline()
        reader = csv.reader(automobile_data)
        for line in reader:
            brand = line[2]
            doors = line[5]
            type = line[6]
            price = line[25]
            if type == 'convertible':
                a_convertible = Convertible(brand, doors, type)
                convertables.append(a_convertible)
                print(a_convertible)
            elif type == 'sedan':
                a_sedan = Sedan(brand, doors, type)
                sedans.append(a_convertible)
                print(a_sedan)
            all = [brand, doors, type, price]
            if type not in dict:
                dict[type] = []
            dict[type].append(all)
        #print(convertables)

class Car:
    def __init__(self, brand, doors):
        self._brand = brand
        self._doors = doors


class Convertible(Car):
    def __init__(self, brand, doors, type):
        super().__init__(brand, doors)
        self._type = type

    def __str__(self):
        return f'{self._brand},{self._doors}, {self._type}'

class Sedan(Car):
    def __init__(self, brand, doors, type):
        super().__init__(brand, doors)
        self._type = 'Sedan'
    def __str__(self):
        return f'{self._brand},{self._doors}, {self._type}'
class Wagon(Car):
    def __init__(self, brand, doors):
        super().__init__(brand, doors)
        self._type = 'Wagon'

class Hatchback(Car):
    def __init__(self, brand, doors):
        super().__init__(brand, doors)
        self._type = 'Hatchback'

all_automobiles('Automobile_data.csv')

def main():
        pass