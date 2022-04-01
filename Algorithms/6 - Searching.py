def binary_search(aList, T):

    ##Set L to 0 and R to n − 1.
    L = 0
    R = len(aList) - 1
    m = (L + R) // 2

    while (L <= R):
        ##If L > R, the search terminates as unsuccessful.
        if (L > R):
            return -1

        ##Set m (the position of the middle element) to the floor (the largest previous integer) of (L + R) / 2.
        else:
            m = (L + R) // 2

            ##If Am < T, set L to m + 1 and go to step 2.
            if aList[m] < T:
                L = m + 1

            ##If Am > T, set R to m – 1 and go to step 2.
            elif aList[m] > T:
                R = m - 1

            ##Now Am = T, the search is done; return m.
            else:
                return m


    return m


def insert_binary_search(value, a_list):
    call_binary = binary_search(a_list, value)
    minimum = min(a_list)
    maximum = max(a_list)
    if value < minimum:
        a_list.insert(0, value)
    elif value > maximum:
        a_list.insert(len(a_list), value)
    else:
        a_list.insert(call_binary, value)
    print(call_binary)
    print(a_list)
a = [3, 4, 4, 6, 8, 10, 14, 14, 14, 14]
insert_binary_search(5, a)