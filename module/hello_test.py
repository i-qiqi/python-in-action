import hello 

# 1. 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 2. 类似_xxx和__xxx这样的函数或变量就是非公开的（private），
# 不应该被直接引用
# 3. private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法
# 可以完全限制访问private函数或变量
# print(hello.__name__)
# print(hello.__doc__)
# print(hello.__author__)

hello_name = hello.greeting(hello.get_name()[:3])
print(hello_name)