#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : py_demo.py
@Time    : 2020-11-02 14:12
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""

import unittest
import pytest
import sys
import ddt



data = [1,2,3]

# @ddt.ddt
@pytest.mark.success
@pytest.mark.demo
class TestDemo(unittest.TestCase):
    """
    1. 类名，不需要继承 unittest.TestCase
    2. 也可以继承 TestCase (pytest 和 unittest 兼容，)
    3. 测试用例不用类，也是可以的。你可以写成独立的函数
    """

    # def setup

    # @ddt.data(*data)
    def test_demo_success(self):
        assert True

    def test_demo_success_2(self):
        assert False

    def test_demo_success_3(self):
        self.assertEqual(1, 3)

    @pytest.mark.skipif(sys.platform == 'linux', reason='window系统')
    def test_demo_success_4(self):
        pass


@pytest.mark.skip
@pytest.mark.demo
def test_demo_another():
    pass


if __name__ == '__main__':
    # 当我们以 python 脚本运行该文件的时候，执行下面的代码
    print("hello")
    pytest.main()
