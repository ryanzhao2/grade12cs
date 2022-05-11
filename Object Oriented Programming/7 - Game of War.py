import random


class Card:
    _valueDictionary = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}

    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    def value(self):

        if self._value in Card._valueDictionary:
            return Card._valueDictionary[self._value]
        else:
            return self._value

    def suit(self):
        return self._suit

    def __str__(self):
        return f'{self._value} of {self._suit}'

    def __repr__(self):
        return f'class Card(value={self._value}, suit={self._suit})'

    def __eq__(self, other_card):
        return self.value() == other_card.value()

    def __lt__(self, other_card):
        return self.value() < other_card.value()

    def __gt__(self, other_card):
        return self.value() > other_card.value()


class Deck:
    _numCards = 52
    _card_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    _suits = ['hearts', 'spades', 'clubs', 'spades']

    def __init__(self):
        self._cards = Deck._generate_cards()

    @classmethod
    def _generate_cards(cls):

        d = []
        for s in cls._suits:
            for v in cls._card_values:
                d.append(Card(v, s))
        return d

    def __getitem__(self, key):

        return self._cards[key]

    def __str__(self):
        s = ""
        for c in self._cards:
            s += c.__str__() + "\n"

        return s

    def shuffle(self):
        for i in range(10):
            random.shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def empty(self):
        if len(self._cards) == 0:
            return True
        return False

    def deal(self):
        return self._cards.pop()

    def deal_pile(self, num):
        card_list = []
        for i in range(num):
            card_list.append(self.deal())
        return card_list

    def add_lots(self, cards):
        self._cards.extend(cards)

class Hand(Deck):
    pass

class Player(Deck):
    def __init__(self, name):
        self._name = name
        self._cards = Deck._generate_cards()


    def __str__(self):
        return f'{self._name}'


def game_of_war():
    d = Deck()
    d.shuffle()
    player1 = Player('1')
    player2 = Player('2')
    player1.add_lots(d.deal_pile(26))
    player2.add_lots(d.deal_pile(26))
    pile = []

    while not player1.empty() and not player2.empty():
        c1 = player1.deal()
        c2 = player2.deal()
        pile.append(c1)
        pile.append(c2)
        if c1 > c2:
            player1.add_lots(pile)
            pile = []

        elif c2 > c1:
            player2.add_lots(pile)
            pile = []

        else:
            if len(player1) >= 4 and len(player2) >= 4:
                for i in range(3):
                    pile.append(player1.deal())
                    pile.append(player2.deal())
            elif len(player1) < 4:
                player2.add_lots(pile)

            else:
                player1.add_lots(pile)
    if len(player2._cards) == 0:
        print(f'winner p1{player1._cards}')
    elif len(player1._cards) == 0:
        print(f'winner p2{player2._cards}')
# Application
def game():
    input("Press any key to continue")


# game()
game_of_war()