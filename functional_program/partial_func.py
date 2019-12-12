import functools

# Partial function
# 通过设定参数的默认值，可以降低函数调用的难
def int2(x, base=2):
    return int(x, base)
x = int('12345', base=6)
print(int2('10001'))

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单

int_2 = functools.partial(int, base=2)
print(int_2('10001'))
kw = {'base':2}
print(int('10010',**kw))
print('*'*5)
max2 = functools.partial(max, 10)
x = max2(5,6,7)
print(x)
args = (10, 5, 6, 7)
x = max(*args)
print(x)
