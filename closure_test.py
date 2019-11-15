from closure import count,count_1,addx,foo, foo_err
f1, f2, f3= count_1()
print(f1(), f2(), f3())

c = addx(8)
print(c.__name__, type(c), c(10))

foo()

c = foo_err()
print(c())