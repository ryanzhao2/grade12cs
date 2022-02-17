import random
def even_odd_list(number_values, low_value, high_value):
    if number_values - 1 + low_value > high_value or high_value < low_value:
        print('Range is too small')
        return
    even_list = []
    odd_list = []
    if number_values % 2 == 1:
        number_values -= 1
    while len(odd_list) != number_values/2 or len(even_list) != number_values/2:
        random_list = (random.sample(range(low_value, high_value+1), number_values))
        for char in random_list:
            if char % 2 == 0 and len(even_list) < number_values/2 and char not in even_list:
                even_list.append(char)
            elif char % 2 == 1 and len(odd_list) < number_values/2 and char not in odd_list:
                odd_list.append(char)

    odd_list.sort()
    even_list.sort()
    odd_list.extend(even_list)
    return odd_list
for i in range(1000000):
    if even_odd_list(6, 10, 20) == [11, 13, 17, 12, 14, 20]:
        print('yes')
    #print(even_odd_list(6, 10, 20))


# def create_school_dictionary(school_codes, school_names):
#     dict = {}
#     for char in school_codes:
#         dict[char] == school_names[char]