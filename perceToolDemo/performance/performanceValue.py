# -*- coding: utf8 -*-

import re
import math
import time
import threading
from performanceCmd import PerformanceCmd

class PerformanceValue(object):
    def __init__(self, driver_ip=None):
        self._performanceCmd = PerformanceCmd(driver_ip)
        self._initFlow()
        # self._initMemLibProportion()
        self._initBattery()

    def _initFlow(self):
        flowOut = self._performanceCmd.getWlanFlow()
        rx_bytes = 0
        tx_bytes = 0
        tmp = flowOut.split('\n')
        for i in tmp:
            if i == '':
                break
            bytes_list = i.split()
            rx_bytes += int(bytes_list[5])
            tx_bytes += int(bytes_list[7])
        self.rx_bytes = rx_bytes
        self.tx_bytes = tx_bytes

    def _initMemLibProportion(self):
        pssMemOut = self._performanceCmd.getMeminfo()
        memLibOut = self._performanceCmd.getMemLibinfo()
        tmp = pssMemOut.split()
        pssMem = float(tmp[1])
        tmp = memLibOut.split()
        rssMem = float(tmp[16])
        self.memLib = float(tmp[28])
        self.proportion = (self.memLib + pssMem - rssMem) / self.memLib
        print self.proportion

    def _batteryinfo(self):
        batteryOut = self._performanceCmd.getBattery()
        self.dicTmp = {}
        countTmp = batteryOut.split('\n')
        loopTmp = False
        for i, j in enumerate(countTmp):
            if j.find('Current Battery Service') != -1:
                loopTmp = True
                continue
            if loopTmp:
                listTmp = j.replace(' ', '').replace('\r', '').split(':')
                self.dicTmp[listTmp[0]] = listTmp[1]
                if i == len(countTmp) - 2:
                    break

    def _initBattery(self):
        self._batteryinfo()
        self.level = self.dicTmp['level']

    def allNeed(self):
        self.surfaceOut = self._performanceCmd.getSurfaceFlinger()
        self.flowOut = self._performanceCmd.getWlanFlow()
        self.batteryOut = self._performanceCmd.getBattery()
        self.memLibOut = self._performanceCmd.getMemLibinfo()

    def cpuNeed(self, interval):
        self.topOut = self._performanceCmd.getTop(interval)

    def memeryValue(self):
        tmp = self.memLibOut.split()
        rssMemeryK = float(tmp[16])
        memLib = float(tmp[28])
        # MemeryM = '%.2f' % ((rssMemeryK - (memLib - memLib * self.proportion)) / 1024)
        MemeryM = '%.2f' % ((rssMemeryK - memLib) / 1024)
        return float(MemeryM)

    def memeryRatio(self):
        tmp = self.memLibOut.split()
        rssMemeryK = float(tmp[16])
        memLib = float(tmp[28])
        # MemeryPercent = '%.2f%%' % \
        #                     ((((rssMemeryK - (memLib - memLib * self.proportion)) / 1024) / (float(self._performanceCmd.memTotal) / 1024)) * 100)
        MemeryPercent = '%.2f%%' % \
                            ((((rssMemeryK - memLib) / 1024) / (float(self._performanceCmd.memTotal) / 1024)) * 100)
        MemeryPercent = re.findall(r'(\S+)%', MemeryPercent)[0]
        return float(MemeryPercent)

    def cpuRatio(self):
        tmp = self.topOut.split()
        cpuPercent = tmp[2]
        cpuPercent = re.findall(r'(\S+)%', cpuPercent)[0]
        return int(cpuPercent)

    def rxFlowConsumption(self):
        rx_bytes_tmp = 0
        tmp = self.flowOut.split('\n')
        for i in tmp:
            if i == '':
                break
            rx_bytes_list = i.split()
            try:
                rx_bytes_tmp += int(rx_bytes_list[5])
            except Exception, e:
                print 'rx_bytes_list[5] is: ' + rx_bytes_list[5]
                print e
        rx_KiloBytes = '%.2f' % ((float(rx_bytes_tmp) - float(self.rx_bytes)) / 1024)
        return float(rx_KiloBytes)

    def txFlowConsumption(self):
        tx_bytes_tmp = 0
        tmp = self.flowOut.split('\n')
        for i in tmp:
            if i == '':
                break
            tx_bytes_list = i.split()
            try:
                tx_bytes_tmp += int(tx_bytes_list[7])
            except Exception, e:
                print 'tx_bytes_list[7] is: ' + tx_bytes_list[7]
                print e
        tx_KiloBytes = '%.2f' % ((float(tx_bytes_tmp) - float(self.tx_bytes)) / 1024)
        return float(tx_KiloBytes)

    def frameRateNew(self):
        counTmp = self.surfaceOut.split('\n')
        syncTmp = []
        jankTmp = []
        jankTmp_1 = []
        jankTmp_2 = []
        jankCount = 0
        haveValueCount = 0
        refresh_period = ''
        for i, j in enumerate(counTmp):
            if i == 0:
                refresh_period = float(j)
                continue
            tmp = j.split()
            try:
                syncTmp.append(tmp[1])
                jankTmp_1.append(tmp[0])
                jankTmp_2.append(tmp[2])
            except Exception:
                continue
        syncTmp.pop(0)
        syncTmp.pop()
        jankTmp_1.pop(0)
        jankTmp_1.pop()
        jankTmp_2.pop(0)
        jankTmp_2.pop()
        alllen = len(syncTmp)
        for i, j in enumerate(syncTmp):
            if j == '0':
                continue
            else:
                haveValueCount = i
                break
        timeShip = int(syncTmp[alllen - 1]) - int(syncTmp[haveValueCount])
        if timeShip == 0:
            fps = 1.0
        else:
            fpsNojank = (alllen - haveValueCount - 1) / (timeShip / 1000000000.0)
            jankTmp_1 = jankTmp_1[(-alllen + haveValueCount):]
            jankTmp_2 = jankTmp_2[(-alllen + haveValueCount):]
            janklen = len(jankTmp_1)
            for i in range(janklen):
                jankTmp.append(math.ceil((float(jankTmp_2[i]) - float(jankTmp_1[i])) / refresh_period))
                if i > 0:
                    if jankTmp[i] > jankTmp[i - 1]:
                        jankCount += 1
            fps = '%.2f' % (fpsNojank - jankCount)
            # fps = '%.2f' % fpsNojank
        return float(fps)

    def batteryLevel(self):
        self._batteryinfo()
        level = int(self.level) - int(self.dicTmp['level'])
        return level

    def batteryVoltage(self):
        self._batteryinfo()
        voltage = self.dicTmp['voltage']
        return int(voltage)

    def batteryTemperature(self):
        self._batteryinfo()
        temperature = self.dicTmp['temperature']
        return float(temperature) / 10

if __name__ == '__main__':
    a = PerformanceValue()
    while 1:
        a.cpuAndMemNeed('1')
        print a.memeryValue()