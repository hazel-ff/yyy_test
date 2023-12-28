# 时间：2022/10/15 10:22
import allure
import pytest

from log.logger import logger
from testdata.common import get_yaml
from task.query import cont_query_get


log = logger()

@pytest.mark.test
@allure.suite("查询接口")
@allure.title("手机号查询")
@pytest.mark.parametrize('param', get_yaml("testdata.yml",'test_data'), indirect=False,
                         ids=['手机号1','手机号2','手机号3'])
def test_query_shouji(param):
    # log.info(f"{param}")
    actual = cont_query_get(param)
    assert actual['status'] == '101'
    log.info(f"接口调用成功，但参数有误：APPKEY为空")


@pytest.mark.allureproject
@allure.suite("校验接口")
@allure.title("号码校验")
@pytest.mark.parametrize('param', get_yaml("testdata.yml",'test_data'), indirect=False,
                         ids=['号码1','号码2','号码3'])
def test_query_number(param):
    # log.info(f"{param}")
    actual = cont_query_get(param)
    assert actual['status'] == '101'
    log.info(f"接口调用成功，但参数有误：APPKEY为空")



