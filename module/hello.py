#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 任何模块代码的第一个字符串都被视为模块的文档注释；
'a test module'

__author__ = 'biqi zhu'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello, world")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else :
        print("Too many arguments")

def get_name():
    return __name__
def _get_name_1(name):
    return 'Hello, %s' % name

def _get_name_2(name):
    return 'Hi, %s' % name

# 编程习惯上不应该引用private函数或变量
# 公开greeting()函数，而把内部逻辑用private函数隐藏起来
def greeting(name):
    if len(name) > 3:
        return _get_name_1(name)
    else :
        return _get_name_2(name)

# print('__name__ = %s' % __name__)
if __name__ == '__main__':
    test()