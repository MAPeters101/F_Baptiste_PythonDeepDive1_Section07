
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

def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()
print(a(10))
print(a(20))
print(a(30))
print()

b = averager()
print(b(10))
print(b(20))
print(b(30))
print()

print(a.__closure__)
print(b.__closure__)
print('-'*80)

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total / count
    return add

a = averager()
print(a(10))
print(a(20))
print(a(30))
print()

b = averager()
print(b(10))
print(b(20))
print(b(30))
print('='*80)

class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count

a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))
print()

b = Averager()
print(b.add(10))
print(b.add(20))
print(b.add(30))
print('=-'*40)

from time import perf_counter

print(perf_counter())
print(perf_counter())

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def poll(self):
        return perf_counter() - self.start

t1 = Timer()
print(t1.poll())
print(t1.poll())
print('-'*80)

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()
print(t1())
print(t1())
print('-'*80)

def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll
t2 = timer()
print(t2())
print(t2())
print(t1())
print(t2())



