class Dog(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Dog object (name: %s)' % self.name
    __repr__ = __str__  # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1   
    # for ... in
    def __iter__(self):
        return self
    
    def __next__(self):
        # 在python中，会在过程中生成一个元组 c，并且c = (b ,a)，
        # 然后进行a = c[0] ， b = c[1] 的操作
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

if __name__ == '__main__':
    # d = Dog('Michael')
    # print(d)
    for i in Fib():
        print(i)
