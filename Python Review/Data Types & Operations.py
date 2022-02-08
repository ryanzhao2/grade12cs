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

#1
"""
import math
radius = 5
print(4/3 * math.pi * radius ** 3)

price = 24.95
first_shipping = 3
additional = 0.75
copies = 60
total_cost = (((price * 0.60) + first_shipping + (copies - 1) * additional) * copies)
print(total_cost)
"""
"""
import datetime
leave_time_hours = 6
leave_time_minutes = 52
leave_time_seconds = 0

easy_pace_minutes = 8 * 2
easy_pace_seconds = 15 * 2

tempo_pace_minutes = 7 * 3
tempo_pace_seconds = 12 * 3

initial_seconds = leave_time_hours * 60 * 60 + leave_time_minutes * 60 + leave_time_seconds
total_easy_pace_seconds = easy_pace_minutes * 60 + easy_pace_seconds
total_tempo_pace_seconds = tempo_pace_minutes * 60 + tempo_pace_seconds
total_seconds = (initial_seconds + total_tempo_pace_seconds + total_easy_pace_seconds)

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
hours = minutes // 60
remaining_minutes = minutes % 60

get_date = datetime.datetime.now()
replaced_date = get_date.replace(hour=hours, minute=remaining_minutes, second=remaining_seconds)
time = replaced_date.strftime("%X")
print(f'{time} am')
"""

#Q3
"""
p = 110000
r = 0.0725 / 12
n = 30 * 12
m = p * (r / (1 - (1 + r) ** -n))
print(f'{m:<.2f}')

"""