# -*- coding: utf8 -*-

import re
import os

class PerformanceCmd(object):
    def __init__(self, driver_ip=None):
        print '\n' + '# ' * 10 + u'性 能 测 试 已 开 始 运 行' + ' #' * 10
        self._connectWifiDriver(driver_ip)
        self._getPackage()
        self._getPid()
        self._getUid()
        self._getMemTotal()

    def _connectWifiDriver(self, driver_ip):
        if driver_ip:
            os.popen('adb connect ' + driver_ip)
        else:
            pass

    def _getPackage(self):
        activityCmd = os.popen('adb shell "dumpsys activity activities | grep mResumedActivity"')
        activityOut = activityCmd.read()
        if activityOut == '':
            activityCmd = os.popen('adb shell "dumpsys activity activities | grep mFocusedActivity"')
            activityOut = activityCmd.read()
        self.package = re.findall('\s(\S+)/', activityOut)[0]
        print u'被测对象包名：' + self.package

    def _getPid(self):
        pidCmd = os.popen('adb shell "ps | grep ' + self.package + '"')
        pidOut = pidCmd.read()
        self.pid = pidOut.split()[1]
        print u'被测对象PID：' + self.pid

    def _getUid(self):
        uidCmd = os.popen('adb shell "cat /proc/' + self.pid + '/status | grep Uid"')
        uidOut = uidCmd.read()
        self.uid = uidOut.split()[1]

    def _getMemTotal(self):
        memTotalCmd = os.popen('adb shell "cat /proc/meminfo | grep MemTotal"')
        memTotalOut = memTotalCmd.read()
        self.memTotal = memTotalOut.split()[1]

    def getTop(self, interval):
        topCmd = os.popen('adb shell "top -n 1 -d ' + interval + ' | grep ' + self.pid + '"')
        out = topCmd.read()
        return out

    def getMeminfo(self):
        memCmd = os.popen('adb shell "dumpsys meminfo '  + self.pid  + ' | grep TOTAL"')
        out = memCmd.read()
        return out

    def getMemLibinfo(self):
        memLibCmd = os.popen('adb shell "cat /proc/'  + self.pid  + '/status | grep Vm"')
        out = memLibCmd.read()
        return out

    def getWlanFlow(self):
        wlanFlowCmd = os.popen('adb shell "cat /proc/net/xt_qtaguid/stats | grep ' + self.uid + ' | grep wlan0"')
        out = wlanFlowCmd.read()
        return out

    def getSurfaceFlinger(self):
        surfaceFlingerCmd = os.popen('adb shell "dumpsys SurfaceFlinger --latency SurfaceView"')
        out = surfaceFlingerCmd.read()
        os.popen('adb shell "dumpsys SurfaceFlinger --latency-clear"')
        return out

    def getBattery(self):
        batteryCmd = os.popen('adb shell "dumpsys battery"')
        out = batteryCmd.read()
        return out

    def getBrand(self):
        brandCmd = os.popen('adb shell getprop ro.product.brand')
        out = brandCmd.read()
        return out

    def getModel(self):
        modelCmd = os.popen('adb shell getprop ro.product.model')
        out = modelCmd.read()
        return out

    def getRelease(self):
        releaseCmd = os.popen('adb shell getprop ro.build.version.release')
        out = releaseCmd.read()
        return out

    def getSdk(self):
        sdkCmd = os.popen('adb shell getprop ro.build.version.sdk')
        out = sdkCmd.read()
        return out
