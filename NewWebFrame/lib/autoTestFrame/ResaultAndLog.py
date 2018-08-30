# -*- coding: utf8 -*-

import os, time

class CreateAny():
    def __init__(self):
        originalTime = time.time()
        nowSec = time.strftime('%Y%m%d%H%M%S', time.localtime(originalTime))
        nowMsec = str('%03d' % ((originalTime - long(originalTime)) * 1000))
        self.now = nowSec + nowMsec

    def createDir(self):
        ''' 定义报告存放路径 '''
        path = 'templates/index/autoTest/reportResource/'
        # 判断目录是否存在，没有则创建
        if not os.path.exists(path):
            os.makedirs(path)
        reportPath = path + self.now
        return  reportPath

    def createLog(self):
        '''定义log输出'''
        path = 'templates/index/autoTest/reportLog/'
        # 判断目录是否存在，没有则创建
        if not os.path.exists(path):
            os.makedirs(path)
        logPath = path + self.now
        return  logPath


class stdEat():
    def __init__(self, fp):
        self.terminalerr = fp

    def write(self, message):
        self.terminalerr.write(message)

class stdVomit():
    def __init__(self, fileN, fp):
        self.terminal = fp
        self.log = open(fileN, 'a', 0)

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass