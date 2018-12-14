# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

from .baseHandler import AuthBaseHandler
from orm.users import users
import tornado.web

class LoginHandler(AuthBaseHandler):
    def get(self, *args, **kwargs):
        pnext = self.get_query_argument("next", "/")
        print("pNext:", pnext)
        self.set_cookie("next",pnext)
        self.render("login.html")

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        passwd = self.get_argument('passwd')
        if users.authenticate(username, passwd):
            self.set_secure_cookie("username", self.get_argument("username"))
            print("auth success")
        pnext = self.get_cookie("next")
        print("pNext:",pnext)
        self.redirect(pnext)


class LogoutHandler(AuthBaseHandler):
    def post(self, *args, **kwargs):
        self.clear_cookie("username")
        self.redirect("/")


class RegistHandler(AuthBaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("regist.html")

    def post(self, *args, **kwargs):
        name = self.get_argument("username")
        pw = self.get_argument("passwd")
        rpw = self.get_argument("repasswd")
        try:
            if name and pw == rpw and not users.existUser(name):
                res = users.addUser(name, pw)
                self.write("add user " + str(res))
        except Exception as e:
            self.write(e)
        finally:
            self.redirect("/")
