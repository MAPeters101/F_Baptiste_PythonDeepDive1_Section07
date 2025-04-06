a = 10
print(a)

def my_func(n):
    c = n**2
    return c

def my_func(n):
    print('global a:', a)
    c = a ** n
    return c

print(my_func(2))
print()

def my_func(n):
    a = 20
    c = a ** n
    return c

print(a)
print(my_func(2))
print(a)
print('-'*80)

def my_func(n):
    global a
    a = 20
    c = a ** n
    return c
print(a)
print(my_func(2))
print(a)
print()

def my_func():
    global var
    var = 'hello world'
    return
#print(var)
my_func()
print(var)
print()

a=10
def my_func():
    print('global a:', a)
my_func()
print()

a=10
def my_func():
    global a
    a = 'hello'
    print('global a:', a)
my_func()
print(a)
print()

a=10
def my_func():
    #print('global a:', a)
    a = 'hello world'
    print(a)
my_func()
print(a)
#print(b)
print('-'*80)

a = 10
f = lambda n: print(a**n)
print(f(2))
print()

print(True)
def print(x):
    #print('In new print function.')
    return 'hello {0}'.format(x)
print('world')
del print
print('world')
print('.'*40)

for i in range(10):
    x = 2 * i
print(x)


