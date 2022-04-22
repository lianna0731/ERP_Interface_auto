#coding:utf-8
import logging
from base import get_project_path
class MyLog:
    def My_log(self,msg,level):
        # #默认打印控制台，收集warning以上级别
        # #以下级别按低到高
        # logging.debug("1")
        # logging.info("2")
        # logging.warning("3")
        # logging.error("4")
        # logging.critical("5")
        """
        1.收集日志 logger：级别
        2.输出渠道 handler :指定文件还是控制台，默认控制台
        """
        #定义日志收集器
        my_logger = logging.getLogger("python")
        my_logger.setLevel("DEBUG")

        #定义日志输出格式,用在渠道
        my_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s -日志信息：%(message)s')

        #定义自己的渠道
        #默认控制台
        my_handler = logging.StreamHandler()
        my_handler.setLevel("INFO")
        my_handler.setFormatter(my_format)
        #文件
        my_filehandle = logging.FileHandler(get_project_path.logfile_path,encoding="utf8")
        my_filehandle.setLevel("INFO")
        my_filehandle.setFormatter(my_format)

        #收集器和渠道关联
        my_logger.addHandler(my_handler)
        my_logger.addHandler(my_filehandle)

        #收集日志
        if level =="DEBUG":
            my_logger.debug(msg)
        elif level =="INFO":
            my_logger.info(msg)
        elif level =="WARNING":
            my_logger.warning(msg)
        elif level =="ERROR":
            my_logger.error(msg)
        elif level =="CRITICAL":
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(my_handler)
        my_logger.removeHandler(my_filehandle)

    def debug(self,msg):
        MyLog().My_log(msg,"DEBUG")

    def info(self,msg):
        MyLog().My_log(msg,"INFO")

    def warning(self,msg):
        MyLog().My_log(msg,"WARNING")

    def error(self,msg):
        MyLog().My_log(msg,"ERROR")

    def ctitical(self, msg):
        MyLog().My_log(msg, "CRITICAL")

if __name__ == "__main__":
    MyLog().My_log("提示好好地", "WARNING")
    #MyLog().My_log("报错好好的","ERROR")