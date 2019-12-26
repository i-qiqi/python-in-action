# 多线程和多进程最大的不同在于，
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，
# 所以，任何一个变量都可以被任何一个线程修改，

import time, threading

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
        # print("temperal balance = %d" % balance)
    print('i = ' , i , ' %s' % threading.current_thread().name)

for i in range(2):  
    print('----%dth test start----' % i)
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    print('----%dth test end---' % i)

