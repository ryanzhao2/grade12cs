def convert(value):
    try:
        return int(value)
    except ValueError:
        return None
    except TypeError as err:
        print(err)
        return None

# print(convert([]))

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:
        return 0
    except TypeError as err:
        print(err)
        print(f'{a}, {b} \
              division not supported')
        return None

def main():

    try:
        print(divide(1, 0))
        print(divide('1', '2'))
    except (ZeroDivisionError, TypeError):
        print(1)

main()



# print(1 + 1.5)
# print('11')
