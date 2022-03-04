# import csv
# with open('courseMarks.txt', 'r') as course_file:
#     marksDict = {}
#     for line in course_file:
#         list = line.strip().split(',')
#         course = list[1]
#         if course not in marksDict:
#             marksDict[course] = {}
#         marksDict[course][list[0]] = list[2]
#     print(marksDict)

with open('studentsCourseMarks.txt', 'r') as student_marks:
    dict = {}
    list = []
    for line in student_marks:
        split_line = line.strip().split(', ')
        if len(line) == 6:
            course = line.strip()
            list = []
        if len(split_line) == 2:
            list.append(split_line[0])
        dict[course] = list
    print(dict)
