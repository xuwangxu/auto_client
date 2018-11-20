#-*- coding:utf-8 -*-
# author: Wang Xu


import hashlib
from config import settings

def gen_sign(ctime):
    """
    生成URL签名
    :param ctime:
    :return:
    """
    key = settings.URL_AUTH_KEY

    val = '%s|%s' %(key,ctime,)

    obj = hashlib.md5()
    obj.update(val.encode('utf-8'))
    return  obj.hexdigest()