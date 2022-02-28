import csv
type_list = []
main_list = []
large_list = []
dict = {}
with open('Pokemon.csv') as pokemon_file:
    reader = csv.DictReader(pokemon_file)
    for line in reader:
        if line['Type 1'] not in type_list:
            type_list.append(line['Type 1'])
            #print(line)
        for char in type_list:
            if line['Type 1'] == char:
                mini_list = []
                mini_list.append(line['Name'])
                dict[char] = mini_list
                large_list.append(mini_list)

    print(large_list)
    print(dict)
    #print(type_list)

