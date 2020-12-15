# Encapsulation
class BankAccount:
    name = 'Kanat'          # public
    _balance = 0            # protected
    __passport = 'AN5243345'# private
    def __init__(self, name):
        self.name = name

    def get_passport(self):
        return self.__passport
b = BankAccount("Azamat")
print(b.name)
print(b.get_passport())
