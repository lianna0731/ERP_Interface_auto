#coding:utf-8

import unittest
from test_file import HTMLTestRunner_cn
from base.my_log import  MyLog
import os
get_project_path = os.path.realpath(__file__)
#print(get_project_path)
a = os.path.split(os.path.split(get_project_path)[0])[0] #获取顶级路径
#   print(a) #E:\ERP_interface_Auto
report_path = a+"\\report\\report.html"
fp = open(report_path, 'wb')

dirc = a+"\\case"
pattern = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=dirc, pattern=pattern)

# suit = unittest.TestSuite()
# suit.addTest('test1')
# suit.addTest('test2')
# case_list = ('test1','test2')
# suit.addTests(case_list)
# unittest.TextTestRunner().run(suit)
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='接口测试报告', description="这是接口测试报告")
runner.run(discover)