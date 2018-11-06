# _*_ coding:utf-8 _*_
# -*- yangyaqi -*-
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))#注意相对路径获取方法
    chrom_driver_path = dir +'/tools/chromedriver.exe'
    #ie_driver_path = dir+'/tools/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver=driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer","URL")
        logger.info("测试服务器的url是 : %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrom_driver_path)
            logger.info("Starting chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info('open url:%s'%url)
        driver.maximize_window()
        logger.info('Maximize the current window')
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds")
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()
