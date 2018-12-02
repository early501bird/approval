# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
import os

BASE_DIR = os.path.dirname(__file__)


PORT=8000

settings={
    "debug":True,
    "static_path":os.path.join(BASE_DIR,'static'),
    "template_path":os.path.join(BASE_DIR,'template'),
    "login_url":"/login",
}