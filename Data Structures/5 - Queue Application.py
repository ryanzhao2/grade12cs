import math
from Queue import Queue
'''
Implementing a radix sort
Aaron Quesnelle
June 2020

'''
'''
@author: aaronQuesnelle
2018 for ICS4U

'''

def radixSort(aList):
    # calculate length of longest digit

    numberDigits = int(math.log(abs(max(aList)), 10) + 1)

    # generate a list of 10 queues to hold numbers during the sort
    lou = [Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]
    # this could be a queue of queues but since it has an absolute length
    # an array/list is the most appropriate data type

    # lou is a list of buckets (queues)

    # start sort
    # outside loop runs same number of times as there are digits in longest number
    for digit in range(0, numberDigits):
        # iterate through the dequeued numbers
        # this is the list of numbers
        for item in aList:
        # extract the particular digit you are sorting on this loop
            index = int((item / 10 ** digit) % 10)

        # put number in appropriate queue
            lou[index].insert(item)
        # dequeue the queues
        aList = []

    # loop through the buckets
        for q in lou:
            while q.empty() != True:
                aList.append(q.remove())
    # return
    return aList

# hardcode a list
numbers = [802, 8001, 102, 3, 7, 98, 143, 43, 129, 29, 45]

result = radixSort(numbers)

print(result)





