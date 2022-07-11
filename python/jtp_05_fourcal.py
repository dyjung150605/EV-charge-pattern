class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal(4, 6)
print(a.add())


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result


a = MoreFourCal(5, 2)
print(a.pow())
