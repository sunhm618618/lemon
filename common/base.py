# TODO: 违反 PO 原则，应该是通用
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import setting


DEFAULT_TIMEOUT = 10
DEFAULT_POLL = 0.5


class BasePage:
    host = ''

    def __init__(self, browser):
        self.browser = browser

    # @save_screenshot()
    def wait_clickable(self, locator, timeout=DEFAULT_TIMEOUT, poll=DEFAULT_POLL):
        """等带元素被点击"""
        try:
            wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll)
            el = wait.until(expected_conditions.element_to_be_clickable(locator))
        except Exception as e:
            self.screen_shot()
            logging.error("定位元素失败{}".format(e))
        return el

    def wait_visible(self, locator, timeout=DEFAULT_TIMEOUT, poll=DEFAULT_POLL):
        """等带元素被点击"""
        wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll)
        el = wait.until(expected_conditions.visibility_of_element_located(locator))
        return el

    def wait_presence(self, locator, timeout=DEFAULT_TIMEOUT, poll=DEFAULT_POLL):
        """等带元素被点击"""
        wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll)
        el = wait.until(expected_conditions.presence_of_element_located(locator))
        return el

    def screen_shot(self):
        pic_name = os.path.join(setting.IMG_PATH, str(int(time.time())) + '.png')
        self.driver.save_screenshot(pic_name)

    # 截图
    # driver.save_screenshot('demo.png')

    # 还有那些操作是通用的，可以封装到 basepage

    def refresh(self):
        """刷新"""
        self.browser.refresh()

    def goto(self, url:str):
        """访问 URL """
        if url.startswith(('http://', 'https://')):
            return self.driver.get(url)
        if not url.startswith('/'):
            return ValueError('url must start with slash /.')
        url = self.host + url
        return self.driver.get(url)

    def click(self, locator):
        el = self.wait_clickable(locator)
        el.click()
        return self

    def wait_element(self, locator, timeout=DEFAULT_TIMEOUT,  poll=DEFAULT_POLL):
        """智能等待"""
        used_time = 0
        while used_time < timeout:
            try:
                time.sleep(poll)
                return self.browser.find_element(locator)
            except NoSuchElementException as e:
                used_time += poll
        raise NoSuchElementException("找不到元素 {}".format(locator))


    def fill(self, locator, words):
        """输入"""
        el = self.wait_element(locator)
        el.send_keys(words)
        return self

    # 双击， 右击， 拖撰
    def double_click(self, locator):
        """双击"""
        el = self.wait_clickable(locator)
        ac = ActionChains(self.browser)
        ac.double_click(el).perform()
        return el

    def scroll_to(self, width, height):
        self.browser.execute_script(
            "window.scrollTo({}, {})".format(width, height)
        )

    def scroll_to_bottom(self):
        """窗口滚动到页面底部"""
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def upload(self, locator):
        """上传文件"""
        pass

    # 如果你发现用 js 可以实现的浏览器操作，如果 selenium 没有支持，就可以放到 basepage
    # seleneium 不支持元素属性设置，
    def set_attr(self, locator, prop_name, prop_value):
        """el =
        js 语句修改元素属性
        """
        el = self.wait_element(locator)
        # js语句 el.value = "2019"
        js_code = 'arguments[0].{} = "{}"'.format(prop_name, prop_value)
        self.browser.execute_script(js_code, el)