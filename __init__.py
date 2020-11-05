# -*- coding:utf-8 -*-
# @project : python--Linux
# @author : admin
# @file : __init__.py.py
# @ide : PyCharm
# @time : 2020/11/5 14:27
from selenium import webdriver
class logginPage:
    """
    简单的PO模式 以opms为例
    """
    def __init__(self):
        self.driver = webdriver.Chrome("E:\chrome_firfox_drive\chrome\chromedriver.exe")
        self.driver.get('http://127.0.0.1:8088/login')
    #为了防止出现陈旧的元素，所以在封装时，需要将页面的每个元素封装成一个方法，元素的行为封装成一个方法
    #实时获取用户名输入框
    def usenameBox(self):
        return  self.driver.find_element_by_name('username')
    #实时获取密码输入框
    def pwdBox(self):
        return  self.driver.find_element_by_name('password')
    #实时获取登录按钮
    def loginButton(self):
        return  self.driver.find_element_by_tag_name('button')

    def login(self,uname,pwd):
        """登录系统"""
        #输入用户名
        self.usenameBox().send_keys(uname)
        # 输入密码
        self.pwdBox().send_keys(pwd)
        #点击登录
        self.loginButton().click()
if __name__ == '__main__':
    userlogin = logginPage()
    userlogin.login('libai','opmsopms123')
