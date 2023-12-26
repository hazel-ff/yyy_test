# 时间：2022/10/15 14:09
import json

import requests

from log.logger import logger
from task.const import binstd_url

server_url = binstd_url
log = logger()
"""
get请求
"""
def cont_query_get(params):
    result = requests.get(
        url = f"{server_url}/shouji/query",
        data=params
    )
    res = json.loads(result.text)
    log.info(f"请求接口返回{res}")
    return res

"""
post请求
"""
def shouji_query_post(params):
    result = requests.post(
        url = 'https://jsonplaceholder.typicode.com/posts',
        data=params
    )
    log.info(f"{result}")
    return result

