import csv
type_list = []
large_list = []
my_list = []
dict = {}
with open('Pokemon.csv') as pokemon_file:
    reader = csv.DictReader(pokemon_file)
    for line in reader:
        if line['Type 1'] not in type_list:
            type_list.append(line['Type 1'])
            dict[line['Type 1']] = []
            #print(line)
        mini_list = []
        for char in type_list:

            if line['Type 1'] == char:
                for stat in line:
                    if stat != 'Type 1':
                        mini_list.append(line[stat])
                if mini_list[2] == '':
                    mini_list.pop(2)
                #print(mini_list)
        dict[line['Type 1']].append(mini_list)
    print(dict)
