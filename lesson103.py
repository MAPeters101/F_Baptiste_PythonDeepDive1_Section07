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





