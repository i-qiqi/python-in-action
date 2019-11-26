# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，
# 执行结果就是动态创建出一个Hello的class对象
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello, %s.' % name)
    
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self, name='world'):
    print('Hello, %s.' % name)

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        # 1. 当前准备创建的类的对象 2. 类的名字 3. 类继承的父类集合 4. 类的方法集合
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass



if __name__ == '__main__':
    # type(class名称，　父类元组，class方法名称与函数绑定)
    # Hello = type('Hello', (object,) , dict(hello=fn))
    # h = Hello()
    # h.hello()
    # print(type(Hello))
    # print(type(h))
    L = MyList()
    L.add(1)
    L.add(2)
    print(L)