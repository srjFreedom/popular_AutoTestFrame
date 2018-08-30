#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import re

class Program_director(object):
    def __init__(self):
        self.m_dl = 0
        self.idNum = 0
        self.HTML = []

    def _directorPath(self, path, level=1):
        '''''
        打印一个目录下的所有文件夹和文件
        '''
        self.idNum += 1
        # 目录下所有文件夹
        dirList = []
        # 目录下所有文件
        fileList = []
        # 返回一个列表，包含目录所有条目
        alls = os.listdir(path)
        dirList.append(str(level))
        for f in alls:
            if (os.path.isdir(path + '/' + f)):
                # 排除隐藏文件夹
                if (f[0] != '.'):
                    # 添加文件夹
                    dirList.append(f)
            if (os.path.isfile(path + '/' + f)) and re.findall('.*py$', f) != [] and re.findall('^__init__.*', f) == []:
                # 添加文件
                fileList.append(f)
        # 空文件加跳过
        if len(dirList) == 1 and len(fileList) == 0:
            self.HTML.append('</ul>')
        # 跳过第一条数据
        i_dl = 0
        for dl in dirList:
            if (i_dl == 0):
                i_dl = i_dl + 1
            else:
                if dl == dirList[len(dirList) - 1] and len(fileList) == 0 and len(dirList) > 1:
                    self.m_dl = 1
                # 打印至控制台，不是第一个的目录
                self.HTML.append('<li><i class="glyphicon glyphicon-folder-open"></i><input type="checkbox"><a href="javascript:showhide(\'' + 'ss' + str(self.idNum) + '\');">' + dl + '</a>')
                self.HTML.append('<ul id="' + 'ss'+ str(self.idNum) + '">')
                # 打印目录下的所有文件夹和文件，目录级别+1
                self._directorPath(path + '/' + dl, (int(dirList[0]) + 1))
        for fl in fileList:
            # 打印文件
            self.HTML.append('<li><i class="glyphicon glyphicon-file"></i><input name="scripts_point" type="checkbox" value=\"' + path + ',' + fl + '\"><span>' + fl + '</span></li>')
            if fl == fileList[len(fileList) - 1]:
                self.HTML.append('</ul>')
            if fl == fileList[len(fileList) - 1] and self.m_dl == 1:
                self.HTML.append('</ul>')
                self.m_dl = 0

    def createDirHtml(self, path):
        self._directorPath(path)
        return ''.join(self.HTML)