
import threading

class Student(object):
    def __init__(self, name):
        self.name = name


# def process_student(name):
#     std = Student(name)
#     do_task_1(std)
#     do_task_2(std)

# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_1(std)

# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)

# global_dict = {}

# def std_thread(name):
#     std = Student(name)
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()

# def do_task_1():
#     std = global_dict[threading.current_thread()]

# def do_task_2():
#     std = global_dict[threading.current_thread()]

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',), name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()

# windows下创建进程开销巨大，os能同时运行的进程数也是有限的
#IIS服务器，Apache服务器
# 多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个
# 进程崩溃，因为所有线程共享进程的内存
# 对应到Python语言，单线程的异步编程模型称为协程