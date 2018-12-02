# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from tornado import ioloop
from config import PORT
from application import Application



if __name__ == '__main__':
    app = Application()
    app.listen(PORT)
    ioloop.IOLoop.current().start()