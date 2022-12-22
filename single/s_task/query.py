# 时间：2022/10/15 14:09
import requests
from single.const import binstd_url

server_url = binstd_url

"""
get请求
"""
def shouji_query_get(params):
    result = requests.get(
        url = f"{server_url}/shouji/query",
        data=params
    )
    return result

"""
post请求
"""
def shouji_query_post(params):
    result = requests.post(
        url = 'https://jsonplaceholder.typicode.com/posts',
        data=params
    )
    return result

