#coding:utf-8
#import pymysql
import pymssql
import json
import time
import datetime
from base.read_config import ReadConfig
from base import get_project_path


# connection = pymssql.connect(host="192.168.15.49\SQLSERVER2012",
#                                      port=1322,
#                                      user='erp',
#                                      password='erp123!@#',
#                                      database="ERP_DEV_0707",
#                                      charset='utf8'
#                      )
#
# cur = connection.cursor()   #创建邮标
# cur.execute("select id from cg_please_buy_detail WHERE P_code = 'PQ-2021-08-28-0010'") #执行数据库查询语句
# result = cur .fetchall() #获取查询结果
# print(result)
# cur.close()

class SqlServer_connectin():
    def __init__(self):
        # self.connection = pymssql.connect(host="122.112.238.45",
        #                              port=1022,
        #                              user='erp',
        #                              password='erp123!@#',
        #                              database="ERP_DEV_0707",
        #                              charset='GBK',
        #                              #cursorclass = pymssql.cursor.DictCursor #获取结果转成字典
        #
        #                              )
        conf_path = get_project_path.config_path
        #print(conf_path)
        c1onnection = ReadConfig.get_config(conf_path, "DB", "connection")
        self.connection = eval(ReadConfig.get_config(get_project_path.config_path, "DB", "connection"))
        self.cur = self.connection.cursor()

    def query_one_data(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        result = result[0]
        return result

if __name__ =="__main__":

    shili =SqlServer_connectin()
    #sql = "select id from cg_please_buy_detail WHERE P_code = 'PQ-2021-08-28-0010'"
    #res = shili.query_one_data(sql)
    pleasebuy_code = 'PQ-2021-09-08-0007'
    sql = ''' select a.recommend_stock_code,a.recommend_supplier_code,b.supplier_name ,a.recommend_time ,c.person_name
            from cg_please_buy_detail_recommend  a
            JOIN base_supplier b  ON a.recommend_supplier_code = b.supplier_code
            JOIN base_person c on a.dev_buyer_user = c.user_id
            WHERE a.p_code = '{0}'
            '''.format(pleasebuy_code)

    res = shili.query_one_data(sql)
    #print(json.JSONEncoder.default(object=res[3]))


    Date = time.strftime('%Y-%m-%d 08:00:00',time.localtime(time.time()))

    request_data8 = {
        "buyOrder": {
            "businessId": 63,
            "businessName": "黄立灵",
            "bCode": Date,
            "makerId": 72,
            "makerName": "huangliling",
            "supplierName": "厦门信和达电子有限公司",
            "supplierId": 670,
            "supplierCode": None,
            "storeId": None,
            "storeName": None,
            "sourcePleaseCode": None,
            "address": "福建省厦门市同安区五显镇布塘中路11-8号6号楼6层仓库（务必送货上楼，禁止放置快递柜）；厦门四信电子技术有限公司 ，收件人：杨尚志 15934715030",
            "customsCompany": None,
            "customsCompanyName": None,
            "supplierContact": "黄宇坤",
            "supplierContactPhone": "18250870687",
            "reviewUser": "huangliling",
            "company": 3,
            "bDate": Date,
            "auditStatus": 0,
            "billStatus": 1,
            "auditId": "",
            "auditDate": None
        },
        "buyOrderDetails": [
            {
                "sourceId": 31626,
                "quantity": 200,
                "currencyName": "人民币",
                "exchangeRate": 1,
                "brand": "0",
                "askType": "1",
                "stockCode": "1001011012-731",
                "currency": 0,
                "unit": "PCS",
                "deptId": 58,
                "deptName": "研发二部",
                "priceType": 1,
                "projectName": "",
                "projectCode": "",
                "stockName": "1.RM.0141-1.RM.0141-贴片电阻",
                "stockModel": "SMD,33R,0402,±1%,1/16W",
                "sourceStockCode": "1001011012-731",
                "mBillId": "",
                "bomStockName": "",
                "needDate": "2021-08-04",
                "executeQuantity": 0,
                "moq": 1000,
                "mpq": 1000,
                "priceTime": "2020-09-03",
                "quoteBrand": "信和达",
                "priceFee": "0",
                "quotedPrice": "0.00194690265487",
                "price": "0.00194690265487",
                "taxRate": 13,
                "taxPrice": 0.0022,
                "taxAmount": "0.05",
                "amount": "0.39",
                "supplierName": "厦门信和达电子有限公司",
                "supplierId": 670,
                "sendType": "0",
                "pCode": pleasebuy_code,
                "supplierCode": "2100002",
                "recommendSupplierCode": res[1],
                "recommendSupplierName": res[2],
                "recommendStockCode": res[0],
                "recommendReason": "",
                "recommendTime": res[3],
                "devBuyerUserName": res[4],
                "cgPleaseBuyDetailRecommendId": 94,
                "allStockCount": 12719.997,
                "stockCount": 12479.997,
                "expectArrivalDate": Date,
                "company": 3
            }
        ]
    }
    print(request_data8)


    #pleasebuy_id = shili.query_one_data("select id from cg_please_buy_detail WHERE P_code = 'PQ-2021-08-28-0010'")[0]

    print(res)
    print(res[3].strftime('%Y-%m-%d %H:%M:%S'))
