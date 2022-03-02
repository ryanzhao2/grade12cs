import csv


def create_kerala_districts(filename):
    kerala_flood_info = {}
    with open(filename, "r") as file_in:
        info = file_in.readline().strip().split(',')
        reader = csv.reader(file_in)
        for line in reader:
           kerala_flood_info[line[0]] = {}
           kerala_flood_info[line[0]][info[1]] = line[1]
           kerala_flood_info[line[0]][info[2]] = line[2]
           kerala_flood_info[line[0]][info[3]] = line[3]
           kerala_flood_info[line[0]][info[4]] = line[4]
           kerala_flood_info[line[0]][info[5]] = line[5]
           kerala_flood_info[line[0]][info[6]] = line[6]

        #print(kerala_flood_info)
        return kerala_flood_info


def add_kerala_flood_warnings(filename, kerala_flood_info):
    with open(filename, "r") as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for line in reader:
            list = []
            #if line[0] == 'Kasaragode':
             #   line[0] = 'Kasaragod'
            kerala_flood_info[line[0]]['warnings'] = [line[1], line[2], line[3]]

        print(kerala_flood_info)



# def print_kerala_flood_info(kerala_flood_info):
#      for key in (kerala_flood_info):
#          print(key)
#          print(kerala_flood_info[key])
#
#
# def main():
#     flood_dict = create_kerala_districts("district_wise_details.csv")
#     add_kerala_flood_warnings("warnings_actual_predicted.csv", flood_dict)
#
#     print_kerala_flood_info(flood_dict)

add_kerala_flood_warnings('warnings_actual_predicted.csv', create_kerala_districts("district_wise_details.csv"))
#create_kerala_districts('district_wise_details.csv')
#main()

