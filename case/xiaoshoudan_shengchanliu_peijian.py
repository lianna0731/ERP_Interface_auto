#coding:utf-8

import unittest
import json
from base.web_Login_Getcookie import Login
import requests
import json
import random
import time
from base.sqlserver_connection import SqlServer_connectin
from base.get_st_stock_quantity import Get_st_stock_quantity
import datetime
from base.host_header import Host
from base.get_orderNo import Get_OrderNo
from requests_toolbelt import MultipartEncoder
from urllib3 import encode_multipart_formdata
from base.my_log import  MyLog
from base.read_config import ReadConfig
from base import get_project_path
from base.get_cookie import Get_cookie
import datetime

class Run_send(unittest.TestCase):
    """获取类Get_OrderNo里的初始化数值变量，用反射所有流程单号就一致，跑不下去"""
    i = random.randint(0, 9999)
    get_orderNo = Get_OrderNo(i,"客服销售单到erp生产流程")
    date = get_orderNo.date
    #techCode = get_orderNo.techCode
    date3 = get_orderNo.date3  # 当前日期+3
    # pCode = get_orderNo.PleasebuyCode
    # psCode = get_orderNo.PurchaseCode
    # inStoreNo = get_orderNo.inStoreNo
    d_date = get_orderNo.d_date
    current_milli_time_13 = get_orderNo.current_milli_time_13

    @classmethod
    def setUpClass(cls):
        cls.mylog = MyLog()
        cls.mylog.info("客服销售单到erp生产流程开始\n")

    def setUp(self):
        self.session = requests.session()
        """获取配置文件erp、报价系统主机地址、头部信息.存货等"""
        conf_path = get_project_path.config_path
        self.customersys_host= eval(ReadConfig.get_config(get_project_path.config_path,"Customer_Sys","customersys"))['host']
        self.customersys_login_header = eval(ReadConfig.get_config(get_project_path.config_path,"Customer_Sys","customersys"))['login_header']
        self.erp_header_formdata = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['header_formdata']
        self.erp_host = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['host']
        self.erp_login_header = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['login_header']
        self.erp_header = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['header']
        self.CustomerSys_customercode = eval(ReadConfig.get_config(get_project_path.config_path, "Customer_Sys", "customersys"))['customercode']
        self.CustomerSys_customerName = eval(ReadConfig.get_config(get_project_path.config_path, "Customer_Sys", "customersys"))['customerName']
        self.CustomerSys_product = eval(ReadConfig.get_config(get_project_path.config_path, "Customer_Sys", "customersys"))['product']
        self.saleCount = eval(ReadConfig.get_config(get_project_path.config_path, "Customer_Sys", "customersys"))['saleCount']
        self.product_name = eval(ReadConfig.get_config(get_project_path.config_path, "Customer_Sys", "customersys"))['product_name']
        self.get_cookie = Get_cookie()
        self.SqlServer = SqlServer_connectin()
    # def write_report(self):
    #     report_path = "D:\\pycharm_project\\requsts_inference\\report\\report.html"
    #     fp = open(report_path, 'wb')
    #     suit = unittest.TestSuite()
    #     suit.addTest(self.test1())
    #     suit.addTest(self.test2())
    #     # case_list = ('test1','test2')
    #     # suit.addTests(case_list)
    #     # unittest.TextTestRunner().run(suit)
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description="这是接口测试报告")
    #     runner.run(suit)

    def test01(self):
        self.mylog.info('这是第一个测试用例:客服系统新增销售单')
        login_requert_data = {"account": "admin",
                             "userPwd": "xmsx123"}
        cookies=self.get_cookie.customer_sys_get_cookies(self.session,self.customersys_host,login_requert_data,self.customersys_login_header)
        url1="/customer/order/saveOrder.do"
        with open(r"C:\Users\Administrator\Desktop\ERP.doc", mode="rb") as f:
            file = {
            #"breserve": ("ERP.doc", f.read()),  # 引号的file是接口的字段，后面的是文件的名称、文件的内容
            "breserve": ("", ""),  # 不上传附件
            "search_modelmodule": "",
            "customer_customercode":"FF6251200019412D",
            "receiveCheck":"5.CP.3630-LoRa模块",
            "projectname":"lyj项目20211025",
            "subindustry":"lyj行业20211025",
            "contemplate":0,
            "newcustomer":0,
            "contractnature":"销售",
            "customercode":"FF6251200019412D",
            "customertype":0,
            "technicalmanager":"严永金",
            "branchname":"四信通信",
            "depart":9,
            "audit":2,
            "departmanager":"张绍炜-部门经理",
            "invoicesituate":"专票",
            "name":"林云",
            "sutyparagraph":"123",
            "address":"厦门市集美区孙坂南路86~88号 88-1 南楼2楼仓库（务必送货上楼，禁止放置快递柜）；厦门四信电子技术有限公司；收件人：杨尚志；电话：0592-6021827、15934715030",
            "openbank":"12313131231",
            "depositsituation":"无",
            "depositsite":"",
            "skillname":1,
            "paymentmethod":"款到发货",
            "estpaymentdate":"2021-10-25",
            "guaranteescale":1,
            "cooptype":1,
            "presupport":"陈海燕,谢海海,",
            "prodUser":"曾润芳",
            "loanperiod":"",
            "contractnotes":"合同无特殊要求",
            "businessnotes":"",
            "business"	:"付焰波",
            "contractUser":"魏琴",
            "invoicrequire":"无开票要求",
            "invoUser":"黄梨蓉",
            "shipexchangedesc":"无财务备注",
            "recipientaddr":"同收货地址",
            "deliverynotes":"北大青鸟（JB-TB-JBF-11S）,数据上四信平台，再推送到智赣119平台",
            "oldbreserve":"",
            "tipflag":"",
            "countProduct":1,
            #"breserve"	:"",
            "contact":"test",
            "contactid":"",
            "mobilephone":"13799865324",
            "email":"",
            "fixedphone":"",
            "idBundle":"f260ee9c154e45849c9cf7b1aad30c97",
            "products_num":2,
            "moduleid_1":"",
            "typecode_1":"",
            "modelmodule_1":"5.CP.3630-LoRa模块",
            "signsname_1":"",
            "softversion_1":"",
            "quantity_1":self.saleCount,
            "unitprice_1":220,
            "warrantycard_1":self.saleCount,
            "accessories_1":"标配+北大青鸟 （JB-TB-JBF-11S)",
            "packages_1":"单独",
            "hardwarecustom_1"	:"无",
            "softwarecustom_1":"无",
            "customparts_1":"无",
            "customsigns_1":"无",
            "breserve_1":"5001070007-L51",
            "pname_1":"5.CP.3630-LoRa模块",
            "software_1":"",
            "warranty_1":365,
            "fixedtype_1":"不固定",
            "prodrequired_1":"",
            "unit_1":"台",
            "ids":"e51f8a68cbba42da959564b5eb3cbd6d,"
            }
        encode_data = encode_multipart_formdata(file)
        file_data = encode_data[0]
        # print(file_data)
        self.erp_header_formdata["Content-Type"] = encode_data[1]
        result1 = self.session.post(self.customersys_host+url1, data=file_data, headers=self.erp_header_formdata,verify=False,cookies=cookies)
        #self.assertEqual(json.loads(result1.text)['msg'], "succ", msg="接口请求失败")
        self.assertTrue(json.loads(result1.text)['success'], msg="接口请求失败")  #json.loads(result1.text)['success']获取到True为布尔值
        self.mylog.info(result1.text)  #str
        #self.mylog.info(type(json.loads(result1.text)["success"]))   #bool：Ture

    def test03(self):
        self.mylog.info('这是第二个测试用例:ERP技术确认')
        cookies = self.get_cookie.get_cookie(self.session, self.erp_host, self.erp_login_header, "xiehaihai",
                                             "xiehaihai")
        sql = """SELECT TOP 1 *  FROM sale_order a
                    JOIN  sale_tech_confirm  b ON a.order_no = b.order_no
                    WHERE a.custom_code = '{0}'
                    order by a.id  desc""".format(self.CustomerSys_customercode)  # 查询客户的id最大（最新）销售单
        saleorder_No = self.SqlServer.query_one_data(sql)[2]
        # print(saleorder_No)
        createTime = self.SqlServer.query_one_data(sql)[4].strftime(
            '%Y-%m-%d %H:%M:%S')  # 查询出来<class 'datetime.datetime'>，json不支持转换
        print(createTime)
        print(type(createTime))
        techCode = self.SqlServer.query_one_data(sql)[14]
        detailId = self.SqlServer.query_one_data(sql)[13]
        sale_tech_confirm_id = self.SqlServer.query_one_data(sql)[12]
        current_time = time.strftime('%Y%m%d%H%M%S ', time.localtime(time.time()))
        print(current_time)
        url2 = "/sale/saleorder/saveTCInfoTeBom"
        request_data2 = {
            "saleOrderEntity": {
                "softProductLine": "",
                "createTime": createTime,
                "customCode": self.CustomerSys_customercode,
                "orderNo": saleorder_No,
                "sales": "付焰波",
                "review": None,
                "nature": "销售",
                "demand": None,
                "exchange": "无财务备注",
                "techCode": techCode,
                "standard": "4",
                "companyName": "厦门四信通信科技有限公司",
                "customerName": self.CustomerSys_customerName,
                "company": 3
            },
            "saleTechConfirmEntity": {
                "stockCode": self.CustomerSys_product,
                "id": sale_tech_confirm_id,
                "stockModel": "5.CP.3630-LoRa模块",
                "pack": "单独",
                "warrantycard": str(self.saleCount),
                "saleCount": self.saleCount,
                "signs": "无",
                "softVersion": "",
                "softVersionMade": "无",
                "hardwareMade": "无",
                "parts": "标配+北大青鸟 （JB-TB-JBF-11S)",
                "partsMade": "无",
                "remark": "",
                "detailId": detailId,
                "techCode": techCode,
                "bom": 12944,
                "bomId": 12944,
                "bomVersion": "V1.0.0.1",
                "tempAttr": 1,
                "tempName": self.product_name + "-" + current_time,
                "tempMark": "",
                "confirmStatus": 1
            },
            "saleTechBillEntityList": [
                {
                    "category": "20整机配件-选配",
                    "id": 9616,
                    "stockCode": "3701020000-76S",
                    "oldStockCode": "",
                    "productName": "1.WK.0033-1.WK.0033-天线帽",
                    "stockCount": 1690,
                    "outStoreId": "",
                    "remark": "",
                    "supplierCode": "",
                    "supplierName": "",
                    "bitNo": "",
                    "bitNoS": "",
                    "weld": "",
                    "statusType": "自定义",
                    "stockModel": "天线帽",
                    "buyWay": 1320,
                    "stockEnableCount": -47032,
                    "groupName": "370102 孔塞",
                    "status": 4,
                    "stockCode1": "3701020000",
                    "needQuantity": "1"
                }
            ]
        }



    @classmethod
    def tearDownClass(cls):
        cls.mylog.info("客服销售单到erp生产流程结束\n")

if __name__ == '__main__':
    unittest.main()
