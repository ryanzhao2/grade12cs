# def bubble_sort(list):
#     for i in range(len(list)):
#         swapped = False
#         for j in range(0, len(list)-1-i):
#             print(j, i)
#             if list[j] > list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#                 swapped = True
# print(bubble_sort([5,4,3,2,1]))
#
# a = [0, 1, 2, 3]
# a.insert(-1, 5)
# print(a)

def remove_x(s):
    if 'x' not in s:
        return s
    elif 'x' != s[0]:
        return s[0] + remove_x(s[1:])
    elif 'x' == s[0]:
        return remove_x(s[1:])
    else:
        return

print(remove_x('xaxaxaxaxa'))
