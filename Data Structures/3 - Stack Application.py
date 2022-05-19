'''

@author: aaronquesnelle
2018 for ICS 4U
'''

from Stacks import Stack

import math
import operator
ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow,
       'sin':math.sin,
       'tan':math.tan,
       'cos':math.cos,
       'pi':math.pi}

def rpn_calculator(equation):
    a_stack = Stack()
    n1 = ''
    n2 = ''
    answer = ''
    a_list = equation.split()
    for item in a_list:
        if item.isdigit():
            a_stack.push(int(item))
        elif not item.isdigit() and item != ' ':
            n1 = a_stack.pop()
            n2 = a_stack.pop()
            if item == '√':
                answer = round(math.sqrt(n2))
            else:
                answer = round(ops[item](n2,n1))

            a_stack.push(answer)
    return answer



print(rpn_calculator('3 4 3 +'))
# 3 4 + Answer is 7

print(rpn_calculator('1 2 3 * 4 + +'))
# 1 2 3 * 4 + + Answer is 11

print(rpn_calculator('1 2 + 3 * 4 + '))
# 1 2 + 3 * 4 + Answer is 13

print(rpn_calculator('5 1 2 + 4 * 3 - +'))
# 5 1 2 + 4 * 3 - + Answer is 14

print(rpn_calculator('1 2 + 4 * 3 - 5 +'))
# or 1 2 + 4 * 3 - 5 +

print(rpn_calculator('4 18 3 / 2 ^ +'))
# 4 18 3 / 2 ^ +  Answer is 40

print(rpn_calculator('2 1 49 2 √ + * 4 /'))
# 2 1 49 2 √ + * 4 /   Answer is 4