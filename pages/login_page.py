#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : login_page.py
@Time    : 2020-11-04 10:03
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from pages.index_page import IndexPage
from config.setting import HOST
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = HOST + '/Index/login.html'
    phone_locator = (By.NAME,'phone')
    pwd_locator = (By.NAME,'password')
    submit_btn_locator = (By.CLASS_NAME,'btn-special')
    error_info_locator = (By.CLASS_NAME,'form-error-info')
    toast_locator = (By.CLASS_NAME,'layui-layer-content')

    def __init__(self,browser):
        self.browser = browser

    def get(self):
        url = self.url
        self.browser.get(url)
        return self

    def login_fail(self,name,pwd):
        # self.wait_clickable(*self.phone_locator).send_keys ( name )
        # self.wait_clickable(*self.phone_locator).send_keys ( name )
        self.browser.find_element(*self.phone_locator).send_keys ( name )
        self.browser.find_element(*self.pwd_locator).send_keys ( pwd )
        # self.browser.find_element(*self.submit_btn_locator).click ()

        self.wait_clickable(self.submit_btn_locator).click()
        return self

    def login_success(self,name,pwd):

        self.browser.find_element(*self.phone_locator).send_keys ( name )
        self.browser.find_element(*self.pwd_locator).send_keys ( pwd )
        self.browser.find_element(*self.submit_btn_locator).click ()
        return IndexPage(self.browser)

    def get_tip_msg(self):
        msg = self.browser.find_element(*self.error_info_locator).text
        return msg

    def get_toast_msg(self):
        msg = self.browser.find_element(*self.toast_locator).text
        return msg

#
# if __name__ == '__main__':
#     lg = LoginPage(browser)
#     lg.login('','')

