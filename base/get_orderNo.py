#coding:utf-8

import random
import time
import datetime
from base.my_log import  MyLog
class Get_OrderNo:
        def __init__(self,i,test_Category):
                mylog = MyLog()
                # 获取随机4位数拼接申购单编号
                #i = random.randint(1,9999)
                self.date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                self.date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                self.num_str = str(i).zfill(4)
                self.askBuyNo = "AB-" + self.date + "-" + self.num_str  #申购单号
                #mylog.info("{0}的申购单号是：{1}" .format(test_Category,self.askBuyNo))
                self.PleasebuyCode = "PQ-" + self.date + "-" + self.num_str   #请购单号
                #mylog.info("{0}的请购单号是：{1}".format(test_Category,self.PleasebuyCode))
                self.PurchaseCode = "PS-" + self.date + "-" + self.num_str  #进货单号
                #mylog.info("{0}的进货单号是：{1}".format(test_Category,self.PurchaseCode))
                self.inStoreNo = "II-" + self.date + "-" + self.num_str   #入库单号
                #mylog.info("{0}的入库单号是：{1}".format(test_Category,self.inStoreNo))
                self.scorderNo = "MO-" + self.date + "-" + self.num_str  # 组装生产单号
                #mylog.info("{0}的组装生产单号是：{1}".format(test_Category, self.scorderNo))
                self.date3 = (datetime.datetime.now() + datetime.timedelta(days=4)).strftime('%Y-%m-%d')  # 当前日期+3
                self.date1 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                self.d_date = time.strftime('%Y-%m-%d 08:00:00', time.localtime(time.time()))
                #把秒转换毫秒的方法获得13位的时间戳,round()是四舍五入
                millis = int(round(time.time() * 1000))  # 把秒转换毫秒的方法获得13位的时间戳,round()是四舍五入
                current_milli_time = lambda: int(round(time.time() * 1000))
                self.current_milli_time_13 = current_milli_time()


if __name__=="__main__":
   print(Get_OrderNo(1,"ceshi").date1)


