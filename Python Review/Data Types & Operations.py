#Q1
"""
width = 17
height = 12.0
delimiter = '.'
#For each of the following expressions, write the value of the expression and the type (of the value of the expression).

print(width/2)
#8.5 and it is a float
print(width/2.0)
#8.5 and it is a float
print(height/3)
#4.0 and it is a float
print(1 + 2 * 5)
#11 and it is an integer
print(delimiter * 5)
#..... and it is a string
"""

#Q2
import math
radius = 5
print(4/3 * math.pi * radius ** 3)

price = 24.95
first_shipping = 3
additional = 0.75
copies = 60
total_cost = (((price * 0.60) + first_shipping + (copies - 1) * additional) * copies)
print(total_cost)

leave_time_hours = 6
leave_time_minutes = 52

easy_pace_minutes = 8
easy_pace_seconds = 15

tempo_pace_minutes = 7
tempo_pace_seconds = 12

minutes = leave_time_hours * 60
seconds = (minutes + leave_time_minutes) * 60
print(seconds)


