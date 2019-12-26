import subprocess
# 子进程并不是自身，而是一个外部进程。
# 我们创建子进程后，还需要控制子进程的输入和输出
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gb2312'))
print('Exit code:', p.returncode)