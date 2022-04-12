#Q1

#a) 37
#b) 1 + 8 + 16 + 32 + 64 + 128 + 32768 = 33017

#Q2
#1001 1100

#Q3
#You cannot use 8 bits to represent -400 because the smallest signed number you can get with 8 bits is -128

#Q4
# def DecimalToBinary(num):
#         if num >= 1:
#            DecimalToBinary(num // 2)
#         print(num % 2)
#
# DecimalToBinary(52)

#Q5

def ride_wait_time(p):
    trains = 3
    riders_per_train = 24
    load = 300
    duration = 205
    rides_left = (p // (riders_per_train * trains))
    wait_time_minutes = (rides_left * load + rides_left * duration) / 60
    # for i in range(rides_left, 0, -1):
    #     print((i * load + i * duration) / 60)
    return wait_time_minutes

print(ride_wait_time(200))