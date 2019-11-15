# 闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# https://blog.csdn.net/marty_fu/article/details/7679297
def count():
    fs = []
    for i in range(1,5):
        def f():
            return i * i
        fs.append(f)
    return fs



def count_1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
# 如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，
# 那么内部函数就被认为是闭包(closure)
# addy是一个内部函数，x是外部作用域addx里面，但不在全局作用域里=>addy是一个闭包
def addx(x):
    def addy(y): return x + y
    return addy

# 闭包中不能修改外部作用域的局部变量
def foo():
    m = 0
    def foo1():
        m = 1
        print(m)
    print(m)
    foo1()
    print(m)

def foo_err():
    a = 1
    def bar():
        a = a + 1
        return a
    return bar
