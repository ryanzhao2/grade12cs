def bubble_sort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list)-1-i):
            print(j, i)
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                swapped = True
print(bubble_sort([5,4,3,2,1]))
