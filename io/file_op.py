import os

# print(os.name)
# # print(os.uname())# windows上不提供
# print(os.environ.get('PATH'))
# print(os.environ.get('x','default'))
# parent_path = os.path.abspath('.')
# print(parent_path)
# new_dir = os.path.join(parent_path , 'testdir')
# # os.mkdir(new_dir)
# print(new_dir)
# os.rmdir(new_dir)
path_segs = os.path.split("\\Users\zbq\Desktop\python-in-action\io\\bytes_io.py") # splitext
print(path_segs)
# os.rename('gbk.txt', 'gbk_2312.txt')
# os.rename('gbk_2312.txt', 'gbk.txt')

files_filtered = [x for x in os.listdir('.') if os.path.isfile(x)]
print(files_filtered)

files_filtered = [x for x in os.listdir('.') 
if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
print(files_filtered)
