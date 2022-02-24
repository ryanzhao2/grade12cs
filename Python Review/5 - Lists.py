#Q4
# def is_sorted(a_list):
#     new_list = a_list.copy()
#     new_list.sort()
#     if a_list == new_list:
#         return True
#     return False
#
# print(is_sorted([1, 2, 2]))

#Q5

# def has_duplicates(a_list):
#     new_list = []
#     for i in range(len(a_list)):
#         if a_list[i] in new_list:
#             return True
#         elif a_list[i] not in new_list:
#             new_list.append(a_list[i])
#     return False
#
# print(has_duplicates([1, 2, 3, 4, 5, 2]))
#

#Q6
# import random
# u = []
# counts = [0,0,0,0,0,0,0,0,0,0]
# loop_num = 1000
# for i in range(loop_num):
#     u.append(random.randint(0, 9))
#
# for num in u:
#     counts[num] += 1
#
# for char in counts:
#     print(f'{char/loop_num*100:>.1f}%')
#

