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

def right_justify(s, n):
    space = (n - (len(s))) * ' ')


right_justify('allen', 20)
