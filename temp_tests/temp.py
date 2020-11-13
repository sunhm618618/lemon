#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@File    : temp.py
@Time    : 2020-11-03 10:06
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""


def add(s):
    print(3)
    return 2+s

a = add(2)
print(a)
b = add
print(b(2))
print(type(b))
print("&"*20)