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


