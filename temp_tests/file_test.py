#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : file_test.py
@Time    : 2020-10-28 10:07
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
import time
from selenium.webdriver import ActionChains

import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.handle_path import DRIVER
import pyperclip

driver = webdriver.Chrome(executable_path=DRIVER)
# 打开baidu首页
# driver.get("https://www.12306.cn/index/")
driver.implicitly_wait(3)

# js = "var el =  document.getElementById('train_date');" \
#      "el.readOnly = false;" \
#      "el.value = '2020-10-30'"  \
#
# driver.execute_script(js)


# el = driver.find_element_by_id("train_date")
# js = "arguments[0].readOnly = false;arguments[0].value = '2020-11-11'"
# driver.execute_script(js,el)
# time.sleep(3)
# driver.close()
#


# 鼠标滚动

# js_code = "window.scrollTo(0, document.body.scrollHeight)"
# driver.execute_script(js_code)
# time.sleep(3)
# driver.close()
url = 'file:///Users/hongmeisun/Desktop/demo.html'
driver.get(url)
driver.implicitly_wait(3)


file_el = driver.find_element_by_name("user")
print(file_el.is_enabled())
print(type(file_el))
print(file_el)

time.sleep(3)
# file_el.click()
# driver.execute_script("arguments[0].click()", file_el)
# file_el.send_keys(r'/Users/hongmeisun/Desktop/demo.html')
# time.sleep(4)

# p = '/Users/hongmeisun/Desktop/深圳-萌萌-32期.txt'
# pyperclip.copy(p)
# time.sleep(3)
# pyautogui.hotkey('ctrl','v')
#
# pyautogui.press('enter', presses=2)


# driver.close()
action = ActionChains(driver)
action.click(file_el).perform()
time.sleep(3)
file_el.send_keys(r'/Users/hongmeisun/Desktop/demo.html')
time.sleep(3)

# driver.close()
