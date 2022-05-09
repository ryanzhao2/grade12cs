import string
import random


class ShippingContainer:

    _serial_start = 1336

    def __init__(self, owner_code):
        self._owner_code = owner_code
        self._contents = []

        self._serial = self._get_next_serial()

    @classmethod
    def _get_next_serial(cls):
        three_letters = ''
        cls._serial_start += 1
        for i in range(3):
            random_letters = random.choice(string.ascii_uppercase)
            three_letters += random_letters
        return f'{cls._serial_start}{three_letters}'

    def owner_code(self):
        return self._owner_code

    def contents(self):
        return self._contents

    def change_serial(self):
        return self._get_next_serial()


    def serial(self):
        return self._serial

    def __str__(self):
        return f'{self._serial}:{self._owner_code} contains: {self._contents}'

    def add_contents(self, item):
        if item != None:
            self._contents.append(item)

    def remove_contents(self):
        self._contents = None


def shipping_program():
    s1 = ShippingContainer("MSR")
    s1.add_contents('books')
    s1.add_contents('electronics')

    s2 = ShippingContainer("HET")
    s2.add_contents('cars')

    s3 = ShippingContainer("MSR")
    s3.add_contents('clothing')
    s3.add_contents('pillows')

    print(s1)
    print(s2)
    print(s3)
    s3.change_serial()
    print('Change s3 serial number')
    print(s3)


shipping_program()


