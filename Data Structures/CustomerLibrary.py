class Customer:

    def __init__(self, idno, numitems):

        self._id = idno
        self._numitems = numitems

    def numitems(self):
        return self._numitems

    def __str__(self):
        return (f'({self._id}, {self._numitems} items)') 
