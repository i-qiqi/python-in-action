import threading, multiprocessing
from multiprocessing import Pool, Process
# 有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
# 必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
# 让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都
# 给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在
# 100核CPU上，也只能用到1个核。
# def loop():
#     x = 0
#     while True:
#          x = x^1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     print(t.name)
#     t.start()
def loop(i):
    x = 0
    print('Thread - ', i)
    while True :
        x = x ^ 1

def proc(i, cpu_count):
    print('Process: ', i)
    for i in range(4):
        t = threading.Thread(target=loop, args=(i,))
        t.start()

if __name__ == '__main__':
    cpu_count = multiprocessing.cpu_count()
    print('cpu count : ', cpu_count)
    p = Pool(cpu_count)
    for i in range(cpu_count):
        p.apply_async(proc,args=(i, cpu_count))
    p.close()
    p.join()
