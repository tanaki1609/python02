"""
Наследование — это возможность создания новых классов
на основе существующих. Главная польза от наследования —
повторное использование существующего кода.
"""


class Person:  # parent
    def can_walk(self):
        print('Init Person')

    def can_breathe(self):
        print('Я могу дышать')


class Doctor(Person):  # subclass, child
    def can_walk(self):
        print('Init Doctor')

    def can_heal(self):
        print('Я могу лечить')


class Dentist(Doctor):
    def can_walk(self):
        print('Init Dentist')


d = Dentist()
d.can_breathe()
d.can_walk()
print(Dentist.__mro__)
