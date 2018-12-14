# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler


class AuthBaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")
