# 时间：2022/10/15 10:22
import logging

from single.s_task.query import shouji_query_get, shouji_query_post


def test_shouji_query_get():
    param = {
        "shouji":"18751887516",
        "appkey":"0c818521d38759e1"
    }
    actual = shouji_query_get(param)
    assert actual.status_code==200
    logging.info(f"接口访问成功")


def test_shouji_query_post():
    param = {
        "shouji":"15075546853",
        "appkey":"0c818521d38759e2"
    }
    actual = shouji_query_post(param)
    assert actual.status_code==201
    print('接口访问成功',actual.json())




