##coding:utf-8

"""读取配置文件，配置文件配置执行模块的哪几个用例"""
import configparser

class ReadConfig:
    @staticmethod
    def get_config(filepath,section,option):
        cof = configparser.ConfigParser()
        cof.read(filepath,encoding="utf-8")
        return cof[section][option]

if __name__ == "__main__":
    from base import get_project_path
    config_data = eval(ReadConfig.get_config(get_project_path.config_path,"BaseStock","basestock"))['quantity']
    stockCode = eval(ReadConfig.get_config(get_project_path.config_path, "BaseStock", "basestock"))['stockcode']
    quantity = eval(ReadConfig.get_config(get_project_path.config_path, "BaseStock", "basestock"))['quantity']
    print(type(quantity))