#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : BFconftest.py
@Time    : 2020-11-04 10:04
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""

import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from data.login_data import login_error_data, login_toast_data, login_success_data


@pytest.fixture(scope='class')
def browser():
   """
   操作浏览器
   :return:
   """
   driver = webdriver.Chrome()

   driver.implicitly_wait(10)
   print("浏览器已经打开，开始执行用例。。。")
   yield driver
   print("测试用例已经执行完毕，准备关闭浏览器。。。")
   driver.close()


@pytest.fixture()
def login(browser):
   index_page = LoginPage(browser).get().login_success(
      login_data_success[0]['username'], login_data_success[0]['pwd'])
