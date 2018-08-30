# -*- coding: utf-8 -*-

from ..sqlConnect import SqlConnect

class GetProjectDir(object):
    def __init__(self):
        pass

    def getProCount(self):
        sqlCount = SqlConnect('sql/webFrame.db').excute("select count(PROCODE) from PROJECT")
        return sqlCount

    def getProject(self, pageCount):
        sqlPro = SqlConnect('sql/webFrame.db').excute("select PROCODE,PRONAME from PROJECT where rowid >= "+str((pageCount-1)*10+1)+" and rowid <= "+str(pageCount*10))
        return sqlPro

    def getProList(self):
        sqlProList = SqlConnect('sql/webFrame.db').excute("select PROCODE from PROJECT")
        return sqlProList


if __name__ == '__main__':
    print type(GetProjectDir().getProCount())