#Q1
"""
W = 10
X = 2
Y = -1
Z = 25
while not W < X < Y < Z:
    if W > X:
        W,X = X,W
    if X > Y:
        X,Y = Y,X
    if Y > Z:
        Y,Z = Z,Y

print(W, X, Y, Z)
"""

#Q2
n = 50
p = 2
c = 1


while n <= (p * (p * c) or n >= (p * (p * (c + 1)))):
    c = c + 1

print(f'The highest power of 2 <= {n} is {c}')