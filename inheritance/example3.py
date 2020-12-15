class NewInteger(int):

    def double(self):
        return self * self


n = NewInteger(10)
print(n.double())
