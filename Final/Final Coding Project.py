import csv
# parent class for a generic automobile, which holds basic auto attributes,
# plus a method for storing the auto into an inventory
class Automobile:
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

    def put_into_inventory(self, type, inventory):
        if type not in inventory._automobile_dict:
            inventory._automobile_dict[type] = []
        inventory._automobile_dict[type].append(self)

# Inventory class holds all the automobiles in the data set with selected parameters
class Inventory:
    def __init__(self):
        self._automobile_dict = {}

    def get_cars_by_type(self, car_type):
        return self._automobile_dict[car_type]

# 4 child classes each with different requirements to add

# only adds convertibles if their price is less than $25,000
class Convertible(Automobile):

    def store_in_inventory(self, inventory):
        if self.price() <= 25000:
            self.put_into_inventory(self.type(), inventory)

# only adds sedans if their price is less than $15,000
class Sedan(Automobile):
    def store_in_inventory(self, inventory):
        if self.price() <= 25000:
            self.put_into_inventory(self.type(), inventory)

# only adds wagon if their price is less than $17,000
class Wagon(Automobile):
    def store_in_inventory(self, inventory):
        if self.price() <= 25000:
            self.put_into_inventory(self.type(), inventory)

# only adds hatchback if their price is less than $17,000
class Hatchback(Automobile):
    def store_in_inventory(self, inventory):
        if self.price() <= 25000:
            self.put_into_inventory(self.type(), inventory)

# reads through the file and adds the automobile objects into an inventory based on inventory requirements for each type of automobiles
def save_automobiles_in_inventory(file, inventory):
    with open(file, 'r', encoding='utf-8') as automobile_data:
        automobile_data.readline()
        reader = csv.reader(automobile_data)
        for line in reader:
            brand = line[2]
            doors = line[5]
            type = line[6]
            if line[25] == '?':
                line[25] = '100000'
            price = int(line[25])
            if type == 'hatchback' :
                auto = Hatchback(brand, doors, type, price)
            elif type == 'sedan':
                auto = Sedan(brand, doors, type, price)
            elif type == 'wagon':
                auto = Wagon(brand, doors, type, price)
            elif type == 'convertible':
                auto = Convertible(brand, doors, type, price)
            auto.store_in_inventory(inventory)

def main():
    inventory = Inventory()
    save_automobiles_in_inventory('Automobile_data.csv', inventory)
    car_type_list = ['convertible', 'sedan', 'hatchback', 'wagon']

    # display all automobiles in the inventory
    for car_type in car_type_list:
        print(f'-----------{car_type}-----------')
        for car in inventory.get_cars_by_type(car_type):
            print(car)
        print('\n\n')

    # display all fancy convertibles over $15,000
    print ('Fancy convertibles:')
    for car in inventory.get_cars_by_type('convertible'):
        if car.price() > 15000:
            print(car)
    print('\n\n')


main()
