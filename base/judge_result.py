#coding:utf-8
import json
import operator

class Judge_result():

    def is_content(self,str_one,str_two):
        """
        判断str_one是否在str_two中
        """
        flag = None
        if isinstance(str_one,int):
            str_one = str(str_one)
        if isinstance(str_two):
            str_two = str(str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self,dict1,dict2):
        if isinstance(dict1,str):
            dict1 = json.loads(dict1)
        if isinstance(dict2, str):
            dict2 = json.loads(dict2)
        res = operator.eq(dict1,dict2)
        return res
        # flag = 0
        # list = []
        # for i in dict1.items():
        #     if i in dict2.items():
        #         flag = 1
        #         list.append(flag)
        #     else:
        #         flag = 0
        #         list.append(flag)
        # if 0 in list:
        #     return False
        # else:
        #     return True








if __name__=='__main__':
    shili = Judge_result()
    #res = shili.is_content('"password": "6"','{"password": "6", "username": "admin"}')
    dict1 = {'goodsname': 'Java教程', 'remark': '北京动力节点', 'id': '402881e54506bb1701450754f5550040', 'state': 'closed', 'goodstype': '4', 'costprice': '88888'}
    dict2 = {'goodsname': 'Java教程', 'goodstype': '4', 'costprice': '88888', 'remark': '北京动力节点', 'id': '402881e54506bb1701450754f5550040', 'state': 'closed'}
    res = shili.is_equal_dict(dict1,dict2)
    print(res)
