#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : 222.py
@Time    : 2020-10-26 14:44
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.handle_path import DRIVER

driver = webdriver.Chrome(executable_path=DRIVER)

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)
driver.implicitly_wait(10)
time.sleep(5)
iframe_el_locator = ('id', 'iframeResult')
# 切换到iframe里
WebDriverWait ( driver, 20 ).until (
    expected_conditions.frame_to_be_available_and_switch_to_it ( iframe_el_locator )
)

el = driver.find_element_by_id("draggable")

el.click()