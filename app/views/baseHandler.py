# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler
from pycket.session import SessionMixin

class AuthBaseHandler(RequestHandler,SessionMixin):
    def get_current_user(self):
        return self.session.get('user_info',None)
