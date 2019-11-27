def foo(s):
   return 10 / int(s)

def bar(s):
    return foo(s) * 2

def multi_layer_test():
    # try:
        bar('0')
    # except Exception as e:
    #     print('Error:',e)
    # finally:
    #     print('finally...')

def division_by_zero():
    try:
        print('try...')
        r = 10/int('a')
        print('result: ', r)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('No err!')
    finally:
        print('finally...')
    print('END')

# 所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了
def exception_hierachy():
    try:
        print('try...')
        r = 10/int('a')
        print('result: ', r)
    except ValueError as e:
        print('ValueError:', e)
    except UnicodeError:
        print('UnicodeError')
    finally:
        print('finally...')
    print('END')

if __name__ == '__main__':
    # division_by_zero()
    # exception_hierachy()
    multi_layer_test()