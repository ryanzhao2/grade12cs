import random

def create_random_numbers(num):

    list_num = []
    for i in range(0, num):
        list_num.append(random.randint(100, 500))

    return list_num


def write_num_list_file(filename, list_num):

    with open(filename, "w") as fileOut:

        for item in list_num:

            s = f'{item}\n'
            fileOut.write(s)


some_list = create_random_numbers(10)
write_num_list_file("random_numbers.txt", some_list)
        
