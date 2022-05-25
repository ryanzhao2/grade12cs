from Queue import *
from CustomerLibrary import *

'''
@author: aaronQuesnelle
2019 for ICS4U
2022 updated for ICS4U
'''


class CashierQueue(Queue):

    def __init__(self):
        '''
        Create an empty queue.
        '''
        self._length = 0
        self._head = None
        self._tail = None
        self._time_length = 0

    def get_queue_time_length(self):
        return self._time_length

    def insert(self, customer):
        '''
        Similar to insert from Queue class. Also updates time_length attribute
        based on customer numitems.

        Params
        customer is a Customer object
        '''
        newNode = ListNode(customer)

        # if list empty new node is first node
        if (self._head == None):
            self._head = newNode
            self._tail = newNode

        # if list has 1+ items
        else:
            self._tail.newlink(newNode)
            self._tail = newNode

        # increase length by 1
        self._length += 1
        self._time_length += customer.numitems()

    def __str__(self):
        n = self._head
        s = ""
        while (n != None):
            s += str(n.value()) + " "
            n = n.link()

        return f'Total Time: {self._time_length}\nCustomers: [{s}]'


###APPLICATION

def make_cashiers():
    cashiers = []
    for i in range(0, 6):
        c = CashierQueue()
        cashiers.append(c)

    return cashiers


def get_all_customers(filename):
    all_customers = Queue()

    with open(filename, encoding="utf-8") as fileIn:
        for line in fileIn:
            temp = line.strip().split("\t")
            customer = Customer(temp[0], int(temp[1]))
            all_customers.insert(customer)

    return all_customers


def print_cashiers(list_cashiers):
    for cashier in list_cashiers:
        print(f'\n{cashier}')


def main():
    cashiers = make_cashiers()
    all_customers = get_all_customers("customerList.txt")
    time_list = []
    while not all_customers.empty():
        for cashier in cashiers:
            time_list.append(cashier.get_queue_time_length())
        minimum_time = time_list.index(min(time_list))
        cashiers[minimum_time].insert(all_customers.remove())
        time_list = []




    print_cashiers(cashiers)


main()