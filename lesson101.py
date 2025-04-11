def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()
outer_func()
print('-'*80)

def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()
outer_func()
print('-'*80)

def outer_func():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner:', x)
    inner()
    print('outer:', x)
outer_func()
print('-'*80)

def outer_func():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        print('inner:', x)
    print('outer(before calling inner):', x)
    inner()
    print('outer(after calling inner):', x)
outer_func()
print('-'*80)

def outer():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)
outer()
print('-'*80)

def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    inner1()
    print(x)
outer()
print('-'*80)

# x = 'python'
# print(x)
# def outer():
#     global x
#     x = 'monty'
#     def inner():
#         nonlocal x
#         x = 'hello'
#     print(x)
# outer()

x = 'python'
print(x)
def outer():
    #global x
    x = 'monty'
    def inner():
        nonlocal x
        x = 'hello'
    print(x)
outer()
print()

x = 'python'
print(x)
def outer():
    #global x
    x = 'monty'
    def inner():
        nonlocal x
        x = 'hello'
    inner()
    print(x)
outer()
print(x)
print('='*80)

# x = 'python'
# print(x)
# def outer():
#     global x
#     x = 'monty'
#     def inner():
#         nonlocal x
#         x = 'hello'
#     inner()
#     print(x)
# outer()
# print(x)

x = 'python'
print(x)
def outer():
    global x
    x = 'monty'
    def inner():
        global x
        x = 'hello'
    inner()
    print(x)
outer()
print(x)



print('-'*80)


