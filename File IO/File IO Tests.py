# #create a master holding list for all colours
#
# def generate_colours_list(filename):
#     lego_colours = []
#
#     with open(filename) as fileIn:
#
#         fileIn.readline()
#
#         for line in fileIn:
#             print(line)
#             line = line.strip().split(",")
#
#             #create a list for each colour in file
#             #[id, name, hex, transparency]
#             temp_entry = []
#             temp_entry.append(int(line[0]))
#             temp_entry.append(line[1])
#             temp_entry.append('#' + line[2])
#
#             #turn 'f' and 't' value of transparency into a boolean
#             if line[3] == 'f':
#                 temp_entry.append(False)
#             else:
#                 temp_entry.append(True)
#
#
#             lego_colours.append(temp_entry)
#
#     return lego_colours
#
#
# def print_colours_list(some_list):
#     #print the first 10 items of master list
#     for i in range(0, 10):
#         print(some_list[i])
#
#
# colours_list = generate_colours_list('colors.csv')
# print_colours_list(colours_list)

#List() is a function that creates a list by iterating through the characters of the string passed into it as a parameter
# line = list('asdasdasdasd')
# print(line)

#ASSIGNS THE LINE TO 'a' and then the pointer moves down
#THIS IS JUST FOR SEEING HOW READLINE WORKS
# with open('contra.txt') as poem_file:
#     count = 0
#     for i in range(5):
#         a = (poem_file.readline())
#         count += 1
#         print(count)
#         print(a)
#     print(poem_file.readline())

# str = '1,2,3,4,5'
# a = str.split(',', 5)
# b = a[5].split(',')
# print(a)
# print(b)
import linecache


