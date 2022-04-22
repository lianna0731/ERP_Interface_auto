#coding:utf-8

from selenium import webdriver
import requests
import time
import re
from base.my_log import  MyLog
session = requests.session()
class Login:
    global session
    def login(self,url, username, psw,usenamexpath,pswxpath,loginbuttonxpath):
        self.mylog = MyLog()
        option = webdriver.FirefoxOptions()
        option.add_argument("-headless")   #静默方式，火狐headless前面要加-，谷歌不用
        driver = webdriver.Firefox(firefox_options=option)
        driver.get(url)
        #driver.maximize_window()
        # 先登录
        driver.find_element_by_xpath(usenamexpath).send_keys(username)
        driver.find_element_by_xpath(pswxpath).send_keys(psw)
        driver.find_element_by_xpath(loginbuttonxpath).click()
        time.sleep(3)
        allcookies = driver.get_cookies()  # 获取浏览器cookies
        self.mylog.info("获取到登录后的cookies:%s" % allcookies)
        # 把抓取的cookies添加到s中
        driver.quit()
        return allcookies

    def add_cookies(self,allcook):
        '''往session添加cookies'''
        try:
            # 添加cookies到CookieJar
            c = requests.cookies.RequestsCookieJar()
            for i in allcook:
                c.set(i["name"], i['value'])
            session.cookies.update(c)  # 更新session里cookies
        except Exception as msg:
            self.mylog.info(u"添加cookies的时候报错了：%s" % str(msg))
        return session.cookies

if __name__=="__main__":
    login_ = Login()
    usenamexpath = "html/body/div/div[1]/div[1]/div[1]/input"
    pswxpath = "html/body/div/div[1]/div[1]/div[2]/input"
    loginbuttonxpath = "html/body/div/div[1]/div[1]/div[3]/div/button"
    allcookies =  login_.login("http://192.168.10.238:19001/login.html", "yinjing", "yinjing",usenamexpath,pswxpath,loginbuttonxpath)
    cookies = login_. add_cookies(allcookies)
    print(cookies)
    url6 = "http://192.168.10.238:19001/cg/askbuydetail/list?billStartDate=&billEndDate=&askBuyNo=&company=&askDepartment=&askDepartmentName=&askPerson=&askStatus=&stockCode=&stockName=&billStatus=-1&purchaseStatus=-1&askType=&page=1&rows=20&sort=a.ask_buy_no&order=DESC&_=1625457176448.html"
    result2 =session.get(url6,params=session.cookies)
    print(result2.text)