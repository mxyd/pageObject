# -*- coding:utf-8 -*-
# @project : python--Linux
# @author : admin
# @file : projectManagerCase.py
# @ide : PyCharm
# @time : 2020/11/6 16:54
import unittest,time
from PO实战.pages.projectManger import ProjectMangerActionObj
class projectManagerCase(unittest.TestCase):

    def test_indistinct_serch(self):
        """
        模糊查询测试用例
        :return:
       """


        ProjectMangerActionObj.to_page()
        time.sleep(2)
        """1 选定文本，输入并搜索"""
        #第一种方法，将操作元素的动作放在 用例里面，
        # pname = "test"
        # ProjectMangerActionObj.get_project_name().send_keys(pname)
        # ProjectMangerActionObj.get_search_button().click()

        #第二种方法 将 操作元素的动作放在页面类里面，在用例里面直接调用即可
        ProjectMangerActionObj.search_project()
        """2 获取项目名称列表，项目别名列表"""
        #获取名称列表
        project_name_list = ProjectMangerActionObj.get_list_of_project_names()
        #获取别名列表
        project_other_name_list = ProjectMangerActionObj.get_list_of_other_project_names()
        # ProjectMangerActionObj.search_project()
        """3 断言验证，搜索出来的列表，别名或者项目名称中至少包含有一个要搜索的文本"""
        for projectName in project_name_list:
            as1 = ProjectMangerActionObj.pname in project_other_name_list[project_name_list.index(projectName)].text
            as2 = ProjectMangerActionObj.pname in projectName.text
            self.assertTrue(as1 or as2)

if __name__ == '__main__':
    unittest.main()






