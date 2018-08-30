# -*- coding: utf-8 -*-

import sys, os
import time
import logging
import inspect
from logging.handlers import TimedRotatingFileHandler

tmpList = []

def createLog():
    '''定义log输出'''
    path = './Log'
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
    return logName

class Logger_ready():
    def __init__(self):
        self.terminallogger = sys.stderr
    def info(self, message):
        self.terminalerr.write(message)

class LoggerEat():
    def __init__(self):
        self.terminalerr = sys.stderr
    def write(self, message):
        self.terminalerr.write(message)
    def flush(self):
        pass

class LoggerVomit():
    def __init__(self):
        self.log = loggerinit().log
        self.tem = sys.stderr
    def write(self, message):
        try:
            module = inspect.stack()[2][1].split('\\')[-1].replace('.py', '')
            lineno = sys._getframe().f_back.f_lineno
        except Exception:
            module = None
            lineno = None
        if message[-1] != '\n':
            tmpList.append(message)
            return
        if message[-1] == '\n' and message != '\n':
            if message[0] == '\n':
                msg = ''.join(tmpList) + message[1:-1]
            else:
                msg = ''.join(tmpList)+message[0:-1]
        else:
            msg = ''.join(tmpList)
        head = '{0}[{1}]'.format(module, str(lineno))
        lenHead = 24-len(head.encode('GBK'))+len(head)
        self.log.info('{head:<{lenHead}} -- {msg}'.format(head=head, msg=msg, lenHead=lenHead))
        # self.tem.write('{head:<{lenHead}} -- {msg}\n'.format(head=head, msg=msg, lenHead=lenHead))
        del tmpList[:]
    def flush(self):
        pass

class loggerinit():
    def __init__(self):
        self.log = logging.getLogger('webFrame')
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        # file_handler = logging.FileHandler("test.log", mode='a')
        file_handler = TimedRotatingFileHandler(filename='log/webFrame', when="D", interval=1, backupCount=7)
        file_handler.suffix='_%Y-%m-%d.log'
        file_handler.setFormatter(formatter)
        self.log.addHandler(console_handler)
        self.log.addHandler(file_handler)
        self.log.setLevel(logging.DEBUG)