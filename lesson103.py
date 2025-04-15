def outer():
    x = 'python'
    def inner():
        print(x)
    return inner
fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print('-'*80)

def outer():
    x = [1,2,3]
    print('outer:', hex(id(x)), x)
    def inner():
        x = [4,5,6]
        print('inner:', hex(id(x)), x)
    return inner, x
fn, x = outer()
fn()
print('-'*80)

def outer():
    x = 'python'
    print('outer:', hex(id(x)), x)
    def inner():
        x = 'python'
        print('inner:', hex(id(x)), x)
    return inner, x
fn, x = outer()
fn()
print('-'*80)

def outer():
    x = 'python'
    print('outer:', hex(id(x)), x)
    def inner():
        x = 'python'
        print('inner:', hex(id(x)), x)
    return inner, x
fn, x = outer()
fn()
print('-'*80)

def outer():
    x = [1,2,3]
    print('outer  :', hex(id(x)), x)
    def inner():
        y = x
        print('inner-x:', hex(id(x)), x)
        print('inner-y:', hex(id(y)), y)
    return inner, x
fn, x = outer()
print(fn.__closure__)
fn()
print('-'*80)

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0)))
print()

print(fn())
print(fn.__closure__)
print(hex(id(1)))
print('.'*80)

def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count
    def inc2():
        nonlocal count
        count += 1
        return count
    return inc1, inc2
fn1, fn2 = outer()
print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print()

print(fn1())
print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print()

print(fn2())
print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print()
print('.'*80)

def pow(n):
    def inner(x):
        return x ** n
    return inner
square = pow(2)
print(square.__closure__)
print(hex(id(2)))

print(square)
print()

cube = pow(3)
print(cube.__closure__)
print(hex(id(3)))
print(cube(5))
print('.'*80)

def adder(n):
    def inner(x):
        return x + n
    return inner
add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1.__closure__)
print(add_2.__closure__)
print(add_3.__closure__)
print(add_1(10))
print(add_2(10))
print(add_3(10))
print('.'*80)

from pprint import pprint
adders = []
for n in range(1,4):
    adders.append(lambda x: x+n)
pprint(adders)
print(n)

print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print()
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print('.'*80)



