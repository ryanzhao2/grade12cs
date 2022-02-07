def calculate_pressure():
    enter_boiling = int(input('Enter a temperature in Celcius that is greater than 79 and less than 201: '))
    pressure = 5 * enter_boiling - 400
    if pressure < 100:
        sea_level = 1
    elif pressure == 100:
        sea_level = 0
    else:
        sea_level = -1
    print(pressure)
    print(sea_level)

calculate_pressure()