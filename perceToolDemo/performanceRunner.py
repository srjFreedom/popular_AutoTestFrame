# -*- coding: utf8 -*-
'''
以下两方法为事务开始点与结束点，用法：

    from performanceRunner import performanceRunner

    a = performanceRunner
    a.affStart(affName)
    ......
    ...... This's Your Scripts
    ......
    a.affStop()

    # Successful Build The Report
'''
import threading
from performance.performanceReport import PerformanceReport

class performanceRunner():
    def affStart(self,affName, driver_ip=None):
        '''
        此方法定义事务开始点并创建报告
        affName: 定义的事务名，也是结束后输出结果的文件名
        '''
        self.p = PerformanceReport(driver_ip)
        self.p.justDoIt = True
        a = threading.Thread(target=self.p.run, args=(affName, driver_ip))
        a.start()

    def affStop(self):
        '''
        此方法结束当前事务的性能测试并输出性能数据到报告
        '''
        self.p.justDoIt = False