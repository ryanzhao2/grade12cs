'''
Created for ICS4U
aaronquesnelle
'''


def binary_search(aList, T):
    '''
    Returns the index of value T in given list aList.
    Returns -1 if value T is not found.

    @param
    aList - list. The list to search within.
    T - value. The value to search for.

    @return
    index - int. The index of the value if found in given list, -1 if not found.
    '''

    ##Set L to 0 and R to n − 1.
    L = 0
    R = len(aList) - 1
    m = (L + R) // 2

    while (aList[m] != T):
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
    call_binary = binary_search(value, a_list)
    minimum = min(a_list)
    if value < minimum:


insert_binary_search()