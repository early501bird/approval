# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-
import os
from tornado.web import Application
from config import settings
from views.index import *


class Application(Application):
    def __init__(self):
        handlers=(
            (r'/home',HomeHandler),
        )
        super(Application,self).__init__(handlers,**settings)