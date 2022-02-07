#REPL READ EVALUATE PRINT LOOP

import math
number = 10
number = number ** 2

print(number)
print(math.sqrt(number))
#returns sqrt with 1 decimal place
print("Hello World\n\n")
#purpose of \n is to create a new line
print("Hello\tWorld")
#the purpose of \t is to create 3 spaces
print(f'My number is {number}')
#the f is f string which allows you to format the string such as aligning it
print(f'My number is {10:>10.2f}')
#the >10.2f aligns the string 10 spaces to the right with 2 decimal places