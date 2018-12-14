# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
import os

BASE_DIR = os.path.dirname(__file__)


PORT=8000

# settings={
#     "debug":True,
#     "static_path":os.path.join(BASE_DIR,'static'),
#     "template_path":os.path.join(BASE_DIR,'templates'),
#     "login_url":'/login', #没有登录则跳转至此
#
# }

settings=dict(
    debug=True,
    template_path=os.path.join(BASE_DIR,'templates'),
    static_path=os.path.join(BASE_DIR,'static'),
    login_url='/login',
    cookie_secret='1q2w3e4r',  # 加密cookie的字符串
    # pycket={  #固定写法packet，用于保存用户登录信息
    #     'engine': 'redis',
    #     'storage': {
    #         'host': 'localhost',
    #         'port': 6379,
    #         'db_sessions': 5,
    #         'db_notifications': 11,
    #         'max_connections': 2 ** 33,
    #     },
    #     'cookie': {
    #         'expires_days': 38,
    #         'max_age': 100
    #     }
    # }

)