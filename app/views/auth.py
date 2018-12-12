# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import  tornado.web
from .baseHandler import AuthBaseHandler
from utils.account import authenticate

class LoginHandler(AuthBaseHandler):


    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        passwd = self.get_argument('passwd')

        passed = authenticate(username,passwd)
        self.write('user:{0},pd:{1}'.format(username,passwd))