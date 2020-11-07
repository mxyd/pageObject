# -*- coding:utf-8 -*-
# @project : python--Linux
# @author : admin
# @file : basePage.py
# @ide : PyCharm
# @time : 2020/11/6 10:25
from PO实战.utlis.myDriver import Driver
from PO实战.utlis.mysetting import TIMEOUT,POLL_FREQUENCY
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self):
        self.driver = Driver.get_driver()

    def get_element(self,locator):
        """
         (显示等待) 根据表达式匹配单个元素，返回元素对象
        :param locator: 参数是一个元祖(x1,x2)，x1--表示的是定位方法   x2--表示的是元素定位表达式
        :return:
        """
        #使用显示等待 判断元素是否存在
        WebDriverWait(
            #浏览器对象
            driver = self.driver,
            #超时时间
            timeout = TIMEOUT,
            #轮询时间
            poll_frequency = POLL_FREQUENCY
        ).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_elements(self,locator):
        """
         (显示等待) 根据表达式匹配元素列表，返回元素列表
        :param locator: 参数是一个元祖(x1,x2)，x1--表示的是定位方法   x2--表示的是元素定位表达式
        :return:
        """
        #使用显示等待 判断元素是否存在
        WebDriverWait(
            #浏览器对象
            driver = self.driver,
            #超时时间
            timeout = TIMEOUT,
            #轮询时间
            poll_frequency = POLL_FREQUENCY
        ).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

