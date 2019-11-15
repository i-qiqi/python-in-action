from closure import count,count_1,addx,foo, foo_err,create
from closure import make_filter
# f1, f2, f3= count_1()
# print(f1(), f2(), f3())

# c = addx(8)
# print(c.__name__, type(c), c(10))

# foo()

# c = foo_err()
# print(c())
# player = create()
# print(player([1, 0], 10))
# print(player([0, 1], 20))
# print(player([-1, 0], 10))

filter = make_filter("pass")
filter_res = filter("result.txt")
print(filter_res)