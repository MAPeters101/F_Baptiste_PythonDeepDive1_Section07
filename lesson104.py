
class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))
print()

b = Averager()
print(b.add(10))
print(b.add(20))
print(b.add(30))
print('-'*80)





