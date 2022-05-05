# import random
#
#
# class ParttimeEmployee:
#
#     def __init__(self, name, schedule, rate):
#         self._name = name
#         self._schedule = schedule  # as a list of days
#
#         self._hourly_rate = rate
#
#     def __str__(self):
#         return f'{self._name:<20} {self._schedule} ${self._hourly_rate}/hr'
#
#     def __repr__(self):
#         return f'ParttimeEmployee(name={self._name}, schedule={self._schedule}, rate={self._rate}'
#
#     def name(self):
#         return self._name
#
#     def schedule(self):
#         return " ".join(self._schedule)
#
#     def changeSchedule(self, schedule):
#         self._schedule = schedule
#
#     def hourlyrate(self):
#         return round(self._hourly_rate, 2)
#
#     def raiseSalary(self, percentage):
#         self._hourly_rate = round(self._hourly_rate * (1 + percentage / 100), 2)
#
#     def generate_weekly_paycheck(self, hours_worked):
#         earnings = self._hourly_rate * hours_worked
#         return earnings
#
#     def PTO(self):
#         pass
#         # return 10
#         # this function would determine the paid time off for different employees
#
#
# class FulltimeEmployee:
#
#     def __init__(self, name, schedule, rate):
#         self._name = name
#         self._schedule = schedule  # as a list of days
#
#         self._hourly_rate = rate
#
#     def __str__(self):
#         return f'{self._name:<20} {self._schedule} ${self._hourly_rate}/hr'
#
#     def __repr__(self):
#         return f'FulltimeEmployee(name={self._name}, schedule={self._schedule}, rate={self._rate}'
#
#     def name(self):
#         return self._name
#
#     def schedule(self):
#         return " ".join(self._schedule)
#
#     def changeSchedule(self, schedule):
#         self._schedule = schedule
#
#     def hourlyrate(self):
#         return round(self._hourly_rate, 2)
#
#     def raiseSalary(self, percentage):
#         self._hourly_rate = round(self._hourly_rate * (1 + percentage / 100), 2)
#
#     def generate_weekly_paycheck(self, hoursworked):
#         earnings = self._hourly_rate * 40
#         earnings += earnings * 0.10
#         return earnings
#
#     def PTO(self):
#         pass
#         #return 10
#         #this function would determine the paid time off for different employees
#
# class Manager:
#
#     def __init__(self, name, schedule, salary):
#         self._name = name
#         self._schedule = schedule  # as a list of days
#
#         self._salary = salary
#
#     def __str__(self):
#         return f'{self._name:<20} {self._schedule} ${self._salary}/annum'
#
#     def __repr__(self):
#         return f'Manager(name={self._name}, schedule={self._schedule}, salary={self._rate}'
#
#     def name(self):
#         return self._name
#
#     def schedule(self):
#         return " ".join(self._schedule)
#
#     def changeSchedule(self, schedule):
#         self._schedule = schedule
#
#     def hourlyrate(self):
#         return round(self._salary / 52 / 44, 2)
#
#     def raiseSalary(self, percentage):
#         self._salary = round(self._salary * (1 + percentage / 100), 2)
#
#     def generate_weekly_paycheck(self, hoursworked):
#         earnings = self._salary / 52
#
#         return earnings
#
#     def PTO(self):
#         pass
#         #return 10
#         #this function would determine the paid time off for different employees
#
# # MAIN
# def make_random_schedule(num_days):
#     days = ['M', 'T', 'W', 'H', 'F', 'S', 'S']
#
#     schedule = []
#     while len(schedule) < num_days:
#         day = random.choice(days)
#         if day not in schedule:
#             schedule.append(day)
#
#     return schedule
#
#
# def make_managers(emp_list, names, qty):
#     for i in range(qty):
#         name = random.choice(names)
#         names.remove(name)
#         salary = random.randrange(50000, 80000, 10000)
#         m = Manager(name, ['M', 'T', 'W', 'H', 'F'], salary)
#
#         emp_list.append(m)
#
#
# def make_fulltime(emp_list, names, qty):
#     for i in range(qty):
#         name = random.choice(names)
#         names.remove(name)
#         salary = random.randint(14, 25)
#         f = FulltimeEmployee(name, make_random_schedule(5), salary)
#
#         emp_list.append(f)
#
#
# def make_parttime(emp_list, names, qty):
#     for i in range(qty):
#         name = random.choice(names)
#         names.remove(name)
#         salary = random.randint(11, 15)
#
#         p = ParttimeEmployee(name, make_random_schedule(3), salary)
#
#         emp_list.append(p)
#
#
# def make_random_employees():
#     names = ['Nabeela Gentry',
#              'Ishika Lutz',
#              'Sullivan Johnston',
#              'Rhiannan Lambert',
#              'Elijah Odling',
#              'Hanna Salazar',
#              'Kimora Nicholson',
#              'Siobhan Samuels',
#              'Bianka Steadman',
#              'Sianna Franco',
#              'Sierra Greaves',
#              'Ailish Pemberton',
#              'Katie Luna',
#              'Jak Garcia',
#              'Summer-Louise Hughes',
#              'Riley Hancock',
#              'Garfield Moss',
#              'Karishma Hodgson',
#              'Darren Castaneda',
#              'Tasneem Dalton',
#              'Leanne Turner',
#              'Priyanka Read',
#              'Mahnoor Paine',
#              'Savannah Lamb',
#              'Waseem Wynn',
#              'Ruben Hartley',
#              'Izzie Richardson',
#              'Cem Scott',
#              'Eren Hood',
#              'Marc Lane']
#
#     employee_list = []
#
#     make_managers(employee_list, names, 2)
#     make_fulltime(employee_list, names, 10)
#     make_parttime(employee_list, names, len(names))
#
#     return employee_list
#
#
# def run_payroll(employee_list):
#     paycheck_info = []
#
#     for employee in employee_list:
#         # print(type(employee))
#
#         hours = random.randint(10, 20)
#
#         pay_info = employee.generate_weekly_paycheck(hours)
#
#         paycheck_info.append([employee.name(), employee.schedule(), hours, pay_info])
#
#     return paycheck_info
#
#
# def main():
#     list_of_employees = make_random_employees()
#     for e in list_of_employees:
#         print(e)
#
#     paycheck_list = run_payroll(list_of_employees)
#
#     for p in paycheck_list:
#         print(p)
#
#
# main()
#
#
#

import random


class Student:

    def __init__(self, name, courses, average):
        self._name = name
        self._courses = courses
        self._average = average

    def name(self):
        return self._name

    def courses(self):
        return self._courses

    def average(self):
        return self._average

    def __str__(self):
        return (f'{self._name:<10}, average={self._average:<4}, courses={self._courses}')

    def __repr__(self):
        return (f'class Student name={self._name}, avg={self._average}, courses={self._courses}')


class College:

    def __init__(self, name):
        self._name = name
        self._students = []
        self._applicants = []

    def name(self):
        return self._name

    def type(self):
        return self._type

    def __str__(self):
        return (f'{self._name} with {len(self._students)} students enrolled')

    def __repr__(self):
        return (f'class PostSecondary: name={self._name}, students={self._students}, applicants={self._applicants}')

    def print_applicants(self):
        s = ""
        for a in self._applicants:
            s += a.__str__() + "\n"
        return s

    def get_applicants(self):
        return self._applicants

    def print_students(self):
        s = ""
        for a in self._students:
            s += a.__str__() + "\n"
        return s

    def get_students(self):
        return self._students

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)

    def add_applicant(self, applicant):
        if applicant not in self._applicants:
            self._applicants.append(applicant)

    def reject_application(self, applicant):

        if applicant in self._applicants:
            self._applicants.remove(applicant)

    def accept_applications(self):
        self._students.append(self._applicants)

class University:
    def __init__(self, name):
        self._name = name
        self._students = []
        self._applicants = []

    def name(self):
        return self._name

    def type(self):
        return self._type

    def __str__(self):
        return (f'{self._name} with {len(self._students)} students enrolled')

    def __repr__(self):
        return (f'class PostSecondary: name={self._name}, students={self._students}, applicants={self._applicants}')

    def print_applicants(self):
        s = ""
        for a in self._applicants:
            s += a.__str__() + "\n"
        return s

    def get_applicants(self):
        return self._applicants

    def print_students(self):
        s = ""
        for a in self._students:
            s += a.__str__() + "\n"
        return s

    def get_students(self):
        return self._students

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)

    def add_applicant(self, applicant):
        if applicant not in self._applicants:
            self._applicants.append(applicant)

    def reject_application(self, applicant):

        if applicant in self._applicants:
            self._applicants.remove(applicant)

    def accept_applications(self):
        self._students.append(self._applicants)




def generate_random_students():
    names = ['Nabeela Gentry', 'Ishika Lutz', 'Sullivan Johnston', 'Rhiannan Lambert', 'Elijah Odling', 'Hanna Salazar',
             'Kimora Nicholson', 'Siobhan Samuels', 'Bianka Steadman', 'Sianna Franco', 'Sierra Greaves',
             'Ailish Pemberton', 'Katie Luna', 'Jak Garcia', 'Summer-Louise Hughes', 'Riley Hancock', 'Garfield Moss',
             'Karishma Hodgson', 'Darren Castaneda', 'Tasneem Dalton', 'Leanne Turner', 'Priyanka Read',
             'Mahnoor Paine', 'Savannah Lamb', 'Waseem Wynn', 'Ruben Hartley', 'Izzie Richardson', 'Cem Scott',
             'Eren Hood', 'Marc Lane']
    courses = ["MHF4U", "ENG4U", "ICS4U", "MCT4M", "ENG4C", "MDM4U", "EWC4U"]

    all_students = []

    for n in names:

        # pick 4 unique courses
        courseList = []
        while len(courseList) < 4:
            c = random.choice(courses)
            if c not in courseList:
                courseList.append(c)

        avg = random.choice([70, 75, 80, 85, 90, 95])

        s = Student(n, courseList, avg)
        all_students.append(s)

    return all_students


def load_applicants(institution, list_students):
    for current_student in list_students:
        institution.add_applicant(current_student)


def main():
    # imagine that we created even more institutions
    guelph_university = University("Guelph")
    mohawk_college = College("Mohawk")
    all_postsecondary = [guelph_university, mohawk_college]

    # generate random students
    all_students = generate_random_students()

    # add applications to institution database
    for institution in all_postsecondary:
        load_applicants(institution, all_students)

    for institution in all_postsecondary:
        print(f'\n\n{institution.name()}')
        print("Applicants are")
        print("-" * 30)
        print(institution.print_applicants())

    # perform the acceptance check for applicants
    for institution in all_postsecondary:
        institution.accept_applications()

    for institution in all_postsecondary:
        print(f'\n\n{institution.name()}')
        print("Acceptances go out to")
        print("-" * 30)
        print(institution.print_students())


main()


