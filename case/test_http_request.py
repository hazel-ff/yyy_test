# 时间：2022/10/15 10:22

import pytest

from log.logger import logger
from testdata.common import get_yaml
from task.query import cont_query_get


log = logger()
# @allure.feature("测试")
# @allure.title("访问用户信息")
# def test_shouji_query_get():
#     param = {
#         "shouji":"18751887516",
#         "appkey":"0c818521d38759e1"
#     }
#     actual = cont_query_get(param)
#     assert actual.status_code==200
#     logging.info(f"接口访问成功")

@pytest.mark.parametrize('param', get_yaml("testdata.yml",'test_data'), indirect=False,
                         ids=['手机号1','手机号2','手机号3'])
def test_query_shouji(param):
    # log.info(f"{param}")
    actual = cont_query_get(param)
    assert actual['status'] == '101'
    log.info(f"接口调用成功，但参数有误：APPKEY为空")




