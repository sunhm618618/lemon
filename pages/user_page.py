#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : user_page.py
@Time    : 2020-11-09 10:08
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserPage(BasePage):

    money_locator = (By.CLASS_NAME, 'color_sub')

    def __init__(self,browser):
        self.browser = browser

    def get_current_money(self):
        """获取用户当前"""
        el = self.wait_presence(self.money_locator)
        return el.text[:-1]
