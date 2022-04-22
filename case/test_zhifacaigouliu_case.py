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

class Run_send(unittest.TestCase):
    """反射机制获取各单号、日期、时间"""
    #i = random.randint(0, 9999)
    # date = getattr(Get_OrderNo,'date')
    # askBuyNo = getattr(Get_OrderNo,'askBuyNo')
    # date3 =  getattr(Get_OrderNo,'date3')  # 当前日期+3
    # pCode = getattr(Get_OrderNo,'PleasebuyCode')
    # psCode = getattr(Get_OrderNo,'PurchaseCode')
    # inStoreNo = getattr(Get_OrderNo,'inStoreNo')
    # d_date = getattr(Get_OrderNo,'d_date')
    # current_milli_time_13 = getattr(Get_OrderNo,'current_milli_time_13')
    mylog = MyLog()
    """获取类Get_OrderNo里的初始化数值变量，用反射所有流程单号就一致，跑不下去"""
    i = random.randint(0, 9999)
    get_orderNo = Get_OrderNo(i,"直发客户申购")
    date = get_orderNo.date
    askBuyNo = get_orderNo.askBuyNo
    date3 = get_orderNo.date3  # 当前日期+3
    pCode = get_orderNo.PleasebuyCode
    psCode = get_orderNo.PurchaseCode
    inStoreNo = get_orderNo.inStoreNo
    d_date = get_orderNo.d_date
    current_milli_time_13 = get_orderNo.current_milli_time_13
    mylog.info("{0}的单号是：{1}".format("直发客户采购申购单", askBuyNo))
    mylog.info("{0}的单号是：{1}".format("直发客户采购请购单", pCode))
    mylog.info("{0}的单号是：{1}".format("直发客户采购进货单", psCode))
    @classmethod
    def setUpClass(cls):
        cls.mylog.info("直发客户申购测试流程开始\n")

    def setUp(self):
        #self.login_ = Login()
        self.SqlServer = SqlServer_connectin()
        self.st_stock_quantity = Get_st_stock_quantity()
        self.session = requests.session()

        """获取配置文件erp、报价系统主机地址、头部信息.存货等"""
        conf_path = get_project_path.config_path
        self.erp_host= eval(ReadConfig.get_config(get_project_path.config_path,"ERP","erp"))['host']
        self.baojia_host = eval(ReadConfig.get_config(get_project_path.config_path, "BaoJia", "baojia"))['host']
        #self.erp_host  = Host().host
        #self.erp_header = Host().header
        self.erp_header = eval(ReadConfig.get_config(get_project_path.config_path,"ERP","erp"))['header']
        self.erp_header_formdata = eval(ReadConfig.get_config(get_project_path.config_path,"ERP","erp"))['header_formdata']
        self.erp_login_header = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['login_header']
        self.erp_usenamexpath = eval(ReadConfig.get_config(get_project_path.config_path,"ERP","erp"))['erp_usenamexpath']
        self.erp_pswxpath = eval(ReadConfig.get_config(get_project_path.config_path,"ERP","erp"))['erp_pswxpath']
        self.erp_loginbuttonxpath = eval(ReadConfig.get_config(get_project_path.config_path,"ERP","erp"))['erp_loginbuttonxpath']
        self.baojia_usenamexpath = eval(ReadConfig.get_config(get_project_path.config_path, "BaoJia", "baojia"))['baojia_usenamexpath']
        self.baojia_pswxpath = eval(ReadConfig.get_config(get_project_path.config_path, "BaoJia", "baojia"))['baojia_pswxpath']
        self.baojia_loginbuttonxpath = eval(ReadConfig.get_config(get_project_path.config_path, "BaoJia", "baojia"))['baojia_loginbuttonxpath']
        #self.stockCode = eval(ReadConfig.get_config(get_project_path.config_path,"BaseStock","basestock"))['stockcode']
        #self.quantity = eval(ReadConfig.get_config(get_project_path.config_path,"BaseStock","basestock"))['quantity']
        self.stockCode = "3201010002-74E"
        self.quantity = 25
        self.get_cookie = Get_cookie()
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

    def test02(self):
        self.mylog.info('这是第二个测试用例:新增申购单')
        url2 = "/cg/askbuy/save"
        request_data2 = {
                "askBuyNo": self.askBuyNo,
                "company": "3",
                "companyName": None,
                "askDepartment": "58",
                "askDepartmentName": "研发二部",
                "askPerson": "PC69420200320113758",
                "askPersonName": "廖梦芸",
                "remark": "",
                "askStatus": 0,
                "auditMark": None,
                "printCount": 0,
                "makeUser": "yinjing",
                "makeUserName": "尹静",
                "makeDatetime": None,
                "updateUser": None,
                "updateUserName": None,
                "updateDatetime": None,
                "reviewUser": "pengfu",
                "reviewUserName": "唐仕斌",
                "beforeReviewUser": None,
                "reviewDatetime": None,
                "owner": "yinjing,pengfu,liaomengyun,tangshibin",
                "ownerPersonName": "尹静,彭府,廖梦芸,唐仕斌",
                "deleteStatus": 0,
                "billStatus": 1,
                "billDate": self.date,
                "id": None,
                "accountBook": "2021",
                "askBuyDetails": "[{\"askBuyNo\":" '"'+self.askBuyNo+'"' ",\"askCancelNum\":0,\"askCancelTotalNum\":0,\"askCount\":" +str(self.quantity)+ ",\"askType\":3,\"brand\":\"1\",\"buyerQuantity\":0,\"confirmReceiveQuantity\":0,\"deliveryAddress\":\" 软三A06,11楼\",\"demandTime\":\"2021-11-05\",\"executeQuantity\":0,\"id\":11090,\"prevDay\":28,\"prevEnableCount\":93642,\"prevMoq\":1000,\"prevMpq\":1000,\"prevStockCount\":68532,\"price\":0.0022,\"stockAttr\":\"2\",\"stockCode\":\"3201010002-74E\",\"stockCode1\":\"3201010002-74E\",\"stockCount\":34009,\"stockEnableCount\":58658,\"stockId\":15606,\"stockModel\":\"插墙型（竖）,P-046B-B3115-V1,黑色,VAC100~240V 50/60Hz,12V&1.5A@18W,DC输出线长1.5M,DC 5.5*2.5,尺寸:85*53.5*33mm,CCC\",\"stockMoq\":1000,\"stockMpq\":1000,\"stockName\":\"3.PK.0004-3.PK.0004-电源适配器\",\"totalPrice\":4.4,\"turnoverDay\":28,\"unPurchaseQuantity\":0,\"unitName\":\"PCS\",\"remark\":\"MO-2021-10-29-0006\",\"customName\":\"FF5C820211029135555\",\"unitPrice\":null}]",
                "projectCode": None,
                "projectName": None,
                "totalPrice": 4.4
            }
        # allcookies = self.login_.login(self.erp_host + "/login.html", "yinjing", "yinjing",self.erp_usenamexpath,self.erp_pswxpath,self.erp_loginbuttonxpath)
        # cookies = self.login_.add_cookies(allcookies)
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"yinjing", "yinjing")
        result = self.session.post(self.erp_host+url2, data=json.dumps(request_data2), headers=self.erp_header, cookies=cookies, verify=False)
        #print(result.json())
        self.assertEqual(result.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result.text)

    def test03(self):
        self.mylog.info('这是第三个测试用例:申购单一级审核')
        url3 = "/cg/askbuy/audit"
        request_data3 = {
        		"agree": 1,
        		"auditUser": "tangshibin",
        		"comments": "ok",
        		"nos": [self.askBuyNo]
                }
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"pengfu","pengfu")
        result4 = self.session.post(self.erp_host+url3, data=json.dumps(request_data3), headers=self.erp_header, cookies=cookies, verify=False)
        self.mylog.info(result4.text)


    def test04(self):
        self.mylog.info('这是第四个测试用例:申购单二级审核')
        url4 = "/cg/askbuy/audit"
        request_data4 = {
        		"agree": 1,
        		"auditUser": "admin",
        		"comments": None,
        		"nos": [self.askBuyNo]
        }
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"tangshibin", "tangshibin")
        result4 = self.session.post(self.erp_host+url4, data=json.dumps(request_data4), headers=self.erp_header, cookies=cookies, verify=False)
        self.assertEqual(result4.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result4.text)

    def test05(self):
        global pleasebuy_code    #定义全局变量，保存请购单后把请购单号复制给这个全局变量，下一个用例请购单审续审核用
        self.mylog.info('这是第五个测试用例:申购单保存请购单')
        self.mylog.info("————先查询申购单明细，获取sourceId———— ")
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"yinjing", "yinjing")
        url5 = "/cg/askbuy/getInfo/"+self.askBuyNo+"?_="+str(self.current_milli_time_13)
        result5 =self.session.get(self.erp_host+url5,params=cookies)
        #print(type(result2.json()))
        global askbuydetailsourceId
        askbuydetailsourceId = eval(result5.json()["askBuy"]["askBuyDetails"])[0]["id"]
        self.mylog.info(askbuydetailsourceId)
        request_data6 = {
            "pleaseBuy": {
                "deptId": "58",
                "deptName": "研发二部",
                "employId": 90,
                "employName": "王金河",
                #"pCode": self.pCode,
                "userId": None,
                "userName": None,
                "remark": None,
                "mBillId": None,
                "reviewUser": "wangjinhe",
                "bomStockName": None,
                "sourceOrderCode": self.askBuyNo,
                "company": "3",
                "askPerson": "PC69420200320113758",
                "askPersonName": "廖梦芸",
                "makerId": 101,
                "makerName": "wangjinhe",
                "pDate": self.d_date,
                "address": "厦门市集美区孙坂南路86~88号 88-1 南楼2楼仓库（务必送货上楼，禁止放置快递柜）；厦门四信电子技术有限公司；收件人：杨尚志；电话：0592-6021827、15934715030",
                "auditStatus": 0,
                "billStatus": 1,
                "auditId": "",
                "auditDate": None
            },
            "pleaseBuyDetails": [{
                "brand": "1",
                "stockCode1": self.stockCode,
                "askType": "3",
                "deliveryAddress": " 软三A06,11楼",
                "sourceId": askbuydetailsourceId,
                "deptId": "58",
                "deptName": "研发二部",
                "askPerson": "PC69420200320113758",
                "projectName": "",
                "projectCode": "",
                "askPersonName": "廖梦芸",
                "quantity": self.quantity,
                "stockCode": self.stockCode,
                "stockName": "3.PK.0004-3.PK.0004-电源适配器",
                "needDate": self.d_date,
                "stockModel": "插墙型（竖）,P-046B-B3115-V1,黑色,VAC100~240V 50/60Hz,12V&1.5A@18W,DC输出线长1.5M,DC 5.5*2.5,尺寸:85*53.5*33mm,CCC",
                "remark": "MO-2021-10-29-0006",
                "priceRemark": "",
                "unit": "PCS",
                "totalStockCount": 6260,
                "stockCount": 6259,
                "sendType": "0",
                "executeQuantity": "",
                "company": "3"
            }]
        }
        url6 = "/cg/pleasebuy/save"
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"wangjinhe", "wangjinhe")
        result6 = self.session.post(self.erp_host + url6, data=json.dumps(request_data6), headers=self.erp_header, cookies=cookies, verify=False)
        self.assertEqual(result6.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result6.text)
        pleasebuy_code =eval(result6.text)["newCode"]
        #print(pleasebuy_code)


    def test06(self):
        self.mylog.info('这是第六个测试用例:请购单审核')
        self.mylog.info(pleasebuy_code)
        url7 = "/cg/pleasebuyAudit/auditBatch"
        request_data7= {"codes":[pleasebuy_code],"auditStatus":1,"auditMark":""}
        #print(request_data7)
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"wangjinhe", "wangjinhe")
        before_pleaseunexecute_quantity = self.st_stock_quantity.query_quantity("please_unexecute", self.stockCode, 3)
        result7 = self.session.post(self.erp_host + url7, data=json.dumps(request_data7), headers=self.erp_header, cookies=cookies,verify=False)
        self.assertEqual(result7.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result7.text)
        after_pleaseunexecute_quantity = self.st_stock_quantity.query_quantity("please_unexecute", self.stockCode, 3)
        self.st_stock_quantity.judege_after_before("please_unexecute", before_pleaseunexecute_quantity,after_pleaseunexecute_quantity, self.quantity, "请购未执行量")

    def test07(self):
        global  pleasebuy_id
        self.mylog.info('这是第六个测试用例:请购单价格确认')
        sql = "select id from cg_please_buy_detail WHERE P_code = '{0}'".format(pleasebuy_code)   #f 跟format %类似
        #print(sql)
        pleasebuy_id = self.SqlServer.query_one_data(sql)[0]
        url8 = "/cg/pleasebuydetail/confirmPrice"
        request_data7 = {"ids":[pleasebuy_id],"priceConfirm":1}
        #print(request_data7)
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"tangliming", "tangliming")
        result7 = self.session.post(self.erp_host + url8, data=json.dumps(request_data7), headers=self.erp_header, cookies=cookies, verify=False)
        self.assertEqual(result7.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result7.text)

    def test08(self):
        self.mylog.info('这是第七个测试用例:请购单保存为采购单')
        #print(pleasebuy_code)
        sql = ''' select a.recommend_stock_code,a.recommend_supplier_code,b.supplier_name ,a.recommend_time ,c.person_name
                    from cg_please_buy_detail_recommend  a
                    JOIN base_supplier b  ON a.recommend_supplier_code = b.supplier_code
                    JOIN base_person c on a.dev_buyer_user = c.user_id
                    WHERE a.p_code = '{0}'
                    '''.format(pleasebuy_code)
        res = self.SqlServer.query_one_data(sql)
        """res =(3201010002-74E,2130014,厦门市科力电子有限公司,2021-10-30 10:31:31.273,管理员 )"""
        url8 = "/cg/buyorder/save"
        request_data8 = {
            "buyOrder":{
            "businessId":63,
            "businessName":"黄立灵",
            "bCode":self.d_date,
            "makerId":72,
            "makerName":"huangliling",
            "supplierName":res[2],
            "supplierId":802,
            "supplierCode":None,
            "storeId":None,
            "storeName":None,
            "sourcePleaseCode":None,
            "address":"软三A06,11楼",
            "customsCompany":None,
            "customsCompanyName":None,
            "supplierContact":"郑君恩",
            "supplierContactPhone":"13599924981",
            "reviewUser":"huangliling",
            "company":3,
            "bDate":self.d_date,
            "auditStatus":0,
            "billStatus":1,
            "auditId":"",
            "auditDate":None
            },
            "buyOrderDetails":[
            {
            "sourceId":pleasebuy_id,
            "quantity":self.quantity,
            "currencyName":"人民币",
            "exchangeRate":1,
            "brand":"1",
            "askType":"3",
            "stockCode":self.stockCode,
            "currency":0,
            "unit":"PCS",
            "deptId":58,
            "deptName":"研发二部",
            "priceType":1,
            "projectName":"",
            "projectCode":"",
            "stockName":"3.PK.0004-3.PK.0004-电源适配器",
            "stockModel":"插墙型（竖）,P-046B-B3115-V1,黑色,VAC100~240V 50/60Hz,12V&1.5A@18W,DC输出线长1.5M,DC 5.5*2.5,尺寸:85*53.5*33mm,CCC",
            "sourceStockCode":self.stockCode,
            "mBillId":"",
            "bomStockName":"",
            "needDate":self.date3,
            "executeQuantity":0,
            "moq":1000,
            "mpq":1000,
            "priceTime":"2020-04-14",
            "quoteBrand":res[2],
            "priceFee":"0",
            "quotedPrice":"9.11504424778761",
            "price":"9.11504424778761",
            "taxRate":13,
            "taxPrice":10.3,
            "taxAmount":"29.62",
            "amount":"227.88",
            "supplierName":res[2],
            "supplierId":802,
            "sendType":"0",
            "pCode":pleasebuy_code,
            "supplierCode":res[1],
            "recommendSupplierCode":res[1],
            "recommendSupplierName":res[2],
            "recommendStockCode":res[0],
            "recommendReason":"",
            "recommendTime":res[3].strftime('%Y-%m-%d %H:%M:%S'),
            "devBuyerUserName":res[4],
            "cgPleaseBuyDetailRecommendId":237,
            "allStockCount":8285,
            "stockCount":8284,
            "expectArrivalDate":self.d_date,
            "company":3
            }
            ]
            }
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"huangliling","huangliling")
        result8 = self.session.post(self.erp_host + url8, data=json.dumps(request_data8), headers=self.erp_header, cookies=cookies, verify=False)
        self.assertEqual(result8.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result8.text)
        #global buy_code
        #buy_code = eval(result8.text)["newCode"]
        #self.mylog.info(buy_code)

    def test09(self):
        self.mylog.info('这是第九个测试用例:采购单经理审核')
        #print(buy_code)
        url9 = "/cg/buyorderaudit/auditBatch"
        request_data9 = {"reviewUser":"liutianshou","bCodes":[buy_code],"auditStatus":1,"auditMark":""}
        #print(request_data9)
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"huangliling", "huangliling")
        result9 = self.session.post(self.erp_host + url9, data=json.dumps(request_data9), headers=self.erp_header, cookies=cookies,
                               verify=False)
        self.assertEqual(result9.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result9.text)

    def test10(self):
        self.mylog.info('这是第十个测试用例:采购单成本会计审核')
        #print(buy_code)
        url10 = "/cg/buyorderaudit/auditBatch"
        request_data10 = {"reviewUser":"liutianshou","bCodes":[buy_code],"auditStatus":3,"auditMark":""}
        cookies = self.get_cookie.get_cookie(self.session,self.erp_host,self.erp_login_header,"liutianshou", "liutianshou")
        before_pleaseunexecute_quantity = self.st_stock_quantity.query_quantity("please_unexecute", self.stockCode, 3)
        before_buyway_quantity = self.st_stock_quantity.query_quantity("buy_way", self.stockCode, 3)
        result10 = self.session.post(self.erp_host+url10, data=json.dumps(request_data10), headers=self.erp_header, cookies=cookies,verify=False)
        self.assertEqual(result10.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result10.text)
        after_pleaseunexecute_quantity = self.st_stock_quantity.query_quantity("please_unexecute", self.stockCode, 3)
        self.st_stock_quantity.judege_before_after("please_unexecute", before_pleaseunexecute_quantity,after_pleaseunexecute_quantity, self.quantity, "请购未执行量")
        after_buyway_quantity = self.st_stock_quantity.query_quantity("buy_way", self.stockCode, 3)
        self.st_stock_quantity.judege_after_before("buy_way", before_buyway_quantity, after_buyway_quantity,self.quantity, "采购在途量")

    def test11(self):
        i = random.randint(0, 9999)
        #cls.date3 = (datetime.datetime.now() + datetime.timedelta(days=4)).strftime('%Y-%m-%d')  # 当前日期+3
        num_str = str(i).zfill(4)
        waybill = self.date + "-" + num_str
        self.mylog.info('这是第十一个测试用例:报价系统供应商发货')
        """先查询获取供应商编码和采购明细sourceid及stockCode"""
        cookies = self.get_cookie.get_cookie(self.session,self.baojia_host,self.erp_login_header,"admin","xmsx123!@#")
        url = self.baojia_host +"/quote/order/list?supplierCode=&priceFee=0&_search=false&nd="+str( self.current_milli_time_13)+"&limit=50&page=1&sidx=type&order=asc&bCode="+buy_code+"&supplierName=&stockCode=&_="+str( self.current_milli_time_13)
        result11_1 = self.session.get( url,params=cookies)
        self.mylog.info(result11_1.json())
        sourid = result11_1.json()["page"]["list"][0]["id"]
        global stockCode,supplierCode,quantity
        stockCode = result11_1.json()["page"]["list"][0]["sourceStockCode"]
        supplierCode =result11_1.json()["page"]["list"][0]["supplierCode"]
        quantity  = result11_1.json()["page"]["list"][0]["quantity"]
        url11 ="/quote/order/addSend"
        request_data11 = {
                        "send":{
                        "bCode":None,
                        "supAnsDate":self.date3,
                        "waybill":waybill,
                        "remark":None
                        },
                        "details":[
                        {
                        "sourceId":sourid,
                        "quantity":quantity,
                        "stockCode":stockCode,
                        "supplierCode":supplierCode
                        }
                        ]
                        }
        before_buyway_quantity = self.st_stock_quantity.query_quantity("buy_way", self.stockCode, 3)
        before_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in", self.stockCode, 3)
        result11 = self.session.post(self.baojia_host+url11, data=json.dumps(request_data11), headers=self.erp_header, cookies=cookies,verify=False)
        self.assertEqual(result11.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result11.text)
        after_buyway_quantity = self.st_stock_quantity.query_quantity("buy_way", self.stockCode, 3)
        self.st_stock_quantity.judege_before_after("buy_way", before_buyway_quantity, after_buyway_quantity,self.quantity, "采购在途量")
        after_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in", self.stockCode, 3)
        self.st_stock_quantity.judege_after_before("purchase_wait_in", before_purchasewaitin_quantity,after_purchasewaitin_quantity, self.quantity, "进货待入量")

    @unittest.skip
    def test12(self):
        self.mylog.info('这是第十二个测试用例:申购人申购明细确认收货')
        cookies = self.get_cookie.get_cookie(self.session, self.erp_host, self.erp_login_header, "yinjing", "yinjing")
        url12 = "/cg/askbuydetail/confirmPurchase_direct?purchaseNum="+str(self.quantity)+"&id="+str(askbuydetailsourceId)+"&scCode=MO-2021-10-29-0006&askBuyNo="+self.askBuyNo+"&stockCode="+self.stockCode+"&outStoreDirectFlag=Y"
        before_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in", self.stockCode,3)
        before_stockcount_quantity = self.st_stock_quantity.query_quantity("stock_count", self.stockCode, 3)
        result12 = self.session.post(self.erp_host+url12,headers=self.erp_header,cookies=cookies,verify=False)
        self.assertEqual(result12.json()["msg"], "success", msg="接口请求失败")
        self.mylog.info(result12.text)
        after_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in", self.stockCode, 3)
        self.st_stock_quantity.judege_before_after("purchase_wait_in", before_purchasewaitin_quantity,after_purchasewaitin_quantity, self.quantity, "进货待入量")
        after_stockcount_quantity = self.st_stock_quantity.query_quantity("stock_count", self.stockCode, 3)
        self.st_stock_quantity.judege_after_before("stock_count", before_stockcount_quantity, after_stockcount_quantity, self.quantity, "现存量")

    @classmethod
    def tearDownClass(cls):
        cls.mylog.info("直发客户申购测试流程结束")
        @unittest.skip
        def test13(self):
            self.mylog.info('这是第十三个测试用例:弃审确认收货自动审核的出库单')
            cookies = self.get_cookie.get_cookie(self.session, self.erp_host, self.erp_login_header, "yinjing","yinjing")
            url13 = ""
            before_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in", self.stockCode,3)
            before_stockcount_quantity = self.st_stock_quantity.query_quantity("stock_count", self.stockCode, 3)
            result13 = self.session.post(self.erp_host + url13, headers=self.erp_header, cookies=cookies, verify=False)
            self.assertEqual(result13.json()["msg"], "success", msg="接口请求失败")
            self.mylog.info(result13.text)
            after_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in", self.stockCode, 3)
            self.st_stock_quantity.judege_before_after("purchase_wait_in", before_purchasewaitin_quantity, after_purchasewaitin_quantity, self.quantity, "进货待入量")
            after_stockcount_quantity = self.st_stock_quantity.query_quantity("stock_count", self.stockCode, 3)
            self.st_stock_quantity.judege_after_before("stock_count", before_stockcount_quantity,after_stockcount_quantity, self.quantity, "现存量")

        @unittest.skip
        def test13(self):
                self.mylog.info('这是第十三个测试用例:弃审确认收货自动审核的出库单')
                cookies = self.get_cookie.get_cookie(self.session, self.erp_host, self.erp_login_header, "yinjing","yinjing")
                url13 = ""
                before_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in",self.stockCode, 3)
                before_stockcount_quantity = self.st_stock_quantity.query_quantity("stock_count", self.stockCode, 3)
                result13 = self.session.post(self.erp_host + url13, headers=self.erp_header, cookies=cookies,verify=False)
                self.assertEqual(result13.json()["msg"], "success", msg="接口请求失败")
                self.mylog.info(result13.text)
                after_purchasewaitin_quantity = self.st_stock_quantity.query_quantity("purchase_wait_in",self.stockCode, 3)
                self.st_stock_quantity.judege_before_after("purchase_wait_in", before_purchasewaitin_quantity,after_purchasewaitin_quantity, self.quantity, "进货待入量")
                after_stockcount_quantity = self.st_stock_quantity.query_quantity("stock_count", self.stockCode, 3)
                self.st_stock_quantity.judege_after_before("stock_count", before_stockcount_quantity,after_stockcount_quantity, self.quantity, "现存量")

if __name__ == '__main__':
    unittest.main()
