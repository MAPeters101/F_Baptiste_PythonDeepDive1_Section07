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
