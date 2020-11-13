#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : mouse_test.py
@Time    : 2020-10-26 13:16
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.handle_path import DRIVER

driver = webdriver.Chrome(executable_path=DRIVER)
driver.implicitly_wait(10)

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)

action = ActionChains ( driver )
iframe_el_locator = ('id', 'iframeResult')
# 切换到iframe里
WebDriverWait ( driver, 20 ).until (
    expected_conditions.frame_to_be_available_and_switch_to_it ( iframe_el_locator )
)
source_el = driver.find_element_by_id ( 'draggable' )
target_el = driver.find_element_by_id ( 'droppable' )

action.drag_and_drop ( source_el, target_el ).perform ()
# 切换到弹框
alert = driver.switch_to.alert
alert.accept ()
driver.switch_to.default_content ()

driver.switch_to.default_content ()
driver.close ()


