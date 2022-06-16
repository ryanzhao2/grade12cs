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
        self._tail = None
        # self._head.newlink(self._tail)
        self._length = 0



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
            self._tail = newNode
        else:
            self._tail.newlink(newNode)
            self._tail = newNode
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
                self._tail = None
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

my_queue = Queue()
my_queue.insert(5)
my_queue.insert(10)
my_queue.insert(15)
my_queue.remove()
print(my_queue)
my_queue.peek()

# queue1 = Queue()
# queue2 = Queue()
# queue3 = Queue()
# queue1.insert('A')
# queue1.insert('B')
# queue1.insert('C')
# queue1.insert('D')
#
# print('BEFOREHAND')
# print(queue1)
# print(queue2)
# print(queue3,'\n')
#
# #insert A B C
# queue2.insert(queue1.remove())
# queue2.insert(queue1.remove())
# queue2.insert(queue1.remove())
#
# #INSERT D
# queue3.insert(queue1.remove())
#
# #INSERT A B
# queue1.insert(queue2.remove())
# queue1.insert(queue2.remove())
#
# #INSERT C
# queue3.insert(queue2.remove())
#
# #INSERT A
# queue2.insert(queue1.remove())
#
# #INSERT B
# queue3.insert(queue1.remove())
#
# #INSERT A
# queue3.insert(queue2.remove())
#
# print('AFTERHAND')
# print(queue1)
# print(queue2)
# print(queue3)


