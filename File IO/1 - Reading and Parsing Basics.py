# #Q1
# gr_9 = []
# gr_10 = []
# gr_11 = []
# gr_12 = []
# with open('allStudents.txt') as student_file:
#     for line in student_file:
#         line = line.replace('\n', '')
#         line = line.split('\t')
#         elif line[0] == '09':
#             upper_first = line[2][0]
#             upper_last = line[1][0]
#             new_str = upper_first + line[2][1:].lower() + ' ' + upper_first + line[1][1:].lower()
#             gr_9.append(new_str)
#         elif line[0] == '10':
#             upper_first = line[2][0]
#             upper_last = line[1][0]
#             new_str = upper_first + line[2][1:].lower() + ' ' + upper_first + line[1][1:].lower()
#             gr_10.append(new_str)
#         elif line[0] == '11':
#             upper_first = line[2][0]
#             upper_last = line[1][0]
#             new_str = upper_first + line[2][1:].lower() + ' ' + upper_first + line[1][1:].lower()
#             gr_11.append(new_str)
#         elif line[0] == '12':
#             upper_first = line[2][0]
#             upper_last = line[1][0]
#             new_str = upper_first + line[2][1:].lower() + ' ' + upper_first + line[1][1:].lower()
#             gr_12.append(new_str)
#
#
# print(gr_9)

#Q2
# valid = []
# not_valid = []
# with open('emailAddresses.txt') as email_file:
#     for line in email_file:
#         line = line.replace('\n', '')
#         if line[-9:] == '@fake.com' or line[-9:] == '@mail.com':
#             not_valid.append(line)
#         else:
#             valid.append(line)
# print(valid,'\n')
# print(not_valid)

#Q3
# str = ''
# with open('contra.txt') as poem_file:
#     for line in poem_file:
#         print(line)
#         str += line[10]
# print(str)
