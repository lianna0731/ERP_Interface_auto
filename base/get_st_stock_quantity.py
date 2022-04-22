#coding:utf-8
from base.sqlserver_connection import SqlServer_connectin
from base.my_log import MyLog

class Get_st_stock_quantity:
    def __init__(self):
        self.SqlServer = SqlServer_connectin()
        self.mylog = MyLog()
    def query_quantity(self,quantity_type,stockcode,company):
        #sql = "SELECT "+ quantity_type + " FROM st_stock WHERE stock_code='1001011012-731' AND company=3"
        sql = "SELECT {0} FROM st_stock WHERE stock_code='{1}' AND company={2}".format(quantity_type,stockcode,company)
        quantity = self.SqlServer.query_one_data(sql)
        return quantity[0]
    def judege_after_before(self,quantity_type,before,after,quantity,typename):
        if before+int(quantity) ==after:
            #print("审核前{0}数值是{1}，审核后{0}数值是{2}，审核后{0}数量正确".format(quantity_type,before,after))
              self.mylog.info("审核前{0}{3}数值是{1}，审核后{0}数值是{2}，审核后{0}数量正确".format(quantity_type,before,after,typename))
        else:
             self.mylog.info("审核前{0}{3}数值是{1}，审核后{0}数值是{2}，审核后数量{0}不正确".format(quantity_type,before,after,typename))

    def judege_before_after(self,quantity_type,before,after,quantity,typename):
        if before-int(quantity) ==after:
            #print("审核前{0}数值是{1}，审核后{0}数值是{2}，审核后{0}数量正确".format(quantity_type,before,after))
              self.mylog.info("审核前{0}{3}数值是{1}，审核后{0}数值是{2}，审核后{0}{3}数量正确".format(quantity_type,before,after,typename))
        else:
             self.mylog.info("审核前{0}{3}数值是{1}，审核后{0}数值是{2}，审核后数量{0}{3}不正确".format(quantity_type,before,after,typename))

if __name__ =="__main__":
    quantity =Get_st_stock_quantity().query_quantity("please_unexecute",'1001011012-731',3)
    print(quantity)
    print(type(quantity)) #<class 'decimal.Decimal'>
    #print(quantity+1)
    res =  Get_st_stock_quantity().judege_before_after("please_unexecute",1,2,0,"请购单")
    #quantity_type = "please_unexecute"
    # sql = "SELECT {0} FROM st_stock WHERE stock_code='1001011012-731' AND company=3".format(quantity_type)
    # print(sql)
    # sql = "SELECT " + quantity_type + " FROM st_stock WHERE stock_code='1001011012-731' AND company=3"
    # print(sql)