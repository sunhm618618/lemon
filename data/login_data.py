#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : login_data.py
@Time    : 2020-11-06 10:19
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""

login_error_data = [
    {"username":"","pwd":"","expected":"请输入手机号","tag":"error"},
    {"username": "13670036927", "pwd": "", "expected": "请输入密码", "tag": "error"},
    {"username": "111", "pwd": "", "expected": "请输入正确的手机号", "tag": "error"},
]

login_toast_data = [
    {"username": "13670036927", "pwd": "23311112", "expected": "此账号没有经过授权，请联系管理员!", "tag": "toast"},

]

login_success_data = [
    {"username": "18124762064", "pwd": "ss123456", "expected": "我的帐户[萌萌小蜜蜂]", "tag": "success"},

]