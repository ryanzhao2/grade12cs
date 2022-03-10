# import csv
# with open('courseMarks.txt', 'r') as course_file:
#     marksDict = {}
#     for line in course_file:
#         list = line.strip().split(',')
#         course = list[1]
#         score = list[2].replace(' ', '')
#         if course not in marksDict:
#             marksDict[course] = {}
#         marksDict[course][list[0]] = score
#     print(marksDict)

#Q2
# def write_wine():
#     with open('winemag.txt', 'w') as fileIn:
#         a = '0\n'
#         fileIn.write(a)
#         b = '0'
#         c = 'Spain'
#         d = "Martha's Vineyard"
#         e = '96'
#         f = '235'
#         g = 'California'
#         h = 'Cabernet Sauvignon'
#         i = 'Heitz'
#         fileIn.write(f'{b}\t{c}\t{d}\t{e}\t{f}\t{g}\t{h}\t{i}')
# californiaWines = {}
# with open('winemag.txt', 'r') as fileIn:
#     fileIn.readline()
#     for line in fileIn:
#         #print(line)
#         line = line.split('\t')
#         key = (f'{line[7]} | {line[2]}')
#         californiaWines[key] = line[4]
#     print(californiaWines)
#
#
# write_wine()
#
# def student_names(filename):
#     dict = {}
#     with open(filename, 'r') as student_file:
#         for line in student_file:
#             list = line.strip().split(', ')
#             list = [list[0], list[1].replace('\t', ' '), list[2]]
#             dict[list[0]] = list[1]
#     return dict
# #
# def student_courses(filename):
#     with open(filename, 'r') as student_marks:
#         dict = {}
#         list = []
#         for line in student_marks:
#             split_line = line.strip().split(', ')
#             if len(line) == 6:
#                 course = line.strip()
#                 list = []
#             if len(split_line) == 2:
#                 list.append(split_line[0])
#             dict[course] = list
#         return dict
#
# def all_data(filename, names, courses):
#     dict = {}
#     main_list = []
#     with open(filename, 'r') as courses_file:
#         #THIS IS TO SET UP THE LISTS IN THE DICTIONARY FOR ALL STUDENTS
#         for name in names:
#             dict[name] = []
#         for line in courses_file:
#             list_line = line.strip().split(',')
#             if list_line[0] in courses.keys():
#                 courses_list = courses[list_line[0]]
#                 for char in courses_list:
#                     #APPENDING COURSES TO LIST IN THE DICTIONARY IF THE CHARACTER IS IN THE LIST
#                     #ALSO APPENDS NAME WHICH COMES FROM A DIFFERENT DICTIONARY WITH KEY OF STUDENT ID and the value being the name
#                     dict[char].append(list_line[0])
#                     dict[char].append(names[char])
#         for char in dict:
#             dict[char].pop(1)
#             dict[char].pop(2)
#             dict[char].pop(3)
#         for char in dict:
#             name = dict[char][4]
#             courses = dict[char][0:4]
#             list = [char, name, courses]
#             main_list.append(list)
#         print(main_list)
#
# names = student_names('studentsNames.txt')
# courses = student_courses('studentsCourseMarks.txt')
# all_data('studentsCourseMarks.txt', names, courses)