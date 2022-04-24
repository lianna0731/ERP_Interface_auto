#coding:utf-8

import unittest
from test_file import HTMLTestRunner_cn
from base.my_log import  MyLog
report_path = "E:ERP\\ERP_Interface_Auto\\report\\report.html"
fp = open(report_path, 'wb')

dirc = "E:ERP\\ERP_Interface_Auto\\case"
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