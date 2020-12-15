import random

choices = ['stone', 'scissors', 'paper']


class Game:
    user_choice = 0
    comp_choice = 0

    def start_game(self):
        user = User()
        self.user_choice = user.get_choice() - 1  # 0
        print('Your choice is ' + choices[self.user_choice])

    def computer_choice(self):
        self.comp_choice = random.randint(0, 2)
        print('Computer choice is ' + choices[self.comp_choice])

    def get_winner(self):
        if self.user_choice == self.comp_choice:
            print('Winner not found')
        elif self.user_choice == 0 and self.comp_choice == 1:
            print('You are winner')


class User:
    def get_choice(self):
        return (int(input('Enter a number: [stone, scissors, paper]')))


while True:
    game = Game()
    game.start_game()
    game.computer_choice()
    game.get_winner()
