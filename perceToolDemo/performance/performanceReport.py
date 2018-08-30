# -*- coding: utf8 -*-

import time
import os,sys
import traceback
import threading
import plotly.plotly
import plotly.graph_objs as go
from plotly.graph_objs import *
from performanceValue import PerformanceValue
from plotly import tools
import xlrd,xlwt
from xlutils.copy import copy

class PerformanceReport(object):
    def __init__(self, driver_ip=None):
        self._value = PerformanceValue(driver_ip)
        self.x = []
        self.y1, self.y2, self.y3, self.y4, self.y5, self.y6, self.y7, self.y8, self.y9 = \
        [], [], [], [], [], [], [], [], []
        self.justDoIt = True

    def _runCpuAndMem(self):
        while self.justDoIt:
            try:
                startTime = time.time()
                self._value.cpuNeed('1')
                self.y1.append(self._value.cpuRatio())
                len_y = len(self.y1)
                if len_y > 1:
                    self.y1.insert(len_y - 1, float('%.2f' % ((self.y1[len_y - 1] + self.y1[len_y - 2]) / 2)))
                stopTime = time.time()
                errorTime = stopTime - startTime
                if errorTime > 2:
                    intervalTime = 0
                else:
                    intervalTime = 2 - errorTime
                time.sleep(intervalTime)
            except Exception:
                print (u'\ncpuMem循环报错！报错信息:\n')
                traceback.print_exc()
                break
        self.y1.pop(0)
        self.y1_max = max(self.y1)
        self.y1_min = min(self.y1)
        self.y1_avg = '%.2f' % (sum(self.y1) / len(self.y1))

    def _runPerformance(self):
        tt = threading.Thread(target=self._runCpuAndMem)
        tt.start()
        while self.justDoIt:
            i = time.strftime("%Y%m%d-%H:%M:%S")
            print i
            self.x.append(i)
            try:
                startTime = time.time()
                self._value.allNeed()
                self.y2.append(self._value.frameRateNew())
                self.y3.append(self._value.memeryValue())
                self.y4.append(self._value.memeryRatio())
                self.y5.append(self._value.rxFlowConsumption())
                self.y6.append(self._value.txFlowConsumption())
                self.y7.append(self._value.batteryLevel())
                self.y8.append(self._value.batteryVoltage())
                self.y9.append(self._value.batteryTemperature())
                stopTime = time.time()
                errorTime = stopTime - startTime
                if errorTime > 1:
                    intervalTime = 0
                else:
                    intervalTime = 1 - errorTime
                time.sleep(intervalTime)
            except Exception:
                print (u'\nPerformance循环报错！报错信息:\n')
                traceback.print_exc()
                break
        self.x.pop(0)
        self.y2.pop(0)
        self.y3.pop(0)
        self.y4.pop(0)
        self.y5.pop(0)
        self.y6.pop(0)
        self.y7.pop(0)
        self.y8.pop(0)
        self.y9.pop(0)
        self.y2_max = max(self.y2)
        self.y2_min = min(self.y2)
        self.y2_avg = '%.2f' % (sum(self.y2) / len(self.y2))
        num = 0
        for each in self.y2:
            if each > 20.0:
                num += 1
        self.y2_pop = '%.1f' % (num * 100 / len(self.y2))

        self.y3_max = max(self.y3)
        self.y3_min = min(self.y3)
        self.y3_avg = '%.2f' % (sum(self.y3) / len(self.y3))
        self.y4_max = max(self.y4)
        self.y4_min = min(self.y4)
        self.y4_avg = '%.2f' % (sum(self.y4) / len(self.y4))
        self.y5_max = max(self.y5)
        self.y6_max = max(self.y6)
        self.y7_max = max(self.y7)
        self.y8_max = max(self.y8)
        self.y8_min = min(self.y8)
        self.y8_avg = '%.2f' % (sum(self.y8) / len(self.y8))
        self.y9_max = max(self.y9)
        self.y9_min = min(self.y9)
        self.y9_avg = '%.2f' % (sum(self.y9) / len(self.y9))
        tt.join()
        # self._creatReportExcel()
        return self._createTemplate()

    def _createTemplate(self):
        self.fig = tools.make_subplots(rows = 9, cols = 2,
                                       subplot_titles=('CPU(%)','','FPS','','Memery(M)','','Memery(%)','',u'接收数据(KB)','',u'发送数据(KB)',''),
                                       column_width=[5, 2],
        )
        data_1 = go.Scatter(
            name = 'CPU(%)',
            xaxis = dict(
                zeroline=True,
            ),
            marker=dict(
                color='#FF3030',
            ),
            x=self.x, y=self.y1,
        )
        data_1_extract = go.Bar(
            name='CPU(%)',
            marker=dict(
                color='#FF3030',
            ),
            x=[u'CPU最大占用(%)', u'CPU最小占用(%)', u'CPU平均占用(%)'],
            y=[self.y1_max, self.y1_min, self.y1_avg],
        )
        data_2 = go.Scatter(
            name = 'FPS',
            marker=dict(
                color='#66CD00',
            ),
            x=self.x,y=self.y2,
        )
        data_2_extract = go.Bar(
            name='FPS',
            marker=dict(
                color='#66CD00',
            ),
            x=[u'FPS最大值', u'FPS最小值', u'FPS平均值'],
            y=[self.y2_max, self.y2_min, self.y2_avg],
        )
        data_3 = go.Scatter(
            name = 'Memery(M)',
            marker=dict(
                color='#8B4726',
            ),
            x=self.x,y=self.y3,
        )
        data_3_extract = go.Bar(
            name='Memery(M)',
            marker=dict(
                color='#8B4726',
            ),
            x=[u'内存最大值(MB)', u'内存最小值(MB)', u'内存平均值(MB)'],
            y=[self.y3_max, self.y3_min, self.y3_avg],
        )
        data_4 = go.Scatter(
            name = 'Memery(%)',
            marker=dict(
                color='#B8860B',
            ),
            x=self.x,y=self.y4,
        )
        data_4_extract = go.Bar(
            name='Memery(%)',
            marker=dict(
                color='#B8860B',
            ),
            x=[u'内存最大占用(%)', u'内存最小占用(%)', u'内存平均占用(%)'],
            y=[self.y4_max, self.y4_min, self.y4_avg],
        )
        data_5 = go.Scatter(
            name = u'接收数据(KB)',
            marker=dict(
                color='#912CEE',
            ),
            x=self.x,y=self.y5,
        )
        data_5_extract = go.Bar(
            name=u'接收数据(KB)',
            marker=dict(
                color='#912CEE',
            ),
            x=[u'接收数据共消耗流量(KB)'],
            y=[self.y5_max],
        )
        data_6 = go.Scatter(
            name = u'发送数据(KB)',
            marker=dict(
                color='#7B68EE',
            ),
            x=self.x,y=self.y6,
        )
        data_6_extract = go.Bar(
            name=u'发送数据(KB)',
            marker=dict(
                color='#7B68EE',
            ),
            x=[u'发送数据共消耗流量(KB)'],
            y=[self.y6_max],
        )
        data_7 = go.Scatter(
            name=u'电量消耗(%)',
            marker=dict(
                color='#EEEE00',
            ),
            x=self.x, y=self.y7,
        )
        data_7_extract = go.Bar(
            name=u'电量消耗(%)',
            marker=dict(
                color='#EEEE00',
            ),
            x=[u'共消耗电量(%)'],
            y=[self.y7_max],
        )
        data_8 = go.Scatter(
            name=u'电池电压(mV)',
            marker=dict(
                color='#6495ED',
            ),
            x=self.x, y=self.y8,
        )
        data_8_extract = go.Bar(
            name=u'电池电压(mV)',
            marker=dict(
                color='#6495ED',
            ),
            x=[u'电池最大电压(mV)', u'电池最小电压(mV)', u'电池平均电压(mV)'],
            y=[self.y8_max, self.y8_min, self.y8_avg],
        )
        data_9 = go.Scatter(
            name=u'电池温度(℃)',
            marker=dict(
                color='#EE6AA7',
            ),
            x=self.x, y=self.y9,
        )
        data_9_extract = go.Bar(
            name=u'电池温度(℃)',
            marker=dict(
                color='#EE6AA7',
            ),
            x=[u'电池最大温度(℃)', u'电池最小温度(℃)', u'电池平均温度(℃)'],
            y=[self.y9_max, self.y9_min, self.y9_avg],
        )
        self.fig.append_trace(data_1, 1, 1)
        self.fig.append_trace(data_1_extract, 1, 2)
        self.fig.append_trace(data_2, 2, 1)
        self.fig.append_trace(data_2_extract, 2, 2)
        self.fig.append_trace(data_3, 3, 1)
        self.fig.append_trace(data_3_extract, 3, 2)
        self.fig.append_trace(data_4, 4, 1)
        self.fig.append_trace(data_4_extract, 4, 2)
        self.fig.append_trace(data_5, 5, 1)
        self.fig.append_trace(data_5_extract, 5, 2)
        self.fig.append_trace(data_6, 6, 1)
        self.fig.append_trace(data_6_extract, 6, 2)
        self.fig.append_trace(data_7, 7, 1)
        self.fig.append_trace(data_7_extract, 7, 2)
        self.fig.append_trace(data_8, 8, 1)
        self.fig.append_trace(data_8_extract, 8, 2)
        self.fig.append_trace(data_9, 9, 1)
        self.fig.append_trace(data_9_extract, 9, 2)
        try:
            brand = self._value._performanceCmd.getBrand().replace('\r', '').replace('\n', '')
            model = self._value._performanceCmd.getModel().replace('\r', '').replace('\n', '')
            release = self._value._performanceCmd.getRelease().replace('\r', '').replace('\n', '')
            sdk = self._value._performanceCmd.getSdk().replace('\r', '').replace('\n', '')
            self.fig['layout']['title'] = brand + '手机： ' + model + '<br>' \
                                          'Android系统：' + release + '  Android api：' + sdk
        except Exception:
            traceback.print_exc()
            print u'获取手机信息失败，检查手机版本'
        self.fig['layout']['height'] = 3000
        return self.fig

    def _creatReportExcel(self):
        #write excel,output values in point cell
        xlsName = os.path.dirname(sys.argv[0]) + "/PerformanceTestingReport.xls"
        sheetName = "Report"
        path = 'D:/AutoTestReport/Performance/REPORT/'
        style = self._setStyle(u'微软雅黑', 0x08, xlwt.Font.UNDERLINE_NONE)
        try:
            oldexcel = xlrd.open_workbook(xlsName,formatting_info=True)
        except:
            raise BaseException,"Cannot find report excel!"
        try:
            oldsheet = oldexcel.sheet_by_name(sheetName)
        except:
            raise BaseException,"Cannot find report sheet!"
        newexcel = copy(oldexcel)
        newsheet = newexcel.get_sheet(sheetName)
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,1) == "":
                newsheet.write_merge(i,i,1,1,self.y1_max,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,2) == "":
                newsheet.write_merge(i,i,2,2,self.y1_min,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,3) == "":
                newsheet.write_merge(i,i,3,3,self.y1_avg,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,4) == "":
                newsheet.write_merge(i,i,4,4,self.y3_max,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,5) == "":
                newsheet.write_merge(i,i,5,5,self.y3_min,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,6) == "":
                newsheet.write_merge(i,i,6,6,self.y3_avg,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,7) == "":
                newsheet.write_merge(i,i,7,7,self.y2_max,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,8) == "":
                newsheet.write_merge(i,i,8,8,self.y2_min,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,9) == "":
                newsheet.write_merge(i,i,9,9,self.y2_avg,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,10) == "":
                newsheet.write_merge(i,i,10,10,self.y2_pop,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,11) == "":
                newsheet.write_merge(i,i,11,11,self.y6_max,style)
                break
        for i in xrange(2,oldsheet.nrows):
            if oldsheet.cell_value(i,12) == "":
                newsheet.write_merge(i,i,12,12,self.y5_max,style)
                break
        for i in xrange(2,oldsheet.nrows):
            style = self._setStyle(u'微软雅黑', 0x0C, xlwt.Font.UNDERLINE_SINGLE)
            a = oldsheet.cell_value(i,13)
            print a
            if oldsheet.cell_value(i,13) == "":
                link = 'HYPERLINK("%s%s.html";"%s")'%(path,self.reportTime,self.reportTime)
                newsheet.write_merge(i,i,13,13,xlwt.Formula(link),style)
                break
            else:
                link = 'HYPERLINK("%s%s.html";"%s")' % (path, oldsheet.cell_value(i,13), oldsheet.cell_value(i,13))
                newsheet.write_merge(i, i, 13, 13, xlwt.Formula(link), style)
        newexcel.save(xlsName)

    def _setStyle(self, name, color, underline):
        #set excel cell style
        style = xlwt.XFStyle()
        fnt = xlwt.Font()  # 创建一个文本格式，包括字体、字号和颜色样式特性
        fnt.name = name  # 设置其字体为微软雅黑
        fnt.colour_index = color  # 设置其字体颜色
        fnt.underline = underline
        style.font = fnt
        #单元格对齐方式
        agmt = xlwt.Alignment()
        agmt.horz = xlwt.Alignment.HORZ_CENTER
        style.alignment = agmt
        #单元格边框格式
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        # 单元格边框颜色
        borders.left_colour = 0x00
        borders.right_colour = 0x00
        borders.top_colour = 0x00
        borders.bottom_colour = 0x00
        style.borders = borders
        return style

    def run(self, fileName, driver_ip=None):
        path = 'D:/AutoTestReport/Performance/REPORT/'
        if not os.path.exists(path):
            os.makedirs(path)
        plotly.offline.plot(self._runPerformance(), filename=path + fileName + '.html', auto_open=False)