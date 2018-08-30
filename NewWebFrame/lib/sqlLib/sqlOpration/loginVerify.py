# -*- coding: utf-8 -*-

from ..sqlConnect import SqlConnect

class LoginVerify(object):
    def __init__(self):
        pass

    def isUser(self, username, password):
        sqlUsername = SqlConnect('sql/webFrame.db').excute("select USERNAME from USER where USERNAME='" + username + "'")
        sqlPassword = SqlConnect('sql/webFrame.db').excute("select PASSWORD from USER where PASSWORD='" + password + "'")
        if sqlUsername and sqlPassword:
            return True
        else:
            return False
