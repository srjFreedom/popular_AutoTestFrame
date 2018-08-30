#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
该文件为执行入口
"""

__version__='1.4.2'

import unittest
import os, time, sys
import threading
import traceback
import HTMLRunner
from ResaultAndLog import CreateAny, stdVomit, stdEat
from ..sqlLib.sqlConnect import SqlConnect
# import sys

# Python2.7需重加载编码为utf8
# reload(sys)
# sys.setdefaultencoding('utf8')

# 记录日志
# sys.stdout = LoggerEat()
# sys.stderr = LoggerVomit(CreateAny().createLog())



class CreateSuite():
    def __init__(self, caselist, phone_ip, testRunner):
        ''' 创建测试用例集 '''
        timeName = CreateAny()
        filepath = timeName.createDir()
        logpath = timeName.createLog()
        self.filename = filepath + '_result.html'
        self.logname = logpath + '.log'
        self.suite = unittest.TestSuite()
        self.caselist = caselist
        self.phone_ip = phone_ip
        self.testRunner = testRunner
        self.totalRun = len(self.caselist[1])
        self.pro = self.caselist[0][0].split('/')[2]
        self.reportName = self.filename.split('/')[-1]
        self.runner = None


    def _createSuite(self, dirlist, scriptlist):
        ''' 添加用例 '''
        if len(dirlist) == len(scriptlist):
            for i in range(0, len(dirlist)):
                try:
                    # discover方法定义
                    discover = unittest.defaultTestLoader.discover(
                        # 测试用例放置的位置
                        str(dirlist[i]),
                        pattern = str(scriptlist[i]),
                        top_level_dir = str(dirlist[i])
                    )
                    # discover方法筛选出来的用例，循环添加到测试套件中
                    for test_suite in discover:
                        self.suite.addTests(test_suite)
                except Exception:
                    print (traceback.format_exc())
            return self.suite

    def runnerMode(self):
        sys.stderr = stdVomit(self.logname, sys.stderr)
        sys.stdout = stdEat(sys.stderr)
        print ('\n' + '# ' * 10 + u'脚 本 已 开 始 运 行' + ' #' * 10 + '\n')
        # 读取用例存放路径
        try:
            allTestCase = self._createSuite(self.caselist[0], self.caselist[1])
        except Exception, e:
            print (u'\n用例套件报错！报错信息:\n')
            print (e)
        else:
            SqlConnect('sql/webFrame.db').commit_excute("insert into REPORT_AUTO (RPONAME, PROCODE, RUNNER) VALUES ('{0}', '{1}', '{2}')".format(self.reportName, self.pro, self.testRunner))
            self.fp = open(self.filename, 'ab')
            # 定义测试报告
            self.runner = HTMLRunner.HTMLTestRunner(
                stream=self.fp,
                title='自动化测试报告',
                description='用例执行情况：'
            )
            self.isRun = True
            threading.Thread(target=self._threadedGetSchedule).start()
            try:
                self.runner.run(allTestCase)
            except Exception:
                SqlConnect('sql/webFrame.db').commit_excute("update REPORT_AUTO set FINISHED='{0}' where RPONAME='{1}'".format('2', self.reportName))
                print (u'\n运行报错！报错信息:\n')
                print (traceback.format_exc())
            else:
                passrate = self.runner.passrate
                SqlConnect('sql/webFrame.db').commit_excute("update REPORT_AUTO set RPOPATH='{0}', RPOPASSRATE='{1}', FINISHED='{2}' where RPONAME='{3}'".format(self.filename, passrate, '1', self.reportName))
            self.isRun = False
            if self.phone_ip == '':
                pass
            else:
                os.popen('adb disconnect '+self.phone_ip+':5555')
            self.fp.close()
            print (u'\n完成\n')

    def _threadedGetSchedule(self):
        alreadyRun = 0
        backTmp = 0
        while self.isRun:
            time.sleep(2)
            if getattr(self.runner.resultMy, 'testsRun', False):
                backTmp = self.runner.resultMy.testsRun
                if backTmp > alreadyRun:
                    alreadyRun = backTmp
                    schedule = '%.2f' % (float(alreadyRun) / float(self.totalRun) * 100)
                    SqlConnect('sql/webFrame.db').commit_excute("update REPORT_AUTO set SCHEDULE='{0}' where RPONAME='{1}'".format(schedule, self.reportName))