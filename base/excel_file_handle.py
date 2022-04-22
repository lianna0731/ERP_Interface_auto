#coding:utf-8

import xlrd
from xlutils import copy

# xl = xlrd.open_workbook(r'E:\ERP_interface_Auto\test_file\inference1.xls')
# table = xl.sheets()[0]
# nrows = table.nrows
# print(nrows)
# value = table.cell(0,1).value
# print("这是value的值：%s" % value)
# value1 = table.cell_value(0,1)
# print("这是value1的值：%s" % value1)

class Excel_method():
    def __init__(self,file_path=None,id = None):
        if file_path:
            self.file_path = file_path
            self.id = id
        else:
            self.file_path = r"E:\ERP_interface_Auto\test_file\inference1.xls"
            self.id = 0
        self.data = self.excel()

    def excel(self):
        xl = xlrd.open_workbook(self.file_path)
        table = xl.sheets()[self.id]
        return table

    def sheet_nrow(self):
        table = self.data
        nrows = table.nrows
        return nrows

    def sheet_cell_value(self,row,col):
        table = self.data
        value = table.cell_value(row,col)
        return value

    def write_result_excel(self,col,row,value):
        xl = xlrd.open_workbook(self.file_path)
        excel_data = copy.copy(xl)
        sheet = excel_data.get_sheet(0)
        sheet.write(col,row,value)
        excel_data.save(self.file_path)

    """根据caseid找到对应的行内容"""
    def get_row_data(self,caseid):
        num = self.get_row_num(caseid)
        row_data = self.get_row_value(num)
        return row_data

    """根据caseid找到行号"""
    def get_row_num(self,casename=None):
        if casename !=None:
            casename = casename
            col_date = self.get_col_value()
            print(col_date)
            num = 0
            for col in col_date:
                if casename == col:
                    return num
                num = num + 1
        else:
            return None


    """根据行号找到该行内容"""
    def get_row_value(self,rows):
        table = self.data
        row_value = table.row_values(rows)
        return row_value

    """获取某列内容"""
    def get_col_value(self,col_id=None):
        if col_id !=None:
            col_value = self.data.col_values(col_id)
        else:
            col_value = self.data.col_values(0)
        return col_value


if __name__=="__main__":
    #file_path = r'E:\ERP_interface_Auto\test_file\inference1.xls'
    shili = Excel_method()
    # print(shili.sheet_nrow())
    # value = shili.sheet_cell_value(0,1)
    # print(value)

    #shili.write_result_excel(1,10,'fail')
    num =  shili.get_row_num('add_askbuy')
    print(num)