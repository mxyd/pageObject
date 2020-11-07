# -*- coding:utf-8 -*-
# @project : python--Linux
# @author : admin
# @file : attendanceManagementPage.py
# @ide : PyCharm
# @time : 2020/11/6 15:54
"""考勤管理页面"""
from PO实战.pages.basePage import BasePage
from PO实战.utlis.mysetting import URL
from selenium.webdriver.common.by import By
from PO实战.utlis.myDriver import Driver
class AttendanceManagementPage(BasePage):
    def __init__(self,path = "/checkwork/manage"):
        super(AttendanceManagementPage, self).__init__()
        Driver.to_page( "/checkwork/manage")
        # self.path = URL + path
        #考勤管理
        self.Attendance_Management_locator = (By.CSS_SELECTOR,"a[href='/checkwork/manage']>span")




