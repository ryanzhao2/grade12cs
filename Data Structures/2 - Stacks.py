'''

@author: aaronquesnelle
2018 for ICS 4U
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


class Stack:

    def __init__(self):
        '''
        Construct an empty stack with attributes
        length and top (instead of the firstnode)

        '''
        pass

    def empty(self):
        '''
        Determine if the stack is empty.

        Returns
        True if stack is empty, False if not empty.
        '''
        pass

    def push(self, value):
        '''
        Add a new item to the top of the stack.
        Similar code to the insertNewFirstNode function from LinkedList

        Parameters
        value is any data type, the value to add to stack
        '''
        pass

    def pop(self):
        '''
        Removes the top item from the stack and returns the value.
        If stack is empty returns None
        Similar code to the removeFirstNode function from LinkedList

        Returns
        The value of the top item. If empty return None.
        '''
        pass

    def peek(self):
        '''
        Return the value of the top item in the stack without removing it from the stack.

        Returns
        The value of the top item. If empty return None
        '''
        pass

    def __str__(self):
        '''
        Provide the string representation for the stack to appear
        as a Python List. Used with Python's built in print function.
        [item, item, item]

        Returns
        String
        '''
        pass



