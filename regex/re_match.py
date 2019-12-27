import re

m1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(m1)

m1 = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(m1)
char_arr = 'a+b+++c'.split('+') # split 方法是严格按照过滤参数设置的，不会感知连续过滤的参数。
print(char_arr)
char_arr = re.split(r'\s+', 'a b   c')
print(char_arr)
char_arr = re.split(r'[\s\,\;]+', 'xa ,b , c;;;   d')
print(char_arr)
m1 = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print(m1.group(1), m1.group(2))
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 贪婪匹配
greedy_match = re.match(r'^(\d+)(0*)$', '102300').groups()
print(greedy_match)
un_greedy_match = re.match(r'^(\d+?)(0*)$', '102333300').groups()
print(un_greedy_match)

# 预编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

gr = re_telephone.match('010-12345').groups()
print(gr)
gr = re_telephone.match('010-8086').groups()
print(gr)