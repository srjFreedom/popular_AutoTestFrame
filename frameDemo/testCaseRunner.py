#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
该文件为执行入口
"""

__version__='1.4.2'


import unittest
import sys
import ConfigParser
import traceback
import HTMLRunner
from ResaultAndLog import CreateAny, LoggerEat, LoggerVomit
# Python2.7需重加载编码为utf8
reload(sys)
sys.setdefaultencoding('utf8')

# 记录日志
sys.stderr = LoggerVomit(CreateAny().createLog())
sys.stdout = LoggerEat()


class CreateSuite():
    def __init__(self):
        ''' 创建测试用例集 '''
        self.suite = unittest.TestSuite()

    def createSuite(self, csp, csr):
        ''' 添加用例 '''
        cslist = csp.strip('(').strip(')').strip('\n').replace(' ', '').replace('"', '').split(',')
        for i in range(0, len(cslist)):
            try:
                # discover方法定义
                discover = unittest.defaultTestLoader.discover(
                    # 测试用例放置的位置
                    cslist[i],
                    pattern = csr,
                    top_level_dir=cslist[i]
                )
                # discover方法筛选出来的用例，循环添加到测试套件中
                for test_suite in discover:
                    self.suite.addTests(test_suite)
            except Exception:
                traceback.print_exc()
        return self.suite


if __name__ == "__main__":
    print '\n' + '# ' * 10 + u'脚 本 已 开 始 运 行'.encode('gb18030') + ' #' * 10 + '\n'
    # 设置执行路径当前目录
    # BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    # os.chdir(BASE_DIR)
    # 读取用例存放路径
    cf = ConfigParser.ConfigParser()
    cf.read("PathFile.txt")
    allTestCase = CreateSuite().createSuite(cf.get('CasePath', 'cspath'), cf.get('CaseRule', 'csrule'))
    path = CreateAny().createDir()
    filename = path + '_result.html'
    fp = open(filename, 'ab')
    # 定义测试报告
    runner = HTMLRunner.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='用例执行情况：'
    )
    # 执行测试
    try:
        runner.run(allTestCase)
    except Exception:
        fp.close()
        print (u'\n运行报错！报错信息:\n'.encode('gb18030'))
        raw_input(traceback.format_exc())
    fp.close()
    raw_input(u'\n完成\n'.encode('gb18030'))