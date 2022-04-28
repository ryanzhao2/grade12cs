#Q1

def do_stuff_with_number(n):
    print(n)

def main():
    the_list = [1, 2, 3, 4, 5]

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError as err:
            print(err)
            return None

main()

#Q2

def get_last_name(student):
    return student["last_name"]


def main():
    student = {"name": "Sam Blainey", "courses": "ICS4U, MCV4U, SBIO4U"}
    try:
        name = get_last_name(student)
        print("All exceptions caught! Good job!")
        print(f'The student\'s last name is {name}')
    except KeyError as err:
        return err



main()


# def example1():
#     for i in range(3):
#         x = int(input("enter a number: "))
#         y = int(input("enter another number: "))
#         print(f'{x} / {y} = {x / y}')
#
#
# def example2(L):
#     print("\n\nExample 2")
#     sum = 0
#     sumOfPairs = []
#     for i in range(len(L)):
#         sumOfPairs.append(L[i] + L[i + 1])
#     print(f' sumOfPairs = {sumOfPairs}')
#
#
# def print_upper_file(filename):
#     file = open(filename, "r")
#     for line in file:
#         print(line.upper())
#     file.close()
#
#
# def main():
#     example1()
#
#     example2([10, 3, 5, 6, 9, 3])
#     example2([10, 3, 5, 6, "NA", 3])
#
#     print_upper_file("doesNotExistYet.txt")
#     print_upper_file("./Dessssktop/misspelled.txt")
#
#
# main()
# def convert(value):
#     try:
#         return int(value)
#     except ValueError:
#         return None
#     except TypeError as err:
#         print(err)
#         return None
#
# # print(convert([]))
#
# def divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         return 0
#     except TypeError as err:
#         print(err)
#         print(f'{a}, {b} \
#               division not supported')
#         return None
#
# def main():
#
#     try:
#         print(divide(1, 0))
#         print(divide('1', '2'))
#     except (ZeroDivisionError, TypeError):
#         print(1)
#
# main()



# print(1 + 1.5)
# print('11')
