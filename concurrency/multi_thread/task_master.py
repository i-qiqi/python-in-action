# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# task_master.py for windows
import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 任务个数
task_number = 5

#发送任务的队列
task_queue = queue.Queue(task_number)

#接收者的队列
result_queue = queue.Queue(task_number)

def gettask():
    return task_queue

def getresult():
    return result_queue

   
#从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass
def test():
    #把两个Queue都注册到网络上，callable参数关联了Queue对象：
    QueueManager.register('get_task', callable=gettask) # 把原先用lambda表达式的地方改为用函数实现
    QueueManager.register('get_result',callable=getresult)

    # 绑定端口5000, 设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1',5000), authkey=b'abc')

    #启动Queue:
    manager.start()
    try:
        #获得通过网络访问的Queue对象
        task = manager.get_task()
        result = manager.get_result()
        # 放几个任务进去：
        for i in range(task_number):
            n = random.randint(0,10000)
            print('Put task %d...' % n)
            task.put(n)

        # 每秒检测一次所有任务都被执行完
        while not result.full():
            time.sleep(1)
        #从result队列读取结果：
        print('try get results...')
        for i in range(result.qsize()-1):
            ans = result.get()
            print('task %s is finished, runtime: %d s' % ans)
    except:
        print('Manager error')
    finally:
        # 关闭
        manager.shutdown()
        print('master exit...')
if __name__ == '__main__':
    freeze_support() # windows下多进程会炸，添加这句可以缓解
    test()