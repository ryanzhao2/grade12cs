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


class ListNode:
    '''
    Class of listNode is a data type which holds a value and a link to the next
    node in a list. This object is used in conjunction with linked list
    '''

    def __init__(self, value):
        self._value = value
        self._link = None

    def value(self):
        return self._value

    def link(self):
        return self._link

    def newlink(self, node):
        self._link = node

    def __str__(self):
        return self._value


class Queue:

    def __init__(self):
        '''
        Create an empty queue.
        '''
        self._head = None
        self._tail = self._head
        # self._head.newlink(self._tail)
        self._length = 0

    pass


    def empty(self):
        '''
        Determine if the queue is empty.

        Returns
        True if queue is empty, False if not.
        '''
        if self._length == 0:
            return True
        else:
            return False




    def insert(self, value):
        '''
        Insert a value at the tail of the queue.
        Similar code to the insertNewLastNode function from LinkedLists

        Params
        value is any data type to be added to queue.
        '''
        newNode = ListNode(value)

        # if list empty new node is first node
        if (self._head == None):
            self._head = newNode
        else:
            # locate last node in list
            p = self._head
            while (p.link() != None):
                p = p.link()
                self._tail = p.link()
            p.newlink(newNode)
            self._tail = newNode
        # increase length by 1
        self._length += 1




    def remove(self):
        '''
        Remove the first item from the head of the queue.
        If list is empty then return None.
        Similar to the removeFirstNode function from LinkedList

        Returns
        value at the head of the queue. If queue is empty return None.
        '''

        # do nothing if list is empty
        if (self._head != None):

            # if the list has one node, empty list and decrease length
            if (self._head.link() == None):
                a = self._head
                self._head = None
                self._tail = self._head
                self._length -= 1
                return a.value()

            # otherwise the list has two or more nodes
            else:
                # initialize pointers to previous and current node
                # print(self._head)
                b = self._head
                self._head = self._head.link()
                self._tail = self._head

                self._length -= 1
                return b.value()




    def peek(self):
        '''
        Return the value of the item at the head of the queue without removing it.
        If queue is empty return None.

        Returns
        The value of the first item. If empty return None.
        '''
        if self._length == 0:
            return None
        return self._head



    def __str__(self):
        '''
        Provide the string representation for the queue to appear
        as a Python List. Used with Python's built in print function.
        [item, item, item]

        Returns
        String
        '''

        s = ""
        n = self._head

        # iterate through list one item at a time until last item reached
        while (n != None):
            # check if last item in list has been reached
            # if so, do not place a comma after the item
            if n.link() != None:

                # check if item is type string. If so, place it in quotations
                if type(n.value()) == str:
                    s += "'" + str(n.value()) + "', "
                else:
                    s += str(n.value()) + ", "
            else:
                # check if item is type string. If so, place it in quotations
                if type(n.value()) == str:
                    s += "'" + str(n.value()) + "'"
                else:
                    s += str(n.value())

            # advance to next item in list
            n = n.link()

        return ("[" + s + "]")


def radixSort(aList):
    # calculate length of longest digit

    numberDigits = int(math.log(abs(max(aList)), 10) + 1)

    # generate a list of 10 queues to hold numbers during the sort
    lou = [Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]
    print(lou)
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
            q.remove()

    # return
    return aList

# hardcode a list
numbers = [802, 8001, 102, 3, 7, 98, 143, 43, 129, 29, 45]

result = radixSort(numbers)

print(result)





