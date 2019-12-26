# 线程是os直接支持的执行单元
# Python 的线程是真正的Posix Thread, 而不是模拟出来的线程
import time, threading
 
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended.' % threading.current_thread().name)

print('Thread %s is running ...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)

