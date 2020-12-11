# OOP
class Cat:
    name = 'unknown'
    is_black = True

    def __init__(self):
        print('class initialized')  # constructor


Cat.is_white = True

a = Cat()
b = Cat()

a.is_black = False

print(b.is_black)
