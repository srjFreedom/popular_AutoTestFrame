# -*- coding: utf8 -*-
import time
from performanceRunner import *

class TestRunner():

    def __init__(self):
        self.p = performanceRunner()
        self.state = False

    def testrun(self):
        print u"------------------开始------------------"
        while True:
            value = raw_input(unicode('请输入命令：','utf-8').encode('gbk'))
            if value == "start":
                if self.state == False:
                    reporttime = time.strftime("%Y-%m-%d-%H-%M-%S")
                    self.p.affStart(reporttime)
                    self.state = True
                    print u"打点开始\n"
                else:
                    print u"性能收集框架正在运行中，请先停止数据收集！"
            elif value == "stop":
                if self.state == False:
                    print u"还未开始打点，请先打点开始收集数据！"
                else:
                    self.p.affStop()
                    self.state = False
                    time.sleep(1)
                    print u"打点结束\n"
            elif value == "exit":
                if self.state == True:
                    self.p.affStop()
                break
            else:
                print u"输入的指令有误，请检查指令内容！"

if __name__ == '__main__':
    obj = TestRunner()
    obj.testrun()

