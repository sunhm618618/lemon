#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : base_page.py
@Time    : 2020-11-06 13:19
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage(object):
    def __init__(self,browser):
        self.browser = browser


    def wait_clickable(self, locator, timeout=20, poll=1):
        """等带元素被点击"""

        wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll)
        el = wait.until(expected_conditions.element_to_be_clickable(locator))
        return el

    def wait_visible(self,locator,timeout=10,poll=0.5):
        '''
        等待元素可见
        :param locator:
        :param timeout:
        :param poll:
        :return:
        '''
        wait = WebDriverWait(self.browser,timeout,poll)
        el = wait.until(expected_conditions.visibility_of_element_located(locator))
        return el

    def wait_presence(self,locator,timeout=10,poll=0.5):
        '''
        等待元素出现
        :param locator:
        :param timeout:
        :param poll:
        :return:
        '''
        wait = WebDriverWait(self.browser,timeout=timeout,poll_frequency=poll)
        el = wait.until(expected_conditions.presence_of_element_located(locator))
        return el

