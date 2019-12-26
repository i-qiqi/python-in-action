import time, sys, queue, random
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

#由于这个QueueMananger只从网络上获取Queue,
#所以注册时只提供名字：
QueueManager.register('get_task')
QueueManager.register('get_result')

#连接到服务器，也就是运行task_master.py的机器：
server_addr='127.0.0.1'
print('Connect to server %s ...' % server_addr)
conn = QueueManager(address=(server_addr, 5000), authkey=b'abc')
try:
    conn.connect()
except:
    print('连接失败')
    sys.exit()

task = conn.get_task()
result = conn.get_result()

# 从task队列取任务，并把结果写入result队列：
while not task.empty():
    try:
        n = task.get(timeout=1)
        print('run task %d * %d ...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        sleeptime = random.randint(2,5)
        time.sleep(sleeptime)
        time.sleep(1)
        rt = (r, sleeptime)
        result.put(rt)
    except queue.Empty:
        print('task queue is empty')

# 处理结束：
print('worker exit ...')

if __name__ == '__main__':
    pass