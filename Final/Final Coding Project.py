import csv

class Automobile:
    def __init__(self, brand, doors, type, price):
        self._automobile_dict = {}
        self._brand = brand
        self._doors = doors
        self._type = type
        self._price = price

    def brand(self):
        return self._brand

    def doors(self):
        return self._doors

    def price(self):
        return self._price

    def __lt__(self, other):
        return self._price < other.price()

    def __gt__(self, other):
        return self._price > other.price()

    def __eq__(self, other):
        return self._price == other.price()

    def __str__(self):
        return f'The {self._brand} car with {self._doors} is a {self._type} and costs {self._price}'

    def __repr__(self):
        return f'Car(brand={self._brand}, doors={self._doors}, type={self._type})'

    def add_car(self, type, details):
        self._automobile_dict[type].append(details)



class Convertible(Automobile):

    def list_convertible(self):
        return [self._brand, self._doors, self._doors, self._price]

    def resale_value(self):
        return self._price * 0.84

class Sedan(Automobile):
    sedan_list = []


    def resale_value(self):
        return self._price * 0.76

class Wagon(Automobile):
    wagon_list = []

    def resale_value(self):
        return

class Hatchback(Automobile):
    hatchback_list = []


    def resale_value(self):
        return self._price * 0.80

#main

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
            elif type == 'sedan':
                a_sedan = Sedan(brand, doors, type)
            elif type == 'hatchback':
                a_hatchback = Sedan(brand, doors, type)
            all = [brand, doors, type, price]
            if type not in dict:
                dict[type] = []
            dict[type].append(all)
        #print(convertables)

def main():
    all_automobiles('Automobile_data.csv')

main()