#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : test_invest.py
@Time    : 2020-11-09 10:11
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
from decimal import Decimal

import pytest


class TestInvest:
    def test_invest_succcess(self,login):
        index_page = login
        invest_page = index_page.click_rob_invest_btn()
        befor_money = invest_page.get_before_money()
        actual = invest_page.input_money('100').click_invest_btn().get_success_pop_msg()
        expected = "投标成功"
        assert expected in actual
        after_money = invest_page.click_active_btn().get_current_money()
        assert Decimal(befor_money)-Decimal(str(100)) == Decimal(after_money)


if __name__ == '__main__':
    pytest.main()


