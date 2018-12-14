# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import json
import os
from config import BASE_DIR
import hashlib

class Users(object):
    def __init__(self):
        self._userpath = os.path.join(BASE_DIR,"orm/data/user.json")
        self._users = {}
        try:
            with open(self._userpath,"r",encoding="utf-8") as f:
                self._users = json.load(f)
        except IOError as ex:
            print(ex)


    def __str__(self):
        return json.dumps(self._users,ensure_ascii=False)


    def _hash(self,text):
        text = hashlib.md5(text.encode()).hexdigest()
        return text

    def _updateUserFile(self):
        try:
            with open(self._userpath,"w",encoding="utf-8") as f:
                json.dump(self._users,f,ensure_ascii=False)
                return True
        except Exception as e:
            print(e)
            return False

    def existUser(self,username):
        return self._users.__contains__(username)


    def addUser(self,username,passwd):
        if self._users.__contains__(username):
            raise Exception("error :user exist")
        self._users[username]=dict(username=username,password=self._hash(passwd))
        return self._updateUserFile()

    def removeUser(self,username):
        if not self._users.__contains__(username):
            raise Exception("error: user not exist ")
        del self._users[username]
        return self._updateUserFile()

    def authenticate(self,username,password):
        if not username or  not password: return False
        if not self._users.__contains__(username): return False
        return self._users[username]["password"]==self._hash(password)



users = Users()


if __name__ == '__main__':
    print(users)
    try:
        users.addUser("abc","abcadmin")
    except Exception as e:
        print(e)
    finally:
        print(users)
    try:
        users.addUser("李伟", "liweiadmin")
    except Exception as e:
        print(e)
    finally:
        print(users)
    try:
        users.removeUser("abc")
    except Exception as e:
        print(e)
    finally:
        print(users)