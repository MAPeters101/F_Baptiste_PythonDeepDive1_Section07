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