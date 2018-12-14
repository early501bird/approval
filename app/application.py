# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
import os
from tornado.web import Application,StaticFileHandler
from config import *
from views.index import *
from views.auth import *

class Application(Application):
    def __init__(self):
        handlers=(
            (r'/',IndexHandler),
            (r'/login', LoginHandler),
            (r'/logout', LogoutHandler),
            (r'/regist', RegistHandler),

        )
        super(Application,self).__init__(handlers,**settings)