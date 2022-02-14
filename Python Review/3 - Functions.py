#CHAPTER 6 THINK LKE A COMPUTER SCIENTIST

# #2
# def day_name(num):
#     day = ''
#     if num == 0:
#         day = 'Sunday'
#     elif num == 1:
#         day = 'Monday'
#     elif num == 2:
#         day = 'Tuesday'
#     elif num == 3:
#         day = 'Wednesday'
#     elif num == 4:
#         day = 'Thursday'
#     elif num == 5:
#         day = 'Friday'
#     elif num == 6:
#         day = 'Saturday'
#     else:
#         print(None)
#     print(day)
#
# day_name(10)
#
# #6
#
# def days_in_month(month):
#     days = ''
#     if month == 'January':
#         days = 31
#     elif month == 'February':
#         days = 28
#     elif month == 'March':
#         days = 31
#     else:
#         print(None)
#     print(days)
#
# days_in_month('February')
#
# #13
#
# def slope(x1, y1, x2, y2):
#     slope = (y1 - y2)/(x1 - x2)
#     if slope == -0:
#         slope = 0.0
#     print(slope)
#
# slope(1, 2, 3, 2)
#
# #16
#
# def is_factor(f, n):
#     if n % f != 0:
#         print('Not Factor')
#     else:
#         print('Factor')
#
# is_factor(25, 15)
# #
#17
#
# def is_multiple(m, n):
#     if m % n == 0:
#         print('Is Multiple')
#     else:
#         print('Not Multiple')
#
# is_multiple(12, 7)

#Q1
# def right_justify(s, n):
#     space = ((n - (len(s))) * ' ')
#     print(space + s)
#
# right_justify('allen', 20)

#Q2
# def b(z):
#  prod = a(z, z)
#  print(z, prod)
#  return prod
#
# def a(x, y):
#  x = x + 1
#  return x * y
#
# def c(x, y, z):
#  sum = x + y + z
#  pow = b(sum)**2
#  return pow
#
# x = 1
# y = x + 1
# print(c(x, y+3, x+y))
# #returns 90 x 90 which is 8100

#Q3
# def isDigit(str):
#  new_str = ''
#  numbers = '123456789'
#  for i in range(len(str)):
#   if str[i] in numbers:
#    new_str += str[i]
#  if len(new_str) == len(str):
#   return True
#  else:
#   return False
#
# print(isDigit('.12'))
#
# def isFloat(str):
#  new_str = ''
#  float_values = '123456789.'
#  for i in range(len(str)):
#   if str[i] in float_values:
#    new_str += str[i]
#  if len(new_str) == len(str) and '.' in str:
#   return True
#  else:
#   return False
#
# print(isFloat('.12'))
#
# print(isinstance(.12, float))

#Q4
def isLeapYear(someYear):
 return someYear % 4 == 0 and someYear % 100 != 0 or someYear % 400 == 0

print(isLeapYear(400))