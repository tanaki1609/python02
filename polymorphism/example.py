"""
Полиморфизм — это способность программы выбирать различные
реализации при вызове операций с одним и тем же
названием.
"""


class Cat:
    def voice(self):
        print('meow')


class Dog:
    def voice(self):
        print('gav')


class Cow:
    def voice(self):
        print('muu')


chore = [Cat(), Dog(), Cat(), Dog(), Cow()]
for i in chore:
    i.voice()
