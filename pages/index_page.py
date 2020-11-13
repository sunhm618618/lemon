#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : index_page.py
@Time    : 2020-11-06 13:49
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.invest_page import InvestPage


class IndexPage(BasePage):
    user_info_locator = (By.XPATH,'//*[@class="mr-5"]/..')
    rob_invest_btn_locator = (By.XPATH, '//a[@class="btn btn-special"]')


    def __init__(self,browser):
        self.browser = browser

    def get_user_info(self):
        text = self.browser.find_element(*self.user_info_locator).text
        return text

    def click_rob_invest_btn(self):
        self.wait_clickable(self.rob_invest_btn_locator).click()
        return InvestPage(self.browser)

