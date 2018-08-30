# -*- coding: utf8 -*-

import multiprocessing
from testCaseRunner import CreateSuite

class AutoTestRunnerForWeb(multiprocessing.Process):
    def __init__(self, scripts_list, testRunner, phone_ip):
        multiprocessing.Process.__init__(self)
        self.scripts_list = scripts_list
        self.phone_ip = phone_ip
        self.testRunner = testRunner

    def run(self):
        dirlist = []
        scriptlist = []
        for dir in self.scripts_list:
            tmplist = dir.split(',')
            dirlist.append(tmplist[0])
            scriptlist.append(tmplist[1])
        caselist = [dirlist, scriptlist]  # dirlist为脚本目录（列表），scriptlist为目录下所匹配的脚本（列表）
        CreateSuite(caselist, self.phone_ip, self.testRunner).runnerMode()