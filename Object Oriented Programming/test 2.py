class book:
    _owner = 'Ryan'
    def __init__(self, pages, title):
        self._pages = pages
        self._title = title

    @classmethod
    def double_price(cls, price):
        return str(price * 2) + f'{cls._owner}'
    @classmethod
    def t_price(price):
        return str(price._pages * 3) + f'{book._owner}'

    def get_pages(self):
        return self._pages

    @staticmethod
    def anything():
        print('nothing')

class comic_book(book):
    def get_title(self):
        return f'comic{self._title}'

class novel(book):
    def get_title(self):
        return f'novel{self._title}'

c = comic_book(100, 'marvel')
n = novel(300, 'harry potter')
print(n.get_title())
b = book(30, 'wimpy kid')
print(n._owner)
print(comic_book.double_price(200))
book.anything()
# dict = {'one': 1, 'two': 2, 'three': 3}
# for key, price in dict.items():
#     print(key, price)
# print(dict.items())