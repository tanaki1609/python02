import random


class Game:
    def __init__(self, doors):
        self.doors = doors
        self.count = len(doors)
        print('Game started')

    def choose_prized_door(self):
        random_door = random.randint(0, self.count-1)  # door number 0
        self.doors[random_door].set_prized(True)
        print("We choose the door: ")

    def choose_your_door(self):
        chosen_door = int(input('Choose your door: [1-%s] ' % self.count))
        self.chosen_door = chosen_door - 1
        self.doors[chosen_door - 1].set_chosen(True)
        print("You choose the door: %s %s" % (chosen_door, ''))

    def open_not_prized_door(self):
        for i in range(self.count):
            if self.doors[i].is_prize == False and self.doors[i].is_chosen == False:
                self.doors[i].set_opened(True)
                print("We opened the door: %s %s" % (i + 1, ''))
                break

    def open_door(self):
        print(self.doors[self.chosen_door].is_prize)


class Door:
    is_opened = False
    is_prize = False
    is_chosen = False

    def set_opened(self, is_opened):
        self.is_opened = is_opened

    def set_prized(self, is_prized):
        self.is_prize = is_prized

    def set_chosen(self, is_chosen):
        self.is_chosen = is_chosen


game = Game([Door(), Door(), Door(), Door(), Door()])
game.choose_prized_door()
game.choose_your_door()
# game.open_not_prized_door()
game.open_door()
