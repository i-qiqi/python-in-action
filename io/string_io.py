from io import StringIO

#StringIO 在内存中读写string
# f = StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# print(f.getvalue())
# print(f.write('Biqi'))
# print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，
# 然后，像读文件一样读取
f = StringIO('Hello!\nHi\nGoodBye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

