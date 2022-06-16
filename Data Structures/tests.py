class ListNode:
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
        self._head = None
        self._tail = None
        self._length = 0


    def head(self):
        return self._head

    def tail(self):
        return self._tail