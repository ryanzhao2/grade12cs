# import string
# import random
#
#
# class ShippingContainer:
#
#     _serial_number = 1336
#
#     def __init__(self, owner_code):
#         self._owner_code = owner_code
#         self._contents = []
#
#         self._serial = self._get_next_serial()
#
#     @classmethod
#     def _get_next_serial(cls):
#         empty = ''
#         cls._serial_number += 1
#         for i in range(3):
#             empty += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#         return f'{cls._serial_number}{empty}'
#
#     def owner_code(self):
#         return self._owner_code
#
#     def contents(self):
#         return self._contents
#
#     def change_serial(self):
#         self._serial = self._get_next_serial()
#
#
#     def serial(self):
#         return self._serial
#
#     def __str__(self):
#         return f'{self._serial}:{self._owner_code} contains: {self._contents}'
#
#     def add_contents(self, item):
#         if item != None:
#             self._contents.append(item)
#
#     def remove_contents(self):
#         self._contents = None
#
#
# def shipping_program():
#     s1 = ShippingContainer("MSR")
#     s1.add_contents('books')
#     s1.add_contents('electronics')
#
#     s2 = ShippingContainer("HET")
#     s2.add_contents('cars')
#
#     s3 = ShippingContainer("MSR")
#     s3.add_contents('clothing')
#     s3.add_contents('pillows')
#
#     print(s1)
#     print(s2)
#     print(s3)
#     s3.change_serial()
#     print('Change s3 serial number')
#     print(s3)
#
#
# shipping_program()



# import airplanes

class Flight:

    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = Flight._generate_seating_plan(rows, seats)

    # generate a dictionary for each row to hold
    # passenger booking information
    @classmethod
    def _generate_seating_plan(cls, rows, seats):
        seating_plan = []
        for i in range(len(rows)):
            dict = {}
            for letter in seats:
                dict[letter] = None
            seating_plan.append(dict)
        return seating_plan

    @classmethod
    def _check_seat(cls, seat):
        row = seat[:-1]
        seat = seat[-1]
        return int(row), str(seat)


    def allocate_seat(self, seat, passenger):
        row, letter = Flight._check_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft(self):
        return self._aircraft.model()

    def num_seats(self):
        return self._aircraft.num_seats()

    # should be an internal function, not available to applications
    def seating(self):
        return self._seating

class Aircraft:

    def __init__(self):
        pass

    def num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)


class SmallPretendPlane(Aircraft):

    def model(self):
        return 'Small Pretend Plane'

    def seating_plan(self):
        return range(1, 4), "AB"


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEFGHJK"


def make_flights():
    test_plane = SmallPretendPlane()
    print(test_plane.seating_plan())

    test_flight = Flight('QQ234', SmallPretendPlane())
    print(test_flight.num_seats())
    print(test_flight.seating())


    a = AirbusA319()
    print(a.model())
    print(a.num_seats())
    print(a.seating_plan())

    b = Boeing777()
    print(b.model())
    print(b.num_seats())
    print(b.seating_plan())

    f1 = Flight('BA758', AirbusA319())
    f2 = Flight('KL613', Boeing777())

    print(f'FlightNo: {f1.number()}\nAirline: {f1.airline()}')
    print(f'Aircraft: {f1.aircraft()}')
    f1.allocate_seat('15C', 'Jayson Harmen')

    print(f1.num_seats(), 'seats on flight')
    print('Seat allocations\n', f1.seating())


make_flights()
#
# class Flight:
#
#     def __init__(self, number, aircraft):
#         self._number = number
#         self._aircraft = aircraft
#
#         rows, seats = self._aircraft.seating_plan()
#         self._seating = Flight._generate_seating_plan(rows, seats)
#
#     # generate a dictionary for each row to hold
#     # passenger booking information
#     @classmethod
#     def _generate_seating_plan(cls, rows, seats):
#         seating_plan = []
#         for i in rows:
#             dict = {}
#             for j in seats:
#                 dict[j] = None
#             seating_plan.append(dict)
#         return seating_plan
#     @classmethod
#     def _check_seat(cls, seat):
#         if len(seat) == 2:
#             row = seat[0]
#             s = seat[1]
#         else:
#             row = seat[0:2]
#             s = seat[2]
#         return int(row), str(s)
#
#     def allocate_seat(self, seat, passenger):
#         row, letter = Flight._check_seat(seat)
#         if self._seating[row][letter] is not None:
#             raise ValueError(f'Seat {seat} already occupied')
#
#         self._seating[row][letter] = passenger
#
#     def number(self):
#         return self._number
#
#     def airline(self):
#         return self._number[:2]
#
#     def aircraft(self):
#         return self._aircraft.model()
#
#     def num_seats(self):
#         return self._aircraft.num_seats()
#
#     # should be an internal function, not available to applications
#     def seating(self):
#         return self._seating
#
#
# class Aircraft:
#
#     def __init__(self):
#         pass
#
#     def num_seats(self):
#         rows, seats = self.seating_plan()
#         return len(rows) * len(seats)
#
#
# class SmallPretendPlane(Aircraft):
#
#     def model(self):
#         return 'Small Pretend Plane'
#
#     def seating_plan(self):
#         return range(1, 4), "AB"
#
#
# class AirbusA319(Aircraft):
#
#     def model(self):
#         return "Airbus A319"
#
#     def seating_plan(self):
#         return range(1, 23), "ABCDEF"
#
#
# class Boeing777(Aircraft):
#
#     def model(self):
#         return "Boeing 777"
#
#     def seating_plan(self):
#         return range(1, 56), "ABCDEFGHJK"
#
#
# def make_flights():
#     test_plane = SmallPretendPlane()
#     print(test_plane.seating_plan())
#
#     test_flight = Flight('QQ234', SmallPretendPlane())
#     print(test_flight.num_seats())
#     print(test_flight.seating())
#
#
#     a = AirbusA319()
#     print(a.model())
#     print(a.num_seats())
#     print(a.seating_plan())
#
#     b = Boeing777()
#     print(b.model())
#     print(b.num_seats())
#     print(b.seating_plan())
#
#     f1 = Flight('BA758', AirbusA319())
#     f2 = Flight('KL613', Boeing777())
#
#     print(f'FlightNo: {f1.number()}\nAirline: {f1.airline()}')
#     print(f'Aircraft: {f1.aircraft()}')
#     f1.allocate_seat('15C', 'Jayson Harmen')
#
#     print(f1.num_seats(), 'seats on flight')
#     print('Seat allocations\n', f1.seating())
#
#
# make_flights()
