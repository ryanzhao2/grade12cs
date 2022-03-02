import csv


def create_kerala_districts(filename):
    kerala_flood_info = {}
    with open(filename, "r") as file_in:
        info = file_in.readline().strip().split(',')
        reader = csv.reader(file_in)
        for line in reader:
           if line[0] == 'Kasaragode':
               line[0] = 'Kasaragod'
           kerala_flood_info[line[0]] = {}
           for i in range(1, 7):
             kerala_flood_info[line[0]][info[i]] = line[i]
           kerala_flood_info[line[0]]['warnings'] = []
        #print(kerala_flood_info)
        return kerala_flood_info


def add_kerala_flood_warnings(filename, kerala_flood_info):
    with open(filename, "r") as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for line in reader:
            list = [line[1], line[2], line[3]]
            kerala_flood_info[line[0]]['warnings'].append(list)

        return kerala_flood_info

def print_kerala_flood_info(kerala_flood_info):
     for key in (kerala_flood_info):
         print(key)
         print(kerala_flood_info[key])


def main():
    flood_dict = create_kerala_districts("district_wise_details.csv")
    add_kerala_flood_warnings("warnings_actual_predicted.csv", flood_dict)

    print_kerala_flood_info(flood_dict)

#add_kerala_flood_warnings('warnings_actual_predicted.csv', create_kerala_districts("district_wise_details.csv"))
#create_kerala_districts('district_wise_details.csv')
main()

