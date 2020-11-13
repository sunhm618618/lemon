#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : key_test.py
@Time    : 2020-10-26 11:41
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.handle_path import DRIVER

driver = webdriver.Chrome(executable_path=DRIVER)
# 打开baidu首页
driver.get("https://www.baidu.com")

input_el = driver.find_element_by_id('kw')
input_el.send_keys("lemon")
input_el.send_keys(Keys.ENTER)