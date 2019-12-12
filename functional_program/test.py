from funcs_lib import my_abs, move, calc, person
import math

# print(my_abs('A'))
print(my_abs(-9))
# 返回值是tuple
# r = move(100 , 100 , 60 , math.pi / 6)
# print(r)

# nums = [1, 2]
# r =  calc(nums)
# print(r)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Adam' ,45 , **extra)

# 迭代器
it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
# print("end...")