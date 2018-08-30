# -*- coding: UTF-8 -*-
import wx
import threading
import os,time,sys
from performanceRunner import *

class TestDialog(wx.Frame):

    def __init__(self, parent, title):
        self.p = performanceRunner()
        self.Wkstate = False
        self.reportpath = 'D:\AutoTestReport\Performance\REPORT'
        self.model = 1
        self.ip = ""

        wx.Frame.__init__(self, parent, title = title, size = (300, 350),style=wx.DEFAULT_FRAME_STYLE ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        self.SetMaxSize((300, 350))
        self.SetMinSize((300, 350))
        self.Center(wx.Center)

        self.UserPanel = wx.Panel(self)
        #选择模式
        self.btn_Model1 = wx.Button(self.UserPanel, label=u'连线使用',pos=(35,130),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_choose_Model1,self.btn_Model1)
        self.viewIpField = wx.StaticText(self.UserPanel,label=u"输入ip地址:", pos=(150,80), size=(150, 20),style=wx.TE_CENTER)
        self.text_IPinput = wx.TextCtrl(self.UserPanel,pos=(165,105),size=(115,20))
        self.btn_Model2 = wx.Button(self.UserPanel, label=u'无线使用',pos=(185,130),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_choose_Model2,self.btn_Model2)
        #运行时长显示
        self.timeField = wx.StaticText(self.UserPanel, label=u"选择使用模式", pos=(20,20), size=(260, 30), style=wx.ALIGN_CENTER)
        self.timeFont = wx.Font(15,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.timeField.SetFont(self.timeFont)

        self.btnWkjob = wx.Button(self.UserPanel, label=u'开始打点',pos=(90,80),size=(120,40))
        self.btnFont = wx.Font(12,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.btnWkjob.SetFont(self.btnFont)
        self.btnWkjob.Show(False)
        self.Bind(wx.EVT_BUTTON,self.evt_btn_Working,self.btnWkjob)

        #报告列表
        self.reportField = wx.StaticText(self.UserPanel, label=u"报告列表", pos=(150, 170), size=(80, 20), style=wx.ALIGN_CENTER)
        self.reportFont = wx.Font(11,wx.DEFAULT,wx.NORMAL,wx.NORMAL)
        self.reportField.SetFont(self.reportFont)
        self.reportChoiceList = wx.Choice(self.UserPanel,pos=(100,192),size=(180,25))

        self.btnGetReport = wx.Button(self.UserPanel, label=u'刷新列表',pos=(10,190),size=(80,30))
        self.btnFont = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.NORMAL)
        self.btnGetReport.SetFont(self.btnFont)
        self.Bind(wx.EVT_BUTTON,self.evt_btn_GetReport,self.btnGetReport)

        self.checkReport = wx.Button(self.UserPanel, label=u'查看报告',pos=(10,225),size=(80,30))
        self.btnFont = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.NORMAL)
        self.checkReport.SetFont(self.btnFont)
        self.Bind(wx.EVT_BUTTON,self.evt_btn_OpenReport,self.checkReport)

        self.deleteReport = wx.Button(self.UserPanel, label=u'清空报告',pos=(10,260),size=(80,30))
        self.btnFont = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.NORMAL)
        self.deleteReport.SetFont(self.btnFont)
        self.Bind(wx.EVT_BUTTON,self.evt_btn_DeleteReport,self.deleteReport)

    def evt_choose_Model1(self, event):
        self.model = 1
        self.btn_Model1.Show(False)
        self.btn_Model2.Show(False)
        self.viewIpField.Show(False)
        self.text_IPinput.Show(False)
        self.btnWkjob.Show(True)
        self.timeField.SetLabel("")

    def evt_choose_Model2(self, event):
        self.model = 2
        self.ip = self.text_IPinput.GetValue()
        self.btn_Model1.Show(False)
        self.btn_Model2.Show(False)
        self.viewIpField.Show(False)
        self.text_IPinput.Show(False)
        self.btnWkjob.Show(True)
        self.timeField.SetLabel("")

    def evt_btn_Working(self,event):
        if self.Wkstate == False:
            self.Wkstate = True
            t = threading.Thread(target=self.woking_treading)
            t.start()
            reporttime = time.strftime("%Y-%m-%d-%H-%M-%S")
            if self.model == 1:
                self.p.affStart(reporttime)
            else:
                self.p.affStart(affName=reporttime,driver_ip=self.ip)
            self.btnWkjob.SetLabel(u"停止记录")
        else:
            self.p.affStop()
            self.Wkstate = False
            self.btnWkjob.SetLabel(u"开始记录")

    def woking_treading(self):
        starttime = time.time()
        while self.Wkstate is True:
            time.sleep(1)
            nowtime = time.time()
            diftime = int(nowtime - starttime)
            min = diftime / 60
            hour = diftime / 200
            if hour == 0:
                if min == 0:
                    scd = diftime % 60
                    timeinfo = u"本次记录时长：%s秒" %scd
                else:
                    scd = diftime % 60
                    timeinfo = u"本次记录时长：%s分%s秒" %(min, scd)
            else:
                min = (diftime % 3600) / 60
                scd = (diftime % 3600) % 60
                timeinfo = u"本次记录时长：%s小时%s分%s秒" % (hour, min, scd)
            self.timeField.SetLabel(timeinfo)
        self.timeField.SetLabel(u"本次打点记录结束.")

    def evt_btn_GetReport(self, event):
        path = os.path.join(os.path.dirname(sys.argv[0]),self.reportpath)
        dirlist = os.listdir(path)
        filelist = []
        for index in range(len(dirlist)):
            if dirlist[index].find(".html") > 0:
                filelist.append((dirlist[index]).split(".")[0])
        self.reportChoiceList.Set(filelist)
        self.reportChoiceList.SetSelection(0)

    def evt_btn_OpenReport(self, event):
        if self.reportChoiceList.GetStringSelection() != "":
            path = self.reportpath + "\\" + self.reportChoiceList.GetStringSelection() + ".html"
            try:
                os.system(path)
            except:
                dlg = wx.MessageDialog(self, u"打开报告文件失败，请确认是否存在指定的报告！", u"错误", wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, u"请先选择一份报告！", u"警告", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

    def evt_btn_DeleteReport(self, event):
        sure_dlg = wx.MessageDialog(self, u"确认是否要清空报告列表?", u"提示", wx.YES_NO | wx.ICON_ASTERISK)
        if sure_dlg.ShowModal() == wx.ID_YES:
            try:
                path = os.path.join(os.path.dirname(sys.argv[0]), self.reportpath)
                dirlist = os.listdir(path)
                for index in range(len(dirlist)):
                    if dirlist[index].find(".html") > 0:
                        os.remove(self.reportpath + "\\" + dirlist[index])
                dlg = wx.MessageDialog(self, u"报告已全部清空！", u"提示", wx.OK | wx.ICON_ASTERISK)
                dlg.ShowModal()
                dlg.Destroy()
            except:
                dlg = wx.MessageDialog(self, u"文件删除失败，请确认报告文件是否正在使用中！", u"错误", wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
        sure_dlg.Destroy()

class TestApp(wx.App):

    def OnInit(self):
        self.frame = TestDialog(None, u'性能测试小工具')
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
     app = TestApp()
     app.MainLoop()