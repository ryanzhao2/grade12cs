#Q1 SHORTENED CODE THAT ONLY CALCULATES THE FIRST 3 LINES
# main_list = []
# first_list = []
# first_2nd_line = []
# first_3rd_line = []
# second_list = []
# third_list = []
# fourth_list = []
# fifth_list = []
# first_final = []
#
# def parse_braille_file(filename):
#     count = 1
#     with open(filename) as braille_file:
#         for i in range(15):
#             line = braille_file.readline().strip()
#             print(len(line))
#             for i in range(0, len(line), 2):
#                 if count == 1:
#                     first_list.append(line[i:i+2])
#                 elif count == 2:
#                     first_2nd_line.append(line[i:i+2])
#                 elif count == 3:
#                     first_3rd_line.append(line[i:i+2])
#                 # elif count <= 6 and count > 3:
#                 #     second_list.append(line[i:i+2])
#                 # elif count <= 10 and count > 7:
#                 #     third_list.append(line[i:i + 2])
#                 # elif count <= 14 and count > 11:
#                 #     fourth_list.append(line[i:i + 2])
#                 # elif count <= 18 and count > 15:
#                 #     fifth_list.append(line[i:i + 2])
#             count += 1
#         for i in range(len(first_list)):
#             str = first_list[i]
#             str += first_2nd_line[i]
#             str += first_3rd_line[i]
#             main_list.append(str)
#         # print(len(first_list))
#         # for i in range(0, 43):
#         #     str = first_list[i]
#         #     str += first_list[i+43]
#         #         str += first_list[i+86]
#         #     first_final.append(str)
# dict = {'oxxxxo': 't', 'xoxxoo': 'h', 'xooxoo': 'e', 'oooooo': ' ', 'xoxooo': 'b'}
# decipher = ''
#
# parse_braille_file('braille_python.txt')
# print(main_list[0])
# for i in range(5):
#
#     decipher += dict[main_list[i]]
# print(decipher)

#Q2
#
# def create_station_data(filename):
#     dict = {}
#     BC_list = []
#     ON_list = []
#     NU_list = []
#     MB_list = []
#     NT_list = []
#     AB_list = []
#     NB_list = []
#     SK_list = []
#     QC_list = []
#     NS_list = []
#     NL_list = []
#     PE_list = []
#     with open(filename, "r") as fileIn:
#         # read and ignore first 32 lines of file
#         for i in range(0, 32):
#             fileIn.readline()
#         station_dictionary = {}
#         for line in fileIn:
#             a = line = line.strip().replace('"', "").split(',')
#             if a[3] == 'ON':
#                 ON_list.append(a[0])
#             if a[3] == 'BC':
#                 BC_list.append(a[0])
#             if a[3] == 'NU':
#                 NU_list.append(a[0])
#             if a[3] == 'MB':
#                 MB_list.append(a[0])
#             if a[3] == 'NT':
#                 NT_list.append(a[0])
#             if a[3] == 'AB':
#                 AB_list.append(a[0])
#             if a[3] == 'NB':
#                 NB_list.append(a[0])
#             if a[3] == 'SK':
#                 SK_list.append(a[0])
#             if a[3] == 'QC':
#                 QC_list.append(a[0])
#             if a[3] == 'NS':
#                 NS_list.append(a[0])
#             if a[3] == 'NL':
#                 NL_list.append(a[0])
#             if a[3] == 'PE':
#                 PE_list.append(a[0])
#     dict['Ontario'] = ON_list
#     dict['British Columbia'] = BC_list
#     dict['Nunavut'] = NU_list
#     dict['Manitoba'] = MB_list
#     dict['Northwest Territories'] = NT_list
#     dict['Alberta'] = AB_list
#     dict['New Brunswick'] = NB_list
#     dict['Saskatchewan'] = SK_list
#     dict['Quebec'] = QC_list
#     dict['Nova Scotia'] = NS_list
#     dict['Newfoundland and Labrador'] = NL_list
#     dict['Prince Edward Island'] = PE_list
#     return dict
# data = create_station_data('climateData.csv')
# for char in data:
#     print(f'{char} {data[char]},\n')
#
#
