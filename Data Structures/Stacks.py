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
        self._length = 0
        self._top = None

    def empty(self):
        '''
        Determine if the stack is empty.

        Returns
        True if stack is empty, False if not empty.
        '''
        if self._length == 0:
            return True
        return False

    def push(self, value):
        '''
        Add a new item to the top of the stack.
        Similar code to the insertNewFirstNode function from LinkedList

        Parameters
        value is any data type, the value to add to stack
        '''
        newNode = ListNode(value)

        # if list empty new node is first node
        if (self._top == None):
            self._top = newNode

        elif self._top.link != None:
            self._top.newlink(newNode)

        else:
            p = self._top
            while p.link != None:
                p = p.link()
            p.newlink(newNode)


    def pop(self):
        '''
        Removes the top item from the stack and returns the value.
        If stack is empty returns None
        Similar code to the removeFirstNode function from LinkedList

        Returns
        The value of the top item. If empty return None.
        '''
        
        # do nothing if list is empty
        if (self._top != None):

            # if the list has one node, empty list and decrease length
            if (self._top.link() == None):
                a = self._top
                self._top = None
                self._length -= 1
                return a.value()

            # otherwise the list has two or more nodes
            else:
                    # initialize pointers to previous and current node
                # print(self._top)
                b = self._top
                self._top = self._top.link()
                self._length -= 1
                return b.value()


                # advance pointers along the list until current points
                # to last item in list

                # now previous node points to new last node in list
                # length is decreased


    def peek(self):
        '''
        Return the value of the top item in the stack without removing it from the stack.

        Returns
        The value of the top item. If empty return None
        '''
        currentNode = self._top
        while currentNode.link() != None:
            currentNode = currentNode.link()
            
        current_value = currentNode.value()
        return current_value

    def __str__(self):
        '''
        Provide the string representation for the stack to appear
        as a Python List. Used with Python's built in print function.
        [item, item, item]

        Returns
        String
        '''
        s = ""
        n = self._top

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

a_stack = Stack()
a_stack.push('hi')
a_stack.push('hello')
a_stack.push('no')
a_stack.push('bye')
a_stack.pop()
print('\npush\n')
print(a_stack)
#
# a_stack.pop()
# a_stack.pop()
# a_stack.pop()
# print('\npop\n')
# print(a_stack)
#
#
# a_stack.push('yes')
# print(a_stack)
# print(a_stack.peek())
#
# a_stack.push('a')
# a_stack.push('b')
# a_stack.pop()
# a_stack.push('c')
# a_stack.push('d')
# a_stack.pop()
# a_stack.pop()
# a_stack.pop()
# a_stack.push('e')
# a_stack.pop()
# print(a_stack)

# stack1 = Stack()
# stack2 = Stack()
# stack3 = Stack()
# stack1.push('D')
# stack1.push('C')
# stack1.push('B')
# stack1.push('A')
# # print(stack1)
#
# stack2.push(stack1.pop())
# stack2.push(stack1.pop())
# stack3.push(stack1.pop())
# stack3.push(stack1.pop())
# stack3.push(stack2.pop())
# stack3.push(stack2.pop())
# print(stack1)
# print(stack2)
# print(stack3)