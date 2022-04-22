#coding:utf-8
import requests
import json
import time
"""ERP"""
session = requests.session()
"""ERP"""
# header = {
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "Accept-Language": "zh-CN,zh;q=0.9",
#             "Accept-Encoding": "gzip,deflate",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
#             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#         }
#
# login = "http://192.168.10.238:19001/sys/login"
# request_data = {"username":"yinjing","password":"yinjing"}
# result = session.post(login,data=request_data,headers=header)
# cookies = session.cookies
# url = "http://192.168.10.238:19001/cg/askbuydetail/list?billStartDate=&billEndDate=&askBuyNo=&company=&askDepartment=&askDepartmentName=&askPerson=&askStatus=&stockCode=&stockName=&billStatus=-1&purchaseStatus=-1&askType=&page=1&rows=20&sort=a.ask_buy_no&order=DESC&_=1625457176448.html"
# result = session.get(url, params=cookies)
# print(result.text)

"""客服系统"""

login_header={"header": "Accept: application/json, text/javascript, */*; q=0.01",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "zh-CN,zh;q=0.9"}
login = "http://192.168.10.219:7060/customer/login.do"
result = session.get(login,headers=login_header)
#print(session.cookies) #先获取cookie
#再登录
userlogin= "http://192.168.10.219:7060/customer/userLogin.do"

requert_data = {"account":"admin",
                "userPwd":"xmsx123"}
result2 = session.post(userlogin,data=requert_data,headers=login_header,cookies =session.cookies)
#print(result2.text)

header={"Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Referer":"http://192.168.10.219:7060/customer/index.do"
        }
millis = int(round(time.time() * 1000))  # 把秒转换毫秒的方法获得13位的时间戳,round()是四舍五入
current_milli_time = lambda: int(round(time.time() * 1000))
current_milli_time_13 = current_milli_time()
#print(type(current_milli_time_13))
#url = "http://192.168.10.219:7060/customer/order/viewOrder.do?id=01cc28c3bf1944ddb36ff0e6dee1c342&timeStamp="+str(current_milli_time_13)
#print(url)
#result3 = session.get(url,headers=header)
#print(result3.text)

from urllib3 import encode_multipart_formdata
from base.read_config import ReadConfig
from base import get_project_path
login_header={"header": "Accept: application/json, text/javascript, */*; q=0.01",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "zh-CN,zh;q=0.9"}

conf_path = get_project_path.config_path
customersys_host= eval(ReadConfig.get_config(get_project_path.config_path,"Customer_Sys","customersys"))['host']
customersys_login_header = eval(ReadConfig.get_config(get_project_path.config_path,"Customer_Sys","customersys"))['login_header']
erp_header_formdata = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['header_formdata']
url1 = "/customer/order/saveOrder.do"
with open(r"C:\Users\Administrator\Desktop\ERP.doc", mode="rb") as f:
    file = {
    #"breserve": ("ERP.doc", f.read(),"application/octet-stream"),  # 引号的file是接口的字段，后面的是文件的名称、文件的内容
    "breserve": ("", ""),  # 不上传附件
    "search_modelmodule": "",
    "customer_customercode": "FF6251200019412D",
    "receiveCheck": "5.CP.3630-LoRa模块",
    "projectname": "lyj项目20211025",
    "subindustry": "lyj行业20211025",
    "contemplate": 0,
    "newcustomer": 0,
    "contractnature": "销售",
    "customercode": "FF6251200019412D",
    "customertype": 0,
    "technicalmanager": "严永金",
    "branchname": "四信通信",
    "depart": 9,
    "audit": 2,
    "departmanager": "张绍炜-部门经理",
    "invoicesituate": "专票",
    "name": "林云",
    "sutyparagraph": "123",
    "address": "厦门市集美区孙坂南路86~88号 88-1 南楼2楼仓库（务必送货上楼，禁止放置快递柜）；厦门四信电子技术有限公司；收件人：杨尚志；电话：0592-6021827、15934715030",
    "openbank": "12313131231",
    "depositsituation": "无",
    "depositsite": "",
    "skillname": 1,
    "paymentmethod": "款到发货",
    "estpaymentdate": "2021-10-25",
    "guaranteescale": 1,
    "cooptype": 1,
    "presupport": "陈航程,陈海燕,谢海海,",
    "prodUser": "曾润芳",
    "loanperiod": "",
    "contractnotes": "合同无特殊要求",
    "businessnotes": "",
    "business": "付焰波",
    "contractUser": "魏琴",
    "invoicrequire": "无开票要求",
    "invoUser": "黄梨蓉",
    "shipexchangedesc": "无财务备注",
    "recipientaddr": "同收货地址",
    "deliverynotes": "北大青鸟（JB-TB-JBF-11S）,数据上四信平台，再推送到智赣119平台",
    "oldbreserve": "",
    "tipflag": "",
    "countProduct": 2,
    #"breserve": "",
    "contact": "test",
    "contactid": "",
    "mobilephone": "13799865324",
    "email": "",
    "fixedphone": "",
    "idBundle": "f260ee9c154e45849c9cf7b1aad30c97",
    "products_num": 2,
    "moduleid_1": "",
    "typecode_1": "",
    "modelmodule_1": "5.CP.3630-LoRa模块",
    "signsname_1": "",
    "softversion_1": "",
    "quantity_1": 200,
    "unitprice_1": 220,
    "warrantycard_1": 200,
    "accessories_1": "标配+北大青鸟 （JB-TB-JBF-11S)",
    "packages_1": "单独",
    "hardwarecustom_1": "无",
    "softwarecustom_1": "无",
    "customparts_1": "无",
    "customsigns_1": "无",
    "breserve_1": "5001070007-L51",
    "pname_1": "5.CP.3630-LoRa模块",
    "software_1": "",
    "warranty_1": 365,
    "fixedtype_1": "不固定",
    "prodrequired_1": "",
    "unit_1": "台",
    "ids": "bdb50202adaa405dbba2157a9cb0f923,"
}

encode_data = encode_multipart_formdata(file)
file_data = encode_data[0]
print(file_data)
erp_header_formdata["Content-Type"] = encode_data[1]
print(encode_data[1])
session = requests.session()
login = "http://192.168.10.219:7060/customer/login.do"
result = session.get(login,headers=login_header)
print(session.cookies) #先获取cookie
#再登录
userlogin= "http://192.168.10.219:7060/customer/userLogin.do"
requert_data = {"account":"admin",
                "userPwd":"xmsx123"}
result2 = session.post(userlogin,data=requert_data,headers=login_header,cookies =session.cookies)
result1 = session.post(customersys_host+url1,cookies=session.cookies, data=file_data, headers=erp_header_formdata,verify=False)
print(result1.text)
