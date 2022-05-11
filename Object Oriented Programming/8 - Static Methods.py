import random


class Die:

    def __init__(self):
        self._value = 1
        self._shouldRoll = True

    def value(self):
        return self._value

    def shouldRoll(self):
        return self._shouldRoll

    def markShouldRoll(self, b):
        self._shouldRoll = b

    def roll(self):
        self._value = random.randint(1, 6)

    def __lt__(self, other):
        return self._value < other.value()

    def __gt__(self, other):
        return self._value > other.value()

    def __eq__(self, other):
        return self._value == other.value()

    def __str__(self):
        return self._value

    def __repr__(self):
        return self._value


class Interface:

    @staticmethod
    def printDice(listDice):
        return listDice

    @staticmethod
    def whichDiceToKeep():
        choice = input('Choose a die')
        return markShouldRoll()

    @staticmethod
    def printScore(result, score):
        return 2


class PokerDiceGame:

    def __init__(self):
        self._score = 0
        self._myDice = self._generateDice()

    @classmethod
    def _generateDice(cls):
        d = []

        for i in range(5):
            d.append(Die())

        return d

    def roll(self):

        for d in self._myDice:
            if d.shouldRoll():
                d.roll()

    def markDiceToKeep(self, listIndexes):

        # make all dice possible to roll again
        for index in range(5):
            self._myDice[index].markShouldRoll(True)

        # mark the dice the user chose
        for index in listIndexes:
            self._myDice[index].markShouldRoll(False)

    def comboScoring(self):

        self._score += 50
        return f'Score is still default: straight, 50 points'

    def main(self):

        while self._score < 100:

            self.roll()

            for i in range(2):
                Interface.printDice(self._myDice)

                diceKeep = Interface.whichDiceToKeep()

                self.markDiceToKeep(diceKeep)

                self.roll()

            Interface.printDice(self._myDice)

            result = self.comboScoring()

            Interface.printScore(result, self._score)

            self.markDiceToKeep([])
            input("\n\nPress any key to continue")


p = PokerDiceGame()
p.main()




