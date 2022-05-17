class Node:
    def __init__(self, value):
        self.value = value
        self.link = None

class LinkedList:
    def __init__(self):
        self.firstNode = None

    def add(self, newNode):
        # The linked list is empty
        if(self.firstNode is None):
            self.firstNode = newNode
        else:
            # Add to the end of the linked list
            currentNode = self.firstNode
            while currentNode is not None:
                # Found the last element
                if(currentNode.link is None):
                    currentNode.link = newNode
                    break
                else:
                    currentNode = currentNode.link


    def addBefore(self, valueToFind, newNode):
        currentNode = self.firstNode # point to firstNode
        previousNode = None
        while currentNode.value != valueToFind: # while currentNode.data is not equal to valueToFind, move currentNode to next node and keep track of previous node i.e. previousNode
            previousNode = currentNode # keep tack of previous node
            currentNode = currentNode.link # move to next node

        previousNode.link = newNode # previous node will point to new node
        previousNode = previousNode.link # move previous node to newly inserted node
        previousNode.link = currentNode # previous node ka next will to currentNode

    def printClean(self):
        currentNode = self.firstNode
        while currentNode is not None:
            print(f'[{currentNode.value}]')
            if(currentNode.link != None):
                currentNode = currentNode.link
            else:
                return

testLinkedList = LinkedList()
testLinkedList.add(Node(2))
testLinkedList.add(Node(3))
testLinkedList.addBefore(3, Node(5))
testLinkedList.printClean()
