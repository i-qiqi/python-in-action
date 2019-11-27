class FooErr(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooErr('invalid value: %s' % s)
    return 10 / n

def test():
    foo('0')

if __name__ == '__main__':
    test()