# Polymorphism
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        print(self.a * self.b)


chore = [Rectangle(3, 4)]
for i in chore:
    i.get_area()
