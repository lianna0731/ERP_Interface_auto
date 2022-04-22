#coding:utf-8
import time
import random
import requests
import json
from requests_toolbelt import MultipartEncoder
#
#
# # millis = int(round(time.time() * 1000))   #把秒转换毫秒的方法获得13位的时间戳,round()是四舍五入
# # current_milli_time = lambda: int(round(time.time() * 1000))
# # current_milli_time_13 = current_milli_time()
# # print(current_milli_time_13)
# #
# # i = random.randint(0,9999)
# # date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# # print(date)
# # num_str =str(i).zfill(4)
# #
# # askBuyNo = "AB-" + date+"-"+num_str
# # url6 = "http://192.168.10.238:19001/cg/askbuy/getInfo/"+askBuyNo+"?_="+str(current_milli_time_13)
# # print(url6)
# #
# # sourceId = 123456
# # j = random.randint(0,9999)
# # date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# # num_str =str(j).zfill(4)
# # pCode = "PQ-" + date+"-"+num_str
# # pDate =time.strftime('%Y-%m-%d 08:00:00', time.localtime(time.time()))
#
# import requests
# import json
# #这是一个python通过urllib直接登陆网站，并处理网站的session和cookie
#
# from http import cookiejar
# import 	urllib,urllib.request,urllib.parse    #python3
#
# username = 'yinjing'
#
# password = 'yinjing111111'
#
# # Enable cookie support for urllib2
#
# cookiejar = cookiejar.CookieJar()
#
# urlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
#
# # Send login/password to the site and get the session cookie
#
# values = {'username':username, 'password':password }
#
# data = urllib.parse.urlencode(values).encode("utf-8")
# print(type(data))
#
# request = urllib.request.Request("http://192.168.10.238:19001/sys/login", data)
#
# url = urlOpener.open(request) # Our cookiejar automatically receives the cookies
# page = url.read(500000)
# print(page)
#
# if not 'ERP_SID' in [cookie.name for cookie in cookiejar]:
#
#     raise ValueError("Login failed with login=%s, password=%s" % (username,password))
#
# print ("We are logged in !")
#
#
# result = urlOpener.open('http://192.168.10.238:19001/cg/askbuydetail/list?billStartDate=&billEndDate=&askBuyNo=&company=&askDepartment=&askDepartmentName=&askPerson=&askStatus=&stockCode=&stockName=&billStatus=-1&purchaseStatus=-1&askType=&page=1&rows=20&sort=a.ask_buy_no&order=DESC&_=1625457176448.html')
# page= url.read(500000)
# print(page)



#
# list2 =[]
#
# for j in range(0,3):
#     list1 = []
#     for i in range(0,8):
#         ran = random.randint(0,1)
#         list1.append(ran)
#     list2.append(list1)
# print(list2)
# pleasebuy_code = 'PQ-2021-08-28-0010'
# sql = "select id from cg_please_buy_detail WHERE P_code = '{0}'".format(pleasebuy_code)     #字符串里嵌入单引号
# print(sql)
#session = requests.session()
# header_login = {
# 		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# 		"Accept-Language": "zh-CN,zh;q=0.9",
# 		"Accept-Encoding": "gzip,deflate",
# 		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
# 		"Connection":"keep-alive",
# 		"cookie":"Supplier_SID=f42c94a4-fe1d-418d-b015-eaf25728cf0d"
# 		}
# login = "http://192.168.10.238:10031/login.html"
# login_url = "http://192.168.10.238:10031/sys/login.html"
# headers = {
# 			"Accept": "application/json, text/javascript, */*; q=0.01",
# 			"Accept-Language": "zh-CN,zh;q=0.9",
# 			"Accept-Encoding": "gzip,deflate",
# 			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
# 			"Content-Type": "application/json",
# 			"Connection":"keep-alive"
# 			}

# data = {
#           	"username":" admin",
# 			"password":" xmsx123!@#"
# 		}
# result = session.get(login,params=header_login)
# print("获取第一登录的cookies:%s" % session.cookies)
#result = session.get(login,params=header_login)
#print(result)
#result1 = session.post(login_url,data=json.dumps(data),headers=header_login)
#print("获取到登录后的cookies:%s" % session.cookies.get_dict() )
#url6 = "http://192.168.10.238:19001/cg/askbuydetail/list?billStartDate=&billEndDate=&askBuyNo=&company=&askDepartment=&askDepartmentName=&askPerson=&askStatus=&stockCode=&stockName=&billStatus=-1&purchaseStatus=-1&askType=&page=1&rows=20&sort=a.ask_buy_no&order=DESC&_=1625457176448.html"
#result2 =session.get(url6,params=session.cookies.get_dict())
#print(result2.text)



from base.web_Login_Getcookie import Login
from urllib3 import encode_multipart_formdata
from selenium import webdriver
login_ = Login()
session = requests.session()
# erp_usenamexpath = "html/body/div/div[1]/div[1]/div[1]/input"
# erp_pswxpath = "html/body/div/div[1]/div[1]/div[2]/input"
# erp_loginbuttonxpath = "html/body/div/div[1]/div[1]/div[3]/div/button"
# url13 = "http://192.168.10.238:19001/cg/purchase/iqcAudit"
#
# with open(r"C:\Users\Administrator\Desktop\ERP.doc", mode="rb") as f: # 打开文件，路径不能带中文
# 	file = {
# 		"uploadfile": ("", ""),# 引号的file是接口的字段，后面的是文件的名称、文件的内容
# 		"dtoData": "{\"purchase\":{\"reviewUser\":\"zhangfeng\",\"iqcAuditStatus\":1,\"pCode\":\"PS-2021-10-11-5603\",\"auditMark\":\"\"},\"purchaseDetails\":[{\"id\":21493,\"stockCode\":\"1001011012-731\",\"quantity\":200,\"qualifiedQuantity\":200,\"auditMark\":\" \"}]}" # 如果接口中有其他字段也可以加上
# 	}
# encode_data = encode_multipart_formdata(file)
# file_data = encode_data[0]
# #  filename="ERP.doc"\r\nContent-Type: text/plain\r\n\r\n...........--c0c46a5929c2ce4c935c9cff85bf11d4--\r\n
#
# header = {
# 		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# 		"Accept-Language": "zh-CN,zh;q=0.9",
# 		"Accept-Encoding": "gzip,deflate",
# 		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
# 		"Content-Type": encode_data[1]     #一定要加上这个，没加发送请求返回登录
#
# 		}
# #"dtoData": {"purchase":{"reviewUser":"zhangfeng","iqcAuditStatus":1,"pCode":"PS-2021-10-11-5603","auditMark":""},"purchaseDetails":[{"id":21583,"stockCode":"1001011012-731","quantity":200,"qualifiedQuantity":200,"auditMark":None}]}
# #"dtoData": {\"purchase\":{\"reviewUser\":\"zhangfeng\",\"iqcAuditStatus\":1,\"pCode\":\"PS-2021-10-11-5603\",\"auditMark\":\"\"},\"purchaseDetails\":[{\"id\":21583,\"stockCode\":\"1001011012-731\",\"quantity\":200,\"qualifiedQuantity\":200,\"auditMark\":None}]}
# allcookies = login_.login("http://192.168.10.238:19001/login.html", "zhangfeng", "zhangfeng", erp_usenamexpath,erp_pswxpath, erp_loginbuttonxpath)
# cookies = login_.add_cookies(allcookies)
# #print(cookies)
# result13 = session.post( url13,headers=header,cookies=cookies,data=file_data,verify=False)
# #res = session.get("http://192.168.10.238:19001/cg/purchase/list?pDateBegin=&pDateEnd=&pCode=&deptName=&deptId=&auditStatus=&businessName=&businessId=&supplierId=&supplierName=&iqcAuditStatus=&businessType=&nobusinessType=&company=&bills=1%2C2&page=2&rows=20&_=1634003203653",params=cookies)
# print(result13.text)
#print(res.text)
# if result13.json()["msg"] == "success":
# 	print("接口请求成功")
# else:
# 	print("接口请求失败")
#print(result13.text)



##得到cookiejar和字典格式互转
#dict_cookie = requests.utils.dict_from_cookiejar(session.cookies)
#print(dict_cookie)


# str_cookie = json.dumps(dict_cookie)
# cookie_dict = json.loads(str_cookie)
#jarcookie = requests.utils.cookiejar_from_dict(dict_cookie)
#print(jarcookie)
# millis = int(round(time.time() * 1000))   #把秒转换毫秒的方法获得13位的时间戳,round()是四舍五入
# current_milli_time = lambda: int(round(time.time() * 1000))
# current_milli_time_13 = current_milli_time()


# import datetime
# i = random.randint(0, 9999)
# date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# date2 = (datetime.datetime.now()+datetime.timedelta(days=4)).strftime('%Y-%m-%d') #当前日期+3
# num_str = str(i).zfill(4)
# waybill = date + "-" + num_str
# print(waybill)
# print(date2)


# # 把秒转换毫秒的方法获得13位的时间戳,round()是四舍五入
# millis = int(round(time.time() * 1000))  # 把秒转换毫秒的方法获得13位的时间戳,round()是四舍五入
# current_milli_time = lambda: int(round(time.time() * 1000))
# current_milli_time_13 = current_milli_time()
# # print(current_milli_time_13)
# url = "Request URL: http://192.168.10.238:10031/quote/order/list?supplierCode=&priceFee=0&_search=false&nd=" + str(
# 	current_milli_time_13) + "&limit=50&page=1&sidx=type&order=asc&bCode=PO-2021-09-09-0004&supplierName=&stockCode=&_=" + str(current_milli_time_13)
# print(url)
# from base.sqlserver_connection import SqlServer_connectin
# SqlServer = SqlServer_connectin()
# sql = """select a.id,b.batch_number,b.id,a.stock_code
# 	            from cg_buy_order_detail  a
# 	            JOIN cg_send_detail b  ON a.id = b.source_id
# 	            WHERE a.b_code = 'PO-2021-10-08-0008' """  #f 跟format %类似
# print(sql)
# buydetail_id = SqlServer.query_one_data(sql)[0]
# batchNumber = SqlServer.query_one_data(sql)[1]
# sendId = SqlServer.query_one_data(sql)[2]
# stockCode = SqlServer.query_one_data(sql)[3]
# print(buydetail_id)
# print(batchNumber)
# print(sendId)
# print(stockCode)
