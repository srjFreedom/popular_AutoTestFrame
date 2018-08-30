# -*- coding: utf-8 -*-

from ..sqlConnect import SqlConnect

class GetUser(object):
    def __init__(self):
        pass

    def getAllUser(self):
        sqlAllUser = SqlConnect('sql/webFrame.db').excute("select USERNAME, REALNAME from USER order by rowid asc")
        return sqlAllUser

    def getCurrentUser(self, username):
        sqlCurrentUser = SqlConnect('sql/webFrame.db').excute("select REALNAME from USER where USERNAME='"+username+"'")
        return sqlCurrentUser