import requests
from base.read_config import ReadConfig
from base import get_project_path
import json
class Get_cookie:
    def get_cookie(self,session,host,header,username,password):
        request_data = {"username":username,
                        "password":password}
        session.post(host+"/sys/login",data=request_data,headers=header)
        return session.cookies

    def customer_sys_get_cookies(self,session,host,login_request_data,header):
        result = session.get(host+"/customer/login.do",headers=header) #先获取cookie
        #print(session.cookies)
        result2 = session.post(host+"/customer/userLogin.do", data=login_request_data,headers=header,cookies=session.cookies) #再登录
        #print(result2.text)
        return session.cookies


if __name__=="__main__":
    conf_path = get_project_path.config_path
    erp_host = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['host']
    erp_header = eval(ReadConfig.get_config(get_project_path.config_path, "ERP", "erp"))['login_header']
    session = requests.session()
    cookies = Get_cookie().get_cookie(session,erp_host,erp_header,"yinjing","yinjing")
    url = "http://192.168.10.238:19001/cg/askbuydetail/list?billStartDate=&billEndDate=&askBuyNo=&company=&askDepartment=&askDepartmentName=&askPerson=&askStatus=&stockCode=&stockName=&billStatus=-1&purchaseStatus=-1&askType=&page=1&rows=20&sort=a.ask_buy_no&order=DESC&_=1625457176448.html"
    result = session.get(url, params=cookies)
    print(result.text)