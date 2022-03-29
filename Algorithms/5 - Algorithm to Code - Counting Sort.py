def counting_sort(a_list):
    minimum = min(a_list)
    maximum = max(a_list)
    spread = maximum - minimum
    offset_value = minimum

    counting_array = []
    for i in range(spread+1):
        counting_array.append(0)

    for element in a_list:
        index = element - offset_value
        counting_array[index] += 1

    sorted_list = []
    for i in range(0, len(counting_array)):
        counter = counting_array[i]
        while counter != 0:
            value = i + offset_value
            sorted_list.append(value)
            counter -= 1
    return sorted_list

list = [6001, 6305, 6300, 6800, 6790,1]
#print(counting_sort(list))

def new_counting_sort(file):
    all_list = []
    dict = {}
    unique_list = []
    with open(file, 'r') as money_file:
        for line in money_file:
            line = line.strip()
            all_list.append(line)
            if line not in unique_list:
                unique_list.append(line)
        unique = len(unique_list)
        for i in range(0, unique):
            print('i', i)
            print('unique', unique_list[i])
            dict[i] = unique_list[i]
            dict[unique_list[i]] = i
        print(dict)
        counting_array = []
        for j in range(unique):
            counting_array.append(0)

        for element in all_list:
            index = dict[element]
            counting_array[index] += 1
        sorted_list = []
        for i in range(0, len(counting_array)):
            counter = counting_array[i]
            while counter != 0:
                value = dict[i]
                sorted_list.append(value)
                counter -= 1
        return sorted_list

print(new_counting_sort('lotsOfMoney.txt'))
