# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
import hashlib
from orm.users import users

def hash(text):
    text=hashlib.md5(text.encode()).hexdigest()
    return text


def authenticate(username,password):
    if username and password:
        hash_pwd=hash(password)
        if username==username and password==password:
            return True

    return False