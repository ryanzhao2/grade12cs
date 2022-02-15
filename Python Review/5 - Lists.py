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
# print(has_duplicates([1, 1]))