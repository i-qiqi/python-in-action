import time
import functools
# 在代码运行期间动态增加功能的=>装饰器
def log(func):
    @functools.wraps(func) # wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s ():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def logx(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s:" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# @log <=> now = now(log)
@log
def now():
    localtime = time.localtime(time.time())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# @logx <=> now = log('execute')(now)
@logx('execute')
def nowx():
    localtime = time.localtime(time.time())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))




#---------------------Test Case------------------------
now()
print(now.__name__)
# nowx = log(now)
nowx()
print(nowx.__name__)



