# coding=utf-8
# -*- yangyaqi -*-

import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains

logger = Logger(logger="BasePage").getlog()


# 定义一个页面基类,让所有页面都继承这个类,封装一些常用的页面操作方法到这个类
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds" % seconds)

    # 点击关闭当
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except Exception as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_window_img(self):
        # file_path = os.path.abspath('.') + '\\screenshots\\'
        file_path = "D:\\Pycharm\\demo\\screenshots\\"
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots/")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_window_img()
        print(file_path)
        print(rq)
        print(screen_name)

    # 元素定位方法
    def find_element(self, selector):
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful"
                            "by %s via value: %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.get_window_img()
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "1" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("找到了元素 \' %s \' successful"
                            "by %s via value: %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("如果列表为空的话:%s" % e)
                self.get_window_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    # 输入文本
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type\' %s \'in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_window_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element\'%s\'was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

        # 退出

    def kill(self):
        self.driver.quit()

        # 刷新

    def f5(self):
        self.driver.refresh()

        # 执行js

    def js(self, sprit):
        self.driver.execute_script(sprit)

        # 获取title

    def get_title(self, fangfa, dingwei):
        return self.driver.title

        # 截屏

    def get_screen(self, file_path):
        self.driver.get_screenshot_as_file(file_path)

        # 允许

    def accpet(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
