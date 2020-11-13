#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : fixture_test.py
@Time    : 2020-11-03 15:07
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
import pytest


class TestFixture():

    @pytest.fixture(scope='class')
    def before_and_after(self):
        print("*"*20)
        yield
        print("%"*20)

    @pytest.mark.ok
    def testcase1(self,before_and_after):
        print("case1111******")

    @pytest.mark.ok
    def testcase2(self,before_and_after):
        print("case2222******")


if __name__ == '__main__':
    pytest.main()