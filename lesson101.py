def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()
outer_func()
print('-'*80)




