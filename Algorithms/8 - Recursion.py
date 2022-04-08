# Q1


# 9 FUNCTION CALLS

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(4))
#

# fib(3) + fib(2)
# fib(2) + fib(1) + fib(1) + fib(0)
# fib(1) + fib(0)
#0, 1, 1, 2, 3, 5,....


# Q2	'''
# 	This method should print the sum of squares from 1 to n
# 	For example sumOfSquares(4) = 30
# 	1^2 + 2^2 + 3^2 + 4^2 = 30
# 	'''
# 	def sumOfSquares(n):
# 	    if n == 1:
# 	        return 1
#
# 	    else:
# 	        return (n*n) + sumOfSquares(n - 1)
#
#
# 	print sumOfSquares(4)

# Q3
# def sum_list_recursion(a_list):
#     if len(a_list) == 1:
#         return a_list[0]
#     else:
#         sum = a_list[0] + sum_list_recursion(a_list[1:])
#         return sum
#
# print(sum_list_recursion([1,2,3,4,5]))

# Q4
#
# def integer_with_commas(num):
#     if len(num) <= 3:
#         return num
#     else:
#         commas = integer_with_commas(num[:-3]) + ',' + num[-3:]
#         return commas
# print(integer_with_commas('15866321232131'))

# def reverse_recursive(str):
#     if len(str) == 1:
#         return str
#     else:
#         reverse = str[-1] + reverse_recursive(str[:-1])
#         return reverse
#
# print(reverse_recursive('hello world'))

# def index_list(some_list, item):
#     if item not in some_list or some_list == []:
#         return 'Not Found'
#     elif some_list[0] == item:
#         return 0
#     else:
#         index = 1 + index_list(some_list[1:], item)
#         return index
#
#
# print(index_list([1, 2, 3, 4, 8, 9, 10, 5], 3))
#
# def flatten_list(some_list):
#     if len(some_list) == 0:
#         return ''
#     if not isinstance(some_list[0], list):
#         print("me:", str(some_list[0]))
#         return str(some_list[0]) + ' ' + str(flatten_list(some_list[1:]))
#     else:
#         print("me2:", str(some_list[0]))
#         return str(flatten_list(some_list[0])) + str(flatten_list(some_list[1:]))
#
#
#
# print(flatten_list([1, 2, 3, [[0, [7]], 9, [8, 8]], 5, 6, 9 ,10]))
