# -*- coding: utf8 -*-

import os, time, sys

class CreateAny():
    def __init__(self):
        pass

    def createDir(self):
        ''' 定义报告存放路径 '''
        path = 'D:/AutoTestReport/Program/HTMLResault/'
        # 判断目录是否存在，没有则创建
        if not os.path.exists(path):
            os.makedirs(path)
        # 当前时间来定义文件名
        originalTime = time.time()
        nowSec = time.strftime('%Y%m%d%H%M%S', time.localtime(originalTime))
        nowMsec = str('%03d' % ((originalTime - long(originalTime)) * 1000))
        now = nowSec + nowMsec
        reportPath = path + now
        return  reportPath

    def createLog(self):
        '''定义log输出'''
        path = 'D:/AutoTestReport/Program/Log/'
        # 判断目录是否存在，没有则创建
        if not os.path.exists(path):
            os.makedirs(path)
        # 当前时间定义文件名
        originalTime = time.time()
        nowSec = time.strftime('%Y%m%d%H%M%S', time.localtime(originalTime))
        nowMsec = str('%03d' % ((originalTime - long(originalTime)) * 1000))
        now = nowSec + nowMsec
        logPath = path + now
        logName = logPath + '.log'
        return  logName


class LoggerEat():
    def __init__(self):
        self.terminalerr = sys.stderr

    def write(self, message):
        self.terminalerr.write(message)

    def flush(self):
        pass

class LoggerVomit():
    def __init__(self, fileN):
        self.terminal = sys.stderr
        self.log = open(fileN, 'a', 0)

    def write(self, message):
        self.terminal.write(message)
        # self.log.write(time.strftime('%Y-%m-%d_%H:%M:%S') + ' -- ' + message)
        # self.log.write(message == '\n' and message or time.strftime('%Y-%m-%d_%H:%M:%S') + ' -- ' + message)
        self.log.write(message.replace('\n', '\n' + time.strftime("%Y-%m-%d_%H:%M:%S") + ' -- '))
    def flush(self):
        pass