import csv


# parent class that holds a dictionary of the inventory when added from child class
class Automobile:
    def __init__(self, name):
        self._type_name = name
        self._automobile_dict = {}

    def type_name(self):
        return self._type_name

    def __str__(self):
        return (f' The {self._type_name} category has these cars:\n {self._automobile_dict[self._type_name]} ')

    def __repr__(self):
        return (f'Garage: name={self._type_name}')

    def print_cars(self, car_type):
        for car in self._automobile_dict[car_type]:
            print(car)


# holds all the cars in the data set with 4 parameters
class Inventory:
    def __init__(self, brand, doors, type, price):
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

    def type(self):
        return self._type

    def __str__(self):
        return f'A {self._brand} with {self._doors} doors costs {self._price}'

    def __repr__(self):
        return f'Car(brand={self._brand}, doors={self._doors}, type={self._type})'


# 4 child classes each with different requirements to add

# only adds convertibles if their price is less than 25000
class Convertible(Automobile):

    def add_car(self, details):
        if 'convertible' not in self._automobile_dict:
            self._automobile_dict['convertible'] = []
        if details.price() <= 25000 and details.type() == 'convertible':
            self._automobile_dict['convertible'].append(details)


# only adds sedans if their price is less than 15000
class Sedan(Automobile):

    def add_car(self, details):
        if 'sedan' not in self._automobile_dict:
            self._automobile_dict['sedan'] = []
        if details.price() <= 15000 and details.type() == 'sedan':
            self._automobile_dict['sedan'].append(details)


# only adds wagon if their price is less than 17000
class Wagon(Automobile):

    def add_car(self, details):
        if 'wagon' not in self._automobile_dict:
            self._automobile_dict['wagon'] = []
        if details.price() <= 17000 and details.type() == 'wagon':
            self._automobile_dict['wagon'].append(details)


# only adds hatchback if their price is less than 17000
class Hatchback(Automobile):

    def add_car(self, details):
        if 'hatchback' not in self._automobile_dict:
            self._automobile_dict['hatchback'] = []
        if details.price() <= 17000 and details.type() == 'hatchback':
            self._automobile_dict['hatchback'].append(details)


# main

# reads through the file and adds to a list
def get_all_automobiles(file):
    with open(file, 'r', encoding='utf-8') as automobile_data:
        automobile_list = []
        automobile_data.readline()
        reader = csv.reader(automobile_data)
        for line in reader:
            brand = line[2]
            doors = line[5]
            type = line[6]
            if line[25] == '?':
                line[25] = '100000'
            price = int(line[25])
            all = Inventory(brand, doors, type, price)
            automobile_list.append(all)
        return automobile_list


# calls function from child class to add each car in the inventory
def insert_car(type_car, list_car):
    for car in list_car:
        type_car.add_car(car)


def main():
    all_auto_list = get_all_automobiles('Automobile_data.csv')

    convertible_car = Convertible('convertible')
    sedan_car = Sedan('sedan')
    wagon_car = Wagon('wagon')
    hatchback_car = Hatchback('hatchback')
    car_type_list = [convertible_car, sedan_car, wagon_car, hatchback_car]

    for car_type in car_type_list:
        insert_car(car_type, all_auto_list)

    for car_type in car_type_list:
        print(f'-----------{car_type.type_name()}-----------')
        car_type.print_cars(car_type.type_name())
        print('\n\n')


main()
