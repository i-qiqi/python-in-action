import os
from multiprocessing import Process

# print('Process (%s) start...')
# pid = os.fork()
# print(os.getppid())

def run_proc(name, seq):
    print('Run child process %s-%s (%s)...'% (name, seq, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', 1))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')