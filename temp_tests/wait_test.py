#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : test_wait.py
@Time    : 2020-10-22 21:34
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.handle_path import DRIVER

driver = webdriver.Chrome(executable_path=DRIVER)
# 打开baidu首页
driver.get("https://www.baidu.com")
# 初始化一个等待器
wait = WebDriverWait(driver=driver,timeout=15,poll_frequency=0.1)
#定位元素
locator = ('id','kw')

# 等待搜索框出现并可以输入内容
el = wait.until(expected_conditions.element_to_be_clickable(locator))

# 输入柠檬班
el.send_keys('柠檬班')
# 点击百度一下按钮，进行搜索
locator = ('id','su')
el = wait.until(expected_conditions.element_to_be_clickable(locator))
el.click()

windows = driver.window_handles
driver.switch_to.window(windows[-1])

assert "baidu.com" in driver.current_url
# locator = ('partial_link_text', 'lemon.ke.qq.com')
locator = (By.PARTIAL_LINK_TEXT, 'lemon.ke.qq.com')
# time.sleep(5)
# locator = ('xpath','//*[@id="1"]/div/div[2]/div[2]/a[1]')
el = wait.until(expected_conditions.element_to_be_clickable(locator))
el.click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
assert "lemon.ke.qq.com/" in driver.current_url
# locator = ('class_name','header-index-logo')
locator = (By.CLASS_NAME,'header-index-logo')

el = wait.until(expected_conditions.element_to_be_clickable(locator))
driver.close()

