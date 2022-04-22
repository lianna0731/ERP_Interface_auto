#coding:utf-8
import os
get_project_path = os.path.realpath(__file__)
#print(get_project_path)
a = os.path.split(os.path.split(get_project_path)[0])[0] #获取顶级路径
#   print(a) #E:\ERP_interface_Auto\requsts_inference


test_data_path = os.path.join(a,"test_file","inference - 1.xlsx")
test_report_path = os.path.join(a,"report","test_result.html")
config_path = os.path.join(a,"conf","case_config")
logfile_path = os.path.join(a,"pylog.txt")
#print(config_path)
#print(logfile_path)