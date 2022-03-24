# def bubble_sort(a_list):
#     index_of_last_unsorted_item = len(a_list)
#     swapped = True
#     while swapped:
#         swapped = False
#
#         for i in range(0, index_of_last_unsorted_item - 1):
#             if a_list[i] > a_list[i+1]:
#                 a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
#                 swapped = True
#         index_of_last_unsorted_item -= 1
#     print(a_list)
# a = [5, 4, 6, 2, 4, 6, 7, 8, 1]
# bubble_sort(a)

def selection_sort(a_list):
    for i in range(len(a_list)-1):
        min = a_list[i]
        for j in range(i, len(a_list)-1-i):
            if a_list[j] < min:
                min = a_list[j]
                a_list[i], a_list[j] = a_list[j], a_list[i]
    print(a_list)
a = [36, 29, 16, 21, 22, 32, 35, 2, 40, 11, 3, 15, 17, 2, 3]
selection_sort(a)