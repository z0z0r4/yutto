from __future__ import annotations

import hashlib
import urllib.parse

APPKEY = "4409e2ce8ffd12b8"
APPSEC = "59b43e04ad6965f34319062b478f83dd"


def appsign(params: dict[str, str], appkey: str = APPKEY, appsec: str = APPSEC) -> dict[str, str]:
    params.update({"appkey": appkey})
    params = dict(sorted(params.items()))  # 按照 key 重排参数
    query = urllib.parse.urlencode(params)  # 序列化参数
    sign = hashlib.md5((query + appsec).encode()).hexdigest()  # 计算 api 签名
    params.update({"sign": sign})
    return params
