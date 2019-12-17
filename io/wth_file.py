# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，
# 并且操作系统同一时间能打开的文件数量也是有限的
# try:
#     f = open('gbk.txt', 'r')
#     print(f.read(6))
# finally:
#     if f :
#         f.close()

# with open('test.txt', 'r')  as f:
#     # print(f.read(7))
#     for line in f.readlines():
#         print(line.strip())  # 去掉\n


# file-like Object
# 像open()函数返回的这种有个read()方法的对象，
# 在Python中统称为file-like Object
# f = open('gbk.txt', 'r' , encoding='gbk')
# print(f.read())


# 写文件
with open('test.txt', 'a') as f:
    f.write('apend a new line')
