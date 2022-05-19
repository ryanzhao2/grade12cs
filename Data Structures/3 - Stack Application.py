'''

@author: aaronquesnelle
2018 for ICS 4U
'''

import Stacks.py

import math
import operator
ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       # '/':operator.div,
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
    for char in equation:
        if char.isdigit():
            a_stack.push(char)
        elif not char.isdigit() and char != ' ':
            n1 = a_stack.pop()
            n2 = a_stack.pop()
            answer = ops[char](n1,n2)
            return answer



print(rpn_calculator('3 4 +'))