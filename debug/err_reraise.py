def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('Value Error!')
        # raise

def test():
    try:
        bar()
    except ValueError as e:
        print("input error")
    finally:
        print('END')

if __name__ == '__main__':
    test()