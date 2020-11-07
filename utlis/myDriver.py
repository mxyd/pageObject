# -*- coding:utf-8 -*-
# @project : python--Linux
# @author : admin
# @file : myDriver.py
# @ide : PyCharm
# @time : 2020/11/6 10:16
from selenium import webdriver
from PO实战.utlis.mysetting import  URL,driverPath
class Driver:
    """
    浏览器工具类
    """
    #初始化驱动对象为空
    driver = None
    @classmethod
    def get_driver(cls,browser_name="Chrome"):
        """
        获取浏览器对象
        :param browser_name:
        :return:
        """
        #如果浏览器为空，就创建，不为空的话，就返回之前创建的浏览器对象
        if cls.driver is None:
            if browser_name == "Chrome":
                cls.driver = webdriver.Chrome(driverPath["Chrome"])
            #最大化窗口
            cls.driver.maximize_window()
            cls.driver.get(URL)
            #执行登录
            cls.__login()
        return cls.driver

    @classmethod
    def __login(cls):
        """
        __login:表示私有方法，只能在类里面调用
        类外面无法调用，子类不能继承
        只在浏览器刚打开的时候登录一次---重要
        :return:
        """
        cls.driver.find_element_by_name("username").send_keys("libai")
        cls.driver.find_element_by_name("password").send_keys("opmsopms123")
        cls.driver.find_element_by_css_selector("button").click()
