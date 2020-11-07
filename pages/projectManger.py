# -*- coding:utf-8 -*-
# @project : python--Linux
# @author : admin
# @file : projectManger.py
# @ide : PyCharm
# @time : 2020/11/6 15:27
"""项目管理页面类"""
from PO实战.pages.basePage import BasePage

from PO实战.utlis.mysetting import URL
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
class ProjectManger(BasePage):

    def __init__(self,path="/project/manage"):
        """项目管理页面类"""
        super().__init__()
        self.path = URL + path
        #以下封装页面元素寻找方法

        #项目状态
        self.project_status_locator = (By.CSS_SELECTOR,"form[class='searchform']>select")
        #项目名称
        self.project_name_locator = (By.CSS_SELECTOR,"form[class='searchform']>input")
        #搜索按钮
        self.search_project_button_locator = (By.CSS_SELECTOR,"form[class='searchform']>button")
        #新项目
        self.creact_project_button_locator = (By.CSS_SELECTOR,"a[href='/project/add']")
        #获取列表当中的每一个项目名称
        self.list_of_project_name_locator = (By.CSS_SELECTOR,"tbody > tr > td:nth-child(1)")
        # 获取列表当中的每一个项目别名
        self.list_of_project_other_name_locator = (By.CSS_SELECTOR, "tbody > tr > td:nth-child(2)")


    # 实时获取元素信息
    #获取项目名称列表
    def get_list_of_project_names(self):
        return self.get_elements(self.list_of_project_name_locator)
    def get_list_of_other_project_names(self):
        return  self.get_elements(self.list_of_project_other_name_locator)
    #获取项目状态
    def  get_project_status(self):
        return  self.get_element(self.project_status_locator)
    #获取项目名称
    def get_project_name(self):
        return self.get_element(self.project_name_locator)
    #点击搜素按钮
    def get_search_button(self):
        return  self.get_element(self.search_project_button_locator)
    def to_page(self):
        """
        访问此页面网址
        :return:
        """
        self.driver.get(self.path)

class ProjectMangerAction(ProjectManger):
    #搜素项目
    pname = "test"
    def search_project(self):

        self.get_project_status()
        self.get_project_name().send_keys(ProjectMangerAction().pname)
        self.get_search_button().click()



#创建对象实例，其他模块引用此对象，可保持对象在内存中只有一个
ProjectMangerActionObj = ProjectMangerAction()
if __name__ == '__main__':
    ProjectMangerActionObj = ProjectMangerAction()
    ProjectMangerActionObj.search_project()




