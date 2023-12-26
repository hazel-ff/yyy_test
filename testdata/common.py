# 时间：2023/12/23 14:33

"""
读取yaml文件
"""
import os.path
import yaml
from log.logger import logger

log = logger()

def get_yaml(yaml_file,key_name):
    current_work_dir = os.path.abspath(os.path.dirname(__file__))   #获取当前文件夹绝对路径
    print(current_work_dir)
    path = f"{current_work_dir}/{yaml_file}"    #获取要读取的yaml文件的最终路径
    with open(path,'r',encoding='utf-8') as f:
        des_file = yaml.safe_load(stream=f)  #yaml.safe_load()用于安全解析yaml文件
        log.info(f"yaml文件内容为：{des_file}")
        res = des_file[key_name]
        log.info(f"测试数据为：{res}")
        return res
        # data = list(des_file.values())   #将yaml文件所有数据转为字典格式
        # return data



if __name__ == '__main__':
    result = get_yaml("testdata.yml", 'test_data')