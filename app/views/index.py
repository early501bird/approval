# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler
import os


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('this is home test')
        # self.render("static_url")
