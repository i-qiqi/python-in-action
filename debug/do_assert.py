import logging
# 日志级别：debug, info, warning, error
# 配置日志输出位置
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    # print('>>> n = %d' % n)
    assert n != 0, 'n is zero!'
    return 10 / n
    
def main():
    foo('0')

if __name__ == '__main__':
    # main()
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)

