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
        return f'{self._value}'

    def __repr__(self):
        return f'{self._value}'


class Interface(Die):

    @staticmethod
    def printDice(listDice):
        lines = '-'*30
        text = f'Your current dice are . . .\nDice Number: 1  2  3  4  5\n{lines}\nYour Dice are: {listDice}\n\n'
        print(text)

    @staticmethod
    def whichDiceToKeep():
        a_list = []
        text = f'Please type in the Dice numbers of the dice you want to keep\
        \nPlease put a space between your values\nExample:  1 4 5  means \
you want to keep Dice 1 4 5 and reroll Dice 2 3'
        print(text)
        user_choice = (input(f'Dice to keep?'))
        print('\n')
        for i in range(len(user_choice)):
            if user_choice[i] != ' ':
                a_list.append(int(user_choice[i]))
        return a_list


    @staticmethod
    def printScore(result, score):
        print(f'{result}, {score}')

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




