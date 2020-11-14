#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : test_login.py
@Time    : 2020-11-04 10:19
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
import pytest

from data.login_data import login_error_data, login_toast_data, login_success_data
from pages.login_page import LoginPage


class TestLogin(object):

    @pytest.mark.parametrize('case',login_error_data)
    def test_error_case(self,case,browser):

        expected = case['expected']
        loginpage = LoginPage(browser)
        actural = loginpage.get().login_fail(case['username'],case['pwd']).get_tip_msg()
        assert expected == actural

    @pytest.mark.parametrize('case',login_toast_data)
    def test_toast_case(self,case,browser):

        expected = case['expected']
        loginpage = LoginPage(browser)
        actural = loginpage.get().login_fail(case['username'],case['pwd']).get_toast_msg()
        assert expected == actural

    @pytest.mark.parametrize('case',login_success_data)
    def test_success(self,case,browser):

        expected = case['expected']
        loginpage = LoginPage(browser)
        actural = loginpage.get().login_success(case['username'],case['pwd']).get_user_info()
        assert expected in actural


if __name__ == '__main__':
    pytest.main()