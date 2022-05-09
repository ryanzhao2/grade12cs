#
# import random
#
# class PostSecondary:
#     def __init__(self, name):
#         self._name = name
#         self._students = []
#         self._applicants = []
#
#     def name(self):
#         return self._name
#
#     def type(self):
#         return self._type
#
#     def __str__(self):
#         return (f'{self._name} with {len(self._students)} students enrolled')
#
#     def __repr__(self):
#         return (f'class PostSecondary: name={self._name}, students={self._students}, applicants={self._applicants}')
#
#     def print_applicants(self):
#         s = ""
#         for a in self._applicants:
#             s += a.__str__() + "\n"
#         return s
#
#     def get_applicants(self):
#         return self._applicants
#
#     def print_students(self):
#         s = ""
#         for a in self._students:
#             s += a.__str__() + "\n"
#         return s
#
#     def get_students(self):
#         return self._students
#
#     def add_student(self, student):
#         if student not in self._students:
#             self._students.append(student)
#
#     def add_applicant(self, applicant):
#         if applicant not in self._applicants:
#             self._applicants.append(applicant)
#
#     def reject_application(self, applicant):
#
#         if applicant in self._applicants:
#             self._applicants.remove(applicant)
#
# class Student:
#
#     def __init__(self, name, courses, average):
#         self._name = name
#         self._courses = courses
#         self._average = average
#
#     def name(self):
#         return self._name
#
#     def courses(self):
#         return self._courses
#
#     def average(self):
#         return self._average
#
#     def __str__(self):
#         return (f'{self._name:<10}, average={self._average:<4}, courses={self._courses}')
#
#     def __repr__(self):
#         return (f'class Student name={self._name}, avg={self._average}, courses={self._courses}')
#
#
# class College(PostSecondary):
#
#     def accept_applications(self):
#         for student in self._applicants:
#             c = student.courses()
#             if student.average() > 80:
#                 if "ENG4U" in c or "ENG4C" in c and "MHF4U" in c or "MCT4M" in c:
#                     self._students.append(student)
#
# class University(PostSecondary):
#
#
#     def accept_applications(self):
#         for student in self._applicants:
#             c = student.courses()
#             print(student)
#             if student.average() > 85 and "ENG4U" in c and "MHF4U" in c and "ICS4U" in c:
#                     self._students.append(student)
#
#
#
# def generate_random_students():
#     names = ['Nabeela Gentry', 'Ishika Lutz', 'Sullivan Johnston', 'Rhiannan Lambert', 'Elijah Odling', 'Hanna Salazar',
#              'Kimora Nicholson', 'Siobhan Samuels', 'Bianka Steadman', 'Sianna Franco', 'Sierra Greaves',
#              'Ailish Pemberton', 'Katie Luna', 'Jak Garcia', 'Summer-Louise Hughes', 'Riley Hancock', 'Garfield Moss',
#              'Karishma Hodgson', 'Darren Castaneda', 'Tasneem Dalton', 'Leanne Turner', 'Priyanka Read',
#              'Mahnoor Paine', 'Savannah Lamb', 'Waseem Wynn', 'Ruben Hartley', 'Izzie Richardson', 'Cem Scott',
#              'Eren Hood', 'Marc Lane']
#     courses = ["MHF4U", "ENG4U", "ICS4U", "MCT4M", "ENG4C", "MDM4U", "EWC4U"]
#
#     all_students = []
#
#     for n in names:
#
#         # pick 4 unique courses
#         courseList = []
#         while len(courseList) < 4:
#             c = random.choice(courses)
#             if c not in courseList:
#                 courseList.append(c)
#
#         avg = random.choice([70, 75, 80, 85, 90, 95])
#
#         s = Student(n, courseList, avg)
#         all_students.append(s)
#
#     return all_students
#
#
# def load_applicants(institution, list_students):
#     for current_student in list_students:
#         institution.add_applicant(current_student)
#
#
# def main():
#     # imagine that we created even more institutions
#     guelph_university = University("Guelph")
#     mohawk_college = College("Mohawk")
#     all_postsecondary = [guelph_university, mohawk_college]
#
#     # generate random students
#     all_students = generate_random_students()
#
#     # add applications to institution database
#     for institution in all_postsecondary:
#         load_applicants(institution, all_students)
#
#     for institution in all_postsecondary:
#         print(f'\n\n{institution.name()}')
#         print("Applicants are")
#         print("-" * 30)
#         print(institution.print_applicants())
#
#     # perform the acceptance check for applicants
#     for institution in all_postsecondary:
#         institution.accept_applications()
#
#     for institution in all_postsecondary:
#         print(f'\n\n{institution.name()}')
#         print("Acceptances go out to")
#         print("-" * 30)
#         print(institution.print_students())
#
# main()

#
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

    def __eq__(self, otherCard):

        return self.value() == otherCard.value() and self.suit() == otherCard.suit()

    def __lt__(self, otherCard):

        return self.value() < otherCard.value()

    def __gt__(self, otherCard):

        return self.value() > otherCard.value()

    def __str__(self):
        return f'{self._value} of {self._suit}'

    def __repr__(self):
        return f'class Card(value={self._value}, suit={self._suit})'


class Deck:
    _numCards = 52
    _cardValues = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    _suits = ['hearts', 'spades', 'clubs', 'diamonds']

    def __init__(self):

        self._cards = self._generateCards()

    @classmethod
    def _generateCards(cls):

        d = []
        for s in cls._suits:
            for v in cls._cardValues:
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

        for i in range(0, 10):
            random.shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def empty(self):
        return len(self._cards) == 0

    def deal(self):
        return self._cards.pop(0)


class Canasta(Deck):
    def __init__(self):
        self._num_deck = Canasta._generateCards()
        self._num_deck *= 3
        for i in range(6):
            self._num_deck.append(Card(0, 'joker'))

    def __str__(self):
        return f'{self._num_deck}'

class Euchre(Deck):

    def __init__(self):
        self._new_deck = []
        self._num_deck = Euchre._generateCards()
        for card in self._num_deck:

            if card.value() <= 8 and card.value() >= 2:

                self._new_deck.append(card)
        for c in self._new_deck:
            self._num_deck.remove(c)


    def __str__(self):
        return f'{self._num_deck}'



class BlackJack(Deck):

    def __init__(self):

        self._cards = BlackJack._generateCards() * 8
        self.shuffle()

    def __str__(self):
        return f'{self._cards}'



# print(Canasta())
print(Euchre())
# bj = BlackJack()
# print(bj)