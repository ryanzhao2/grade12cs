#Q1
#
# W = 10
# X = 2
# Y = -1
# Z = 25
# while not W < X < Y < Z:
#     if W > X:
#         W,X = X,W
#     if X > Y:
#         X,Y = Y,X
#     if Y > Z:
#         Y,Z = Z,Y
#     print(W, X, Y, Z)
#
# print(W, X, Y, Z)


#Q2
#
# n = 100
# p = 1
# c = 2
#
# while c * 2 <= n:
#     c *= 2
#     p += 1
#     print(c)
#
# print(f'The highest power of 2 <= {n} is {p}')


#Q3
all_temp = []
all_w_speed = []
all_chill = []
for w_speed in range(5, 61, 5):
    all_w_speed.append(f'{w_speed:>3}')
    for temp in range(40, -46, -5):
        chill = round(35.74 + (0.6215 * temp) - (35.75 * (w_speed ** 0.16)) + (0.4275 * temp * (w_speed ** 0.16)))
        all_chill.append(f'{chill:>3}')
        if len(all_temp) < 18:
            all_temp.append(f'{temp:>3}')

print('                                       ','Temperature oF')
print('          Calm',*all_temp, '\n', sep=" ")
for row in range(12):
    if row == 5:
        print('Wind(mph)', all_w_speed[row], '', *all_chill[row * 18:(row + 1) * 18], sep=" ")
    else:
        print('         ',all_w_speed[row],'', *all_chill[row*18:(row+1)*18], sep=" ")
