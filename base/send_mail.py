#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
class SendEmail():
    global send_user
    global password
    global email_host

    email_host = 'smtp.qq.com'
    send_user = '530542889@qq.com'
    password = 'dfguhvpvaklccbef'  #邮箱设置->账户->pop3/SMTP开启的授权码
    def send_mail(self,userlist,theme,content):
        user = "我自己的邮箱"+ "<" + send_user +">"
        message = MIMEText(content,_subtype='plain',_charset='UTF-8')
        message['Subject'] = theme
        message['From'] = user
        message['TO'] = ";".join(userlist)
        server = smtplib.SMTP_SSL(email_host,465)
        server.login(send_user,password)
        server.sendmail(user,userlist,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        all_num = pass_num + fail_num
        #%
        if all_num!=0:
            pass_persent = "%.2f%%" %(pass_num/all_num*100)    #显示60%
            fail_persent = "%.2f%%" %(fail_num/all_num*100)
        else:
            print("分母为0，不能做除法运算")

        userlist = ['530542889@qq.com']
        theme = "这是接口自动化测试"
        content = "接口自动化测试报告：总用例个数%s,通过用例%s，通过率%s，失败用例%s，失败率%s" %(all_num,pass_num,pass_persent,fail_num,fail_persent)
        self.send_mail(userlist,theme,content)



if __name__=="__main__":
    shili = SendEmail()
    # userlist = ['530542889@qq.com']
    # theme = "这是接口自动化测试"
    # content = "哈哈哈，接口自动化测试报告哟"
    shili.send_main([1,2,3],[4,5])