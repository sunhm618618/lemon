#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@File    : ketangpai_test.py
@Time    : 2020-10-21 11:34
@Author  : doudou
@Email   : 935919261@qq.com
@Software: PyCharm
"""
import time


from selenium import webdriver

from common.handle_path import DRIVER

browser = webdriver.Chrome(executable_path=DRIVER)
# 打开课堂派首页
browser.get("https://www.ketangpai.com/Index/index")
time.sleep(6)

# 通过class name查找使用新版本的弹框，并关闭
el = browser.find_element_by_class_name("layui-layer-close2")
browser.find_element()
el.click()
time.sleep(2)

# 查找课堂派首页的logo,先找到上级id，再通过element对象进行找class_name=logo的元素，从而
el = browser.find_element_by_id('indextop')
el = el.find_element_by_class_name('logo')
# 查找渠道合作这个元素，并打印其文案
el = browser.find_element_by_link_text('渠道合作')
assert (el.get_attribute('innerText') == '渠道合作')

# 通过样式名className查找 在样式名前加一个.号
el= browser.find_element_by_css_selector(".vide-warp")

# 根据属性名查找 （标签名[属性名="属性值"]）
el = browser.find_element_by_css_selector('a[id="huawen"]')

#通过tag_name查找元素  一般不建议使用
el = browser.find_element_by_tag_name('i')


# 通过xpath查找元素  绝对路径
el = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/a[3]')
print(el.text)


# 通过xpath查找解决方案这个文案
el = browser.find_element_by_xpath('//*[@id="solutiontop"]/a')
print(el.text)
browser.close()


