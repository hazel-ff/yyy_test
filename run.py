# 时间：2023/2/12 13:29
import pytest

"""
用例里面 print/logging 输出都打印， -s 参数
用例遇见失败就停止执行， -x 参数
用例执行详情展示，-v 参数
安静模式, 不输出环境信息， -q
"""
if __name__ == '__main__':
    # pytest.main(['-s','-v','case','-q','--alluredir','allure_report'])
    pytest.main(['-s', '-v', '-m allureproject','./case'])