# 时间：2023/12/25 16:35

"""
用于解决使用@pytest.mark.parametrize() ids为中文，中文标题被使用unicode编码的情况
"""
from typing import List
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')