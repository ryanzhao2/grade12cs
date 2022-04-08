def bubble_sort(a_list):
    index_of_last_unsorted_item = len(a_list)
    swapped = True
    while swapped:
        swapped = False

        for i in range(0, index_of_last_unsorted_item - 1):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                swapped = True
        index_of_last_unsorted_item -= 1
    print(a_list)
a = [5, 4, 6, 2, 4, 6, 7, 8, 1]
bubble_sort(a)

def selection_sort(a_list):
    for i in range(len(a_list)-1):
        index_min = i
        minimum = a_list[i]
        for j in range(i+1, len(a_list)):
            if a_list[j] < minimum:
                index_min = j
                minimum = a_list[j]
        a_list[i], a_list[index_min] = a_list[index_min], a_list[i]

    print(a_list)
a = [300, 500, 600, 100, 450023, 36, 29, 16, 21, 22, 32, 35, 2, 40, 11, 3, 15, 17, 2, 3]
selection_sort(a)

def insertion_sort(a_list):
    index_sorted = 0
    for i in range(1, len(a_list)):
        element = a_list[i]
        a_list.pop(i)
        unsorted = i
        for j in range(index_sorted, -1, -1):
            if a_list[j] > element:
                unsorted = j
            else:
                break
        a_list.insert(unsorted, element)
        index_sorted += 1

    print(a_list)
b = [300, 500, 600, 100, 450023, 36, 29, 16, 21, 22, 32, 35, 2, 40, 11, 3, 15, 17, 2, 3]
insertion_sort(b)
