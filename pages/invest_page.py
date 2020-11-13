#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : invest_page.py
@Time    : 2020-11-09 08:56
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.user_page import UserPage


class InvestPage(BasePage):
    #
    input_money_locator = (By.CLASS_NAME,'invest-unit-investinput')
    invest_btn_locator = (By.XPATH, '//button[contains(@class, "btn-special")]')
    success_pop_locator = (By.XPATH, '//div[@class="layui-layer-content"]//div[@class="capital_font1 note"]')
    active_btn_locator = (By.XPATH, '//div[@class="layui-layer-content"]//button')


    def get_before_money(self):
        """获取投资前的金额--用户余额"""
        el = self.wait_presence(self.input_money_locator)
        return el.get_attribute('data-amount')

    def input_money(self,money):
        """输入金额"""
        self.wait_visible(self.input_money_locator).send_keys(money)
        return self

    def get_error_msg(self):
        """获取输入不正确的投资金额后的错误信息--投资按钮里面的文案会变化"""
        msg = self.wait_presence(self.error_mag_locator).text
        return msg

    def click_invest_btn(self):
        """点击投资按钮--输入投资金额后"""
        self.wait_clickable(self.invest_btn_locator).click()
        return self

    def get_success_pop_msg(self):
        """投标成功元素"""
        el = self.wait_visible(self.success_pop_locator)
        return el.text

    def click_active_btn(self):
        """点击查看并激活"""
        el = self.browser.find_element(*self.active_btn_locator)
        el.click()
        return UserPage(self.browser)




