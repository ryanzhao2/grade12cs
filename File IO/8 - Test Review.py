import csv
with open('courseMarks.txt', 'r') as course_file:
    marksDict = {}
    for line in course_file:
        list = line.strip().split(',')
        course = list[1]
        if course not in marksDict:
            marksDict[course] = {}
        marksDict[course][list[0]] = list[2]
    print(marksDict)


californiaWines = {}
with open('winemag.txt', 'r') as fileIn:
    fileIn.readline()

