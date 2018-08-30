# -*- coding: utf-8 -*-

import sqlite3


def sqlClose(func):
    def decorator(self, *args, **kwargs):
        r = func(self, *args, **kwargs)
        self.con.close()
        return r
    return decorator

def sqlCommit(func):
    def decorator(self, *args, **kwargs):
        r = func(self, *args, **kwargs)
        self.con.commit()
        self.con.close()
        return r
    return decorator

class SqlConnect(object):
    def __init__(self, db):
        self.con = sqlite3.connect(db)

    @sqlClose
    def excute(self, sql):
        cur = self.con.execute(sql)
        return cur.fetchall()

    @sqlCommit
    def commit_excute(self, sql):
        self.con.execute(sql)