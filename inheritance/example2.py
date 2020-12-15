class Robot:
    def can_walk(self):
        print('Robot walk')

    def can_kill(self):
        print('kill')


class Police:
    def can_walk(self):
        print('Police walk')

    def can_talk(self):
        print('talk')


class RoboCop(Police, Robot):
    def can_walk(self):
        print('RoboCop walk')
        self.can_kill()


r = RoboCop()
r.can_walk()
print(RoboCop.__mro__)
