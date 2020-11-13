#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : seliunm_test1.py
@Time    : 2020-10-19 09:48
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
from gevent import os
from selenium import webdriver

from common.handle_path import DRIVER
from pages.base_page import BasePage

browser = webdriver.Chrome(executable_path=DRIVER)
# browser = webdriver.Chrome()
url = "http://www.baidu.com"
# 打开百度
browser.get(url=url)
locator = ('id','su')
btn=browser.wait_clickable(locator)
print(btn.text)


# print(sys.path)