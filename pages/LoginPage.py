# -*- coding:utf-8 -*-
# @project : python--Linux
# @author : admin
# @file : LoginPage.py
# @ide : PyCharm
# @time : 2020/11/6 10:34
import time
from selenium.webdriver.common.by import By
from basePage import BasePage

class login_page(BasePage):
    #父类有init 方法 子类也有 init方法 ，子类要使用父类的init方法，使用supper方法
    def __init__(self):
        super().__init__()
        #只封装查找元素的方法，但是查找元素
        # 用户名输入框
        self.unameInputLocator = (By.NAME,"username")
        #密码输入框
        self.upwdInputLocator = (By.NAME,"password")
        #登录按钮
        self.loginButtonLocator = (By.TAG_NAME,"button")
    #实时获取元素信息
    def unameBox(self):
        return self.get_element(self.unameInputLocator)
    def upwdBox(self):
        return self.get_element(self.upwdInputLocator)
    def loginButton(self):
        return self.get_element(self.loginButtonLocator)
class login_page_action(login_page):
    def login(self,uname,pwd):
        self.unameBox().send_keys(uname)
        self.upwdBox().send_keys(pwd)
        self.loginButton().click()


if __name__ == '__main__':
    login_page_action().login('libai','opmsopms123')
