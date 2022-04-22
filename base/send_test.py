#coding:utf-8

import requests
import json

class Send():

    def send_post(self,url,data,header=None,cookies=None,verify=False):
        if cookies != None:
            res = requests.post(url=url, data=data,headers=header,cookies=cookies,verify=False)
        else:
            res = requests.post(url=url,data=data,headers=header,verify=False)
        return res

    def send_get(self,url,header=None,cookies=None,data=None,verify=False):
        if cookies != None and data!=None:
            res = requests.get(url=url, params=data,headers=header,cookies=cookies,verify=False)
        if data!= None and cookies== None:
            res = requests.get(url=url, params=data,headers=header,verify=False)
        if data== None and cookies!= None :
            res = requests.get(url=url,headers=header, cookies=cookies,verify=False)
        else:
            res = requests.get(url=url,verify=False)
        return res

    def send_main(self,url,method,data=None,headers=None,cookies=None,verify=False):
        if method == 'POST':
            res = self.send_post(url,data,cookies)
            return res
            #return json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True)
        elif method == 'GET':
            res = self.send_get(url,cookies,data)
            return res
            #return json.dumps(res,ensure_ascii=False,indent=2,sort_keys=True) #GET请求返回的不能被处理成json格式会报错
            #
        else:
            return '错误输入'

if __name__=="__main__":
    url = 'https://www.imooc.com/u/card%20'
    url1 = 'http://192.168.9.230:19002/login'
    url2 = 'https://www.xmrc.com.cn/net/talent/ExperienceS.aspx'

    data = {'jsonpcallback': 'jQuery19109693617761826627_1559805393372',
            '_': '1559805393373'
            }
    data1 = {"username": "yinjing",
            "password": "yinjing"}

    header1={
        "Referer": "http://116.63.59.114:9001/login.html",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Encoding":" gzip,deflate",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Host":"116.63.59.114",
        "Connection":"Keep-Alive",
        "Cookie":"Supplier_SID=80366215-4457-4e6a-b092-e7fe13cc632f"
        }
    header2 = {
        "Accept": " text/html, application/xhtml+xml, image/jxr, */*",
        "Referer": " https://www.xmrc.com.cn/net/talent/Main.aspx",
        "Accept-Language": " zh-CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Accept-EncAoding": " gzip, deflate",
        "Host": " www.xmrc.com.cn",
        "Connection": " Keep-Alive",
        "Cookie": " __utmz=5198522.1560938645.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=5198522.775541798.1558350468.1560925500.1560938645.4; _trail=tid=95064794&tidn=F347B7641CE88004&sip=134; UM_distinctid=16ad4ed10d539a-0fc2db6db112c8-293e1d4e-100200-16ad4ed10d61ab0; _temp=tag=e758a1600136442c856d582fd4eb327f; __utmb=5198522.3.10.1560938645; __utmc=5198522; __utmt=1; _tid=9938451E3934C0CB787F4465D689CA20; CNZZDATA3869267=cnzz_eid%3D146949812-1558349030-%26ntime%3D1560936419; www.xmrc.com.cn=94955953; ASP.NET_SessionId=ndrnunixj5r11ptu404ejdfq",
    }
    send = Send()
    #res = send.send_main(url1,'POST',data1)

    #from base.get_cookies import GetCookies
    #shili_getcookie = GetCookies()


    res1= send.send_main(url1, 'POST', data1)
    print(res1.headers)
    #print(type(res1))
    #cookie = shili_getcookie.get_cookies(res1)
    # res2= send.send_main(url, 'GET',header2)
    # print(eval(res))
    # print(type(eval(res)))
    print(res1.text)
    # print(res2)

