# https://www.jellythink.com/archives/530

# 实现了读取文件的基本功能，但是运行时，有时会抛异常
# fileReader = open('students.txt', 'r')
# for row in fileReader:
#     print(row.strip())
# fileReader.close()

# 完成了功能，不简洁
# try:
#     file_reader = open('students.txt', 'r')
#     for row in file_reader:
#         print(row.strip())
# except:
#     print('Read file filed...')
# finally:
#     print('Read end ...')
#     file_reader.close()  

# with语句适用于对资源访问的场景，
# 确保不管使用过程中是否发生异常都会执行必要的“清理”
# with open('students.txt', 'r') as file_reader:
#     for row in file_reader:
#         print(row.strip())

class DBManager(object):
    def __init__(self):
        pass

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        print('__exit__')
        return True

def getInstance():
    return DBManager()
# 自定义上下文管理器来对软件系统中的资源进行管理
# 比如数据库连接、共享资源的访问控制
with getInstance() as dbManagerIns:
    print('with demo')