# -*- coding: utf8 -*-

from ..sqlConnect import SqlConnect

class GetReportDir(object):
    def __init__(self):
        pass

    def getRpoCount(self):
        sqlRpoCount = SqlConnect('sql/webFrame.db').excute("select count(RPONAME) from REPORT_AUTO")
        return sqlRpoCount

    def getReport(self, pageCount):
        sqlRpo = SqlConnect('sql/webFrame.db').excute("select RPONAME, RPOPASSRATE, RUNNER, FINISHED, SCHEDULE, PROCODE from REPORT_AUTO order by rowid desc limit 10 offset 0+({0}-1)*10".format(pageCount))
        return sqlRpo

    def getSrcRpoCount(self, procode, rponame, testrunner):
        if procode:
            procode = " and PROCODE='{0}' ".format(procode)
        if rponame:
            rponame = " and RPONAME like '%{0}%' ".format(rponame)
        if testrunner:
            testrunner = " and RUNNER='{0}' ".format(testrunner)
        sql = "select count(RPONAME) from REPORT_AUTO WHERE 1=1 {0} {1} {2}".format(procode, rponame, testrunner)
        sqlSrcRpoCount = SqlConnect('sql/webFrame.db').excute(sql)
        return sqlSrcRpoCount


    def getSrcReport(self, procode, pageCount, rponame, testrunner):
        if procode:
            procode = " and PROCODE='{0}' ".format(procode)
        if rponame:
            rponame = " and RPONAME like '%{0}%' ".format(rponame)
        if testrunner:
            testrunner = " and RUNNER='{0}' ".format(testrunner)
        sql = "select RPONAME, RPOPASSRATE, RUNNER, FINISHED, SCHEDULE, PROCODE from REPORT_AUTO where 1=1 {0} {2} {3} order by rowid desc limit 10 offset 0+({1}-1)*10".format(procode, pageCount, rponame, testrunner)
        sqlSrcRpo = SqlConnect('sql/webFrame.db').excute(sql)
        return sqlSrcRpo