#Q1
gr_9 = []
gr_10 = []
gr_11 = []
gr_12 = []
with open('allStudents.txt') as student_file:
    for line in student_file:
        line = line.strip().split('\t')
        year = line[0]
        name = f'{line[2]} {line[1]}'
        if year == '09':
            gr_9.append(name)
        elif year == '10':
            gr_10.append(name)
        elif year == '11':
            gr_11.append(name)
        elif year == '12':
            gr_12.append(name)

print(gr_12)

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
str = ''
with open('contra.txt') as poem_file:
    for line in poem_file:
        #print(line)
        str += line[10]
print(str)
