import random
def random_names(filename):
    with open(filename, 'r') as name_file:
        list = []
        for line in name_file:
            list.append(line.strip())
        return list

def random_occupation(filename):
    with open(filename, 'r') as occupation_file:
        list = []
        for line in occupation_file:
            list.append(line.strip())
        return list


def generate_people(filename, names_file, occupations_file):
    with open(filename, 'w') as person_file:
        for i in range(500):
            (num) = ''
            for i in range(1, 11):
                if i == 4 or i == 7:
                    num += '-'
                else:
                    (num) += random.randint(1,9)
            print(num)



names = random_names('names.txt')
occupations = random_occupation('occupations.txt')
#print(names)
print(occupations)
random_people = generate_people('people.txt', names, occupations)

