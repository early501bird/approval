# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import os
import tornado.web
from tornado.web import RequestHandler
from .baseHandler import AuthBaseHandler

class IndexHandler(AuthBaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("index.html",username=self.current_user)
