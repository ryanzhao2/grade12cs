#Q1
# import random
# def random_names(filename):
#     with open(filename, 'r') as name_file:
#         list = []
#         for line in name_file:
#             list.append(line.strip())
#         return list
#
# def random_occupation(filename):
#     with open(filename, 'r') as occupation_file:
#         list = []
#         for line in occupation_file:
#             list.append(line.strip())
#         return list
#
#
# def generate_people(filename, names_file, occupations_file):
#     with open(filename, 'w') as person_file:
#         for char in names_file:
#             id = ''
#             for i in range(1, 12):
#                 if i == 4 or i == 7:
#                     id += '-'
#                 else:
#                     id += str(random.randint(0, 9))
#             salary = random.randint(25000, 125000)
#             salary = f'${salary}'
#             name = char
#             job = random.choice(occupations_file)
#             all_info = f'{id}, {name}, {job}, {salary}\n'
#             person_file.write(all_info)
#
# names = random_names('names.txt')
# occupations = random_occupation('occupations.txt')
# generate_people('people.txt', names, occupations)

#Q2
import csv
def pokemon_dict(filename):
    type_list = []
    large_list = []
    my_list = []
    dict = {}
    with open(filename, 'r') as pokemon_file:
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
        return dict


def display_pokemon(filename, pokemon_file):
    with open(filename, 'w', newline='') as new_pokemon_file:
        str_data = ''
        writer = csv.writer(new_pokemon_file)
        for char in pokemon_file:
            length = str(len(pokemon_file[char]))
            length += '\n'
            char += '\n'
            new_pokemon_file.write(char)
            new_pokemon_file.write(length)
            char = char.replace('\n', '')
            data = pokemon_file[char]
            for char in data:
                writer.writerow(char)


pokemon_info = pokemon_dict('Pokemon.csv')
#print(pokemon_info)
display_pokemon('pokemon_structure.csv', pokemon_info)