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
    dict = {}
    with open(filename, 'r') as pokemon_file:
        pokemon_file.readline()
        reader = csv.reader(pokemon_file)
        for line in reader:
            list = []
            type = line[2]
            if type not in dict:
                dict[type] = []
            for char in line:
                if char != type and char != line[1]:
                    list.append(char)
            dict[type].append(list)
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
            for item in data:
                writer.writerow(item)


pokemon_info = pokemon_dict('Pokemon.csv')
#print(pokemon_info)
display_pokemon('pokemon_structure.csv', pokemon_info)