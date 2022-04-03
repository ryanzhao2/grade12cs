#Q1


#9 FUNCTION CALLS

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# print(fibonacci(4))
#
# fib(3) + fib(2)
# fib(2) + fib(1) + fib(1) + fib(0)
# fib(1) + fib(0) + fib(1) + fib(1) + fib(0)

#Q2	'''
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

#Q3
def sum_recursion(n):
    list = [1, 3, 5, 6, 8]
    length = len(list)
    while length != 0:
        return a_list[i] + sum_recursion(a_list[i+1])

sum_recursion([3, 5, 6, 9, 10, 39])

