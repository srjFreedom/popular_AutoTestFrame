# -*- coding: UTF-8 -*-
import wx
import inspect
import ctypes

import LJS_ProtoTest_Client
from Protoget import *
from LJS_ProtoTest_Client import *
from Transcode import *
import Socket_Com
from Dialog_Frame import *
from File_Manage import *

class Register_DialogBox(wx.Dialog):
    #注册对话框
    def __init__(self, proto_client, connect, *args, **kw):
        super(Register_DialogBox,self).__init__(*args, **kw)
        self.proto_client = proto_client
        self.connect = connect
        self.socket_com = Socket_Msg()
        self.flag = 0#注册成功状态
        wx.Frame.__init__(self, None, title=u"注册", size=(300, 280),
                          style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        self.SetMaxSize((300, 280))
        self.SetMinSize((300, 280))
        self.Center(wx.Center)
        self.RegPanel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE,self.evt_cancel)
        self.viewField1 = wx.StaticText(self.RegPanel, label=u"*账号：", pos=(10, 20), size=(60, 20),style=wx.ALIGN_RIGHT)
        self.inputAccnameField = wx.TextCtrl(self.RegPanel, pos=(75, 15), size=(195, 25), style=wx.TE_PROCESS_ENTER)
        self.viewField2 = wx.StaticText(self.RegPanel, label=u"*角色名：", pos=(10, 60), size=(60, 20),style=wx.ALIGN_RIGHT)
        self.inputNameField = wx.TextCtrl(self.RegPanel, pos=(75, 55), size=(195, 25), style=wx.TE_PROCESS_ENTER)
        self.viewField3 = wx.StaticText(self.RegPanel, label=u" 签名：", pos=(10, 100), size=(60, 20),style=wx.ALIGN_RIGHT)
        self.inputSignField = wx.TextCtrl(self.RegPanel, pos=(75, 95), size=(195, 25), style=wx.TE_PROCESS_ENTER)
        self.viewField4 = wx.StaticText(self.RegPanel, label=u"主角id：", pos=(10, 140), size=(60, 20),style=wx.ALIGN_RIGHT)
        self.inputMajorField = wx.TextCtrl(self.RegPanel, pos=(75, 135), size=(195, 25), style=wx.TE_PROCESS_ENTER)
        self.viewField4 = wx.StaticText(self.RegPanel, label=u"*为必填内容，其他选填", pos=(20, 170), size=(240, 20),style=wx.ALIGN_CENTER)
        self.btn_register = wx.Button(self.RegPanel, label=u"注册", pos=(20, 200), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.evt_register, self.btn_register)
        self.btn_Cancel = wx.Button(self.RegPanel, label=u"取消", pos=(180, 200), size=(80, 30))
        self.Bind(wx.EVT_BUTTON, self.evt_cancel, self.btn_Cancel)

    def evt_register(self,event):
        #注册
        self.accname = self.inputAccnameField.GetValue()
        self.name = self.inputNameField.GetValue()
        self.sign = self.inputSignField.GetValue()
        self.major = self.inputMajorField.GetValue()
        sleeptime = 0
        if self.accname == u"":
            # 空字符串账号事件
            login_dlg = wx.MessageDialog(self, u"账号不能为空！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        elif self.name == u"":
            #昵称空字符串账号事件
            login_dlg = wx.MessageDialog(self, u"角色名不能为空！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        elif self.major == u"":
            #默认主角id
            registdata = 'c2s_register' + " '%s' '%s' '%s' 2000"%(self.accname,self.name,self.sign)
            self.socket_com.send_proto(self.connect, registdata)
            while True:
                pbdatas = Socket_Com.protodata
                pbdatas.reverse()
                for proto in pbdatas:
                    if proto[0] == u"s2c_register":
                        if proto[1][0] == 1:
                            self.flag = 1
                        else:
                            self.flag = 2
                        break
                if self.flag == 1 or self.flag == 2:
                    break
                sleeptime += 0.01
                time.sleep(sleeptime)
                if sleeptime > 2:
                    login_dlg = wx.MessageDialog(self, u"注册超时，请重试！", u"提示", wx.OK)
                    login_dlg.ShowModal()
                    login_dlg.Destroy()
            if self.flag == 0 or self.flag == 2:
                login_dlg = wx.MessageDialog(self, u"注册失败！", u"提示", wx.OK)
                login_dlg.ShowModal()
                login_dlg.Destroy()
        else:
            registdata = 'c2s_register' + " '%s' '%s' '%s' %s"%(self.accname,self.name,self.sign,self.major)
            self.socket_com.send_proto(self.connect, registdata)
            while True:
                pbdatas = Socket_Com.protodata
                pbdatas.reverse()
                for proto in pbdatas:
                    if proto[0] == u"s2c_register":
                        if proto[1][0] == 1:
                            self.flag = 1
                        else:
                            self.flag = 2
                        break
                if self.flag == 1 or self.flag == 2:
                    break
                sleeptime += 0.01
                time.sleep(sleeptime)
                if sleeptime > 2:
                    login_dlg = wx.MessageDialog(self, u"注册超时，请重试！", u"提示", wx.OK)
                    login_dlg.ShowModal()
                    login_dlg.Destroy()
                    break
            if self.flag == 0 or self.flag == 2:
                login_dlg = wx.MessageDialog(self, u"注册失败！", u"提示", wx.OK)
                login_dlg.ShowModal()
                login_dlg.Destroy()
        if self.flag == 1:
            self.Destroy()

    def evt_cancel(self,event):
        #取消注册
        self.Destroy()

class Login_DialogBox(wx.Dialog):
    # 登录对话框
    def __init__(self, proto_client, state, accname, connect, logger, *args, **kw):
        super(Login_DialogBox, self).__init__(*args, **kw)
        self.client = proto_client
        self.logger = logger
        self.connect = connect
        self.state = state
        self.accname = accname
        self.socket_com = Socket_Msg()
        wx.Frame.__init__(self, None, title=u"登录", size=(300, 200), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        self.SetMaxSize((300, 200))
        self.SetMinSize((300, 200))
        self.Center(wx.Center)
        self.loginPanel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.evt_button_cancellogin)
        if state == 0:
            # 账号输入：
            self.viewField1 = wx.StaticText(self.loginPanel, label=u"账号：", pos=(20,20), size=(50, 30))
            self.inputAccnameField = wx.TextCtrl(self.loginPanel,pos=(75,20),size=(195,25),style=wx.TE_PROCESS_ENTER)
            self.viewField1 = wx.StaticText(self.loginPanel, label=u"密码：", pos=(20,60), size=(50, 30))
            self.inputPasswordField = wx.TextCtrl(self.loginPanel,pos=(75,60),size=(195,25),style=wx.TE_PROCESS_ENTER)
            # 登录取消
            self.btn_Login = wx.Button(self.loginPanel,label=u"登录",pos=(20,100),size=(80,30))
            self.Bind(wx.EVT_BUTTON,self.evt_button_login,self.btn_Login)
            self.btn_Cancel = wx.Button(self.loginPanel, label=u"取消", pos=(180,100), size=(80,30))
            self.Bind(wx.EVT_BUTTON,self.evt_button_cancellogin,self.btn_Cancel)
        else:
            # 已登录
            self.viewField1 = wx.StaticText(self.loginPanel, label=u"已有账号登录!\n登录账号为:%s"%accname, pos=(20,50), size=(260,40),style= wx.ALIGN_CENTER)
            self.btn_logout = wx.Button(self.loginPanel, label=u"注销", pos=(50, 100), size=(80, 30))
            self.Bind(wx.EVT_BUTTON, self.evt_button_logout, self.btn_logout)
            self.btn_OK = wx.Button(self.loginPanel,label=u"关闭",pos=(170,100),size=(80,30))
            self.Bind(wx.EVT_BUTTON,self.evt_button_cancellogin,self.btn_OK)

    def evt_button_login(self, event):
        # 登录事件
        self.accname = self.inputAccnameField.GetValue()
        self.password = self.inputPasswordField.GetValue()
        if self.accname == u"":
            # 空字符串账号事件
            login_dlg = wx.MessageDialog(self, u"账号不能为空！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            account_info = "c2s_login" + " '%s' '%s'"%(self.accname,self.password)
            self.socket_com.send_proto(self.connect,account_info)
            # 登录状态判定
            time.sleep(0.1)
            pbdatas = Socket_Com.protodata
            pbdatas.reverse()
            for proto in pbdatas:
                if proto[0] == u"s2c_login":
                    if proto[1][0] == 1:
                        self.state = 1
                    break
            if self.state == 0:
                login_dlg = wx.MessageDialog(self, u"登录失败！", u"提示", wx.OK)
                login_dlg.ShowModal()
                login_dlg.Destroy()
            if self.state == 1:
                #通知服务器前端加载完成，登录后的初始化协议
                c2s = "c2s_game_loaded"
                self.socket_com.send_proto(self.connect,c2s)
                self.Destroy()

    def evt_button_logout(self, event):
        # 注销事件
        self.connect = self.client.logout(self.connect, self.logger)
        self.state = 0
        self.Destroy()

    def evt_button_cancellogin(self, event):
        # 取消登录事件
        self.Destroy()

class Parallel_DialogBox(wx.Dialog):
    # 压力测试界面
    def __init__(self, proto_client, syschecklist, protochecklist, *args, **kw):
        super(Parallel_DialogBox, self).__init__(*args, **kw)
        self.client = proto_client
        self.socket_com = Socket_Msg()
        self.connects = []#socket列表
        self.syschecklist = syschecklist
        if u"其他" not in self.syschecklist:
            self.syschecklist.append(u"其他")
        self.protochecklist = protochecklist
        self.protochecklist.setdefault(u"其他",[u"发送GM命令"])
        self.protoname = ""

        wx.Frame.__init__(self, None, title=u"压力测试", size=(600, 300), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        self.SetMaxSize((600, 350))
        self.SetMinSize((600, 350))
        self.Center(wx.Center)
        self.parallelPanel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.evt_button_cancellogin)

        #注册部分
        self.viewFieldPL = wx.StaticText(self.parallelPanel, label=u"批量注册账号", pos=(10, 10), size=(180, 20),style=wx.ALIGN_CENTER)
        self.viewField1 = wx.StaticText(self.parallelPanel, label=u"账号名：", pos=(10,42), size=(80, 20))
        self.inputAccnameField = wx.TextCtrl(self.parallelPanel,pos=(95,40),size=(85,25),style=wx.TE_PROCESS_ENTER)
        self.viewField2 = wx.StaticText(self.parallelPanel, label=u"注册数量：", pos=(10,83), size=(80, 20))
        self.inputNumField = wx.TextCtrl(self.parallelPanel,pos=(95,80),size=(85,25),style=wx.TE_PROCESS_ENTER)
        self.inputNumField.SetValue("1")
        self.btn_mlregister = wx.Button(self.parallelPanel,label=u"注册",pos=(40,115),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_button_mlregister,self.btn_mlregister)

        #登录部分
        self.viewFieldLN = wx.StaticText(self.parallelPanel, label=u"批量登录账号", pos=(200, 10), size=(400, 20),style=wx.ALIGN_CENTER)
        self.viewField3 = wx.StaticText(self.parallelPanel, label=u"账号名：", pos=(300, 42), size=(80, 20))
        self.inputAccnameField1 = wx.TextCtrl(self.parallelPanel, pos=(395, 40), size=(150, 25), style=wx.TE_PROCESS_ENTER)
        self.viewField4 = wx.StaticText(self.parallelPanel, label=u"登录数量：", pos=(300,83), size=(80, 20))
        self.inputNumField1 = wx.TextCtrl(self.parallelPanel,pos=(395,80),size=(150,25),style=wx.TE_PROCESS_ENTER)
        self.btn_mllogin = wx.Button(self.parallelPanel,label=u"登录",pos=(390,115),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_button_mllogin,self.btn_mllogin)

        #协议批量发送部分
        self.viewField5 = wx.StaticText(self.parallelPanel, label=u"选择系统：", pos=(20, 172), size=(80, 20))
        self.sysCheckList = wx.Choice(self.parallelPanel,pos=(100,170),size=(100,30),choices=self.syschecklist)
        self.sysCheckList.Bind(wx.EVT_CHOICE,self.evt_sysCheckBox_Choose)
        self.sysCheckList.SetSelection(0)
        self.viewField6 = wx.StaticText(self.parallelPanel, label=u"协议选择：", pos=(290,172), size=(80, 20))
        self.protoCheckList = wx.Choice(self.parallelPanel,pos=(370,170),size=(200,30))
        self.viewField7 = wx.StaticText(self.parallelPanel, label=u"输入协议参数：", pos=(40, 212), size=(100, 20))
        self.inputContentField = wx.TextCtrl(self.parallelPanel, pos=(140, 210), size=(400, 25),
                                              style=wx.TE_PROCESS_ENTER)
        self.btn_mlsend = wx.Button(self.parallelPanel,label=u"批量发送",pos=(260,250),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_button_mlsend,self.btn_mlsend)

    # 列表选择事件
    def evt_sysCheckBox_Choose(self, event):
        # 系统选择
        if len(self.connects) > 0:
            protolist = []
            sysname = self.sysCheckList.GetStringSelection()
            for key,value in self.protochecklist.items():
                if sysname == key:
                    protolist = value
                    break
            self.protoCheckList.SetItems(protolist)
            # 默认选中第1个协议，初始化协议选中状态
            self.protoCheckList.SetSelection(0)
            self.protoname = self.protoCheckList.GetStringSelection()
        else:
            login_dlg = wx.MessageDialog(self, u"请先批量登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()
            login_dlg.Destroy()

    def evt_button_mlregister(self, event):
        # 注册事件
        accname = self.inputAccnameField.GetValue()
        numtxt = self.inputNumField.GetValue()
        result = []
        ssc = 0
        fls = 0
        if accname == u"":
            #空字符串账号事件
            dlg = wx.MessageDialog(self, u"账号名不能为空！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        try:
            #非数字字符处理
            num = int(numtxt)
            if num < 1:
                #数量为0或负数处理
                dlg = wx.MessageDialog(self, u"注册数量不能小于1！", u"提示", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()
            else:
                #批量建立协议通道并发送注册协议
                threads = []
                for i in range(num):
                    acname = accname + str(i)
                    name = accname + str(i)
                    host_data = LJS_ProtoTest_Client().login_getway()
                    t = SocketThread(LJS_ProtoTest_Client().connect_and_register, args=(host_data,acname,name))
                    threads.append(t)
                    t.start()
                    t.join()
                #账号注册结果反馈
                for t in threads:
                    result.append(t.result)
                for j in range(len(result)):
                    if result[j] == 1:
                        ssc += 1
                    else:
                        fls += 1
                dlg = wx.MessageDialog(self, u"注册成功%s个账号，失败%s个账号"%(ssc,fls), u"提示", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()
        except:
            dlg = wx.MessageDialog(self, u"数量不能输入非数字的字符！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()

    def evt_button_mllogin(self, event):
        # 登录事件
        accname = self.inputAccnameField1.GetValue()
        numtxt = self.inputNumField1.GetValue()
        result = []
        ssc = 0
        fls = 0
        if accname == u"":
            #空字符串账号事件
            dlg = wx.MessageDialog(self, u"账号名不能为空！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        try:
            #非数字字符处理
            num = int(numtxt)
            if num < 1:
                #数量为0或负数处理
                dlg = wx.MessageDialog(self, u"登录数量不能小于1！", u"提示", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()
            else:
                #批量建立协议通道并发送登录协议
                threads = []
                for i in range(1,num + 1):
                    acname = accname + str(i)
                    host_data = LJS_ProtoTest_Client().login_getway()
                    t = SocketThread(LJS_ProtoTest_Client().connect_and_login, args=(host_data,acname))
                    threads.append(t)
                    t.start()
                    t.join()
                #账号登录结果反馈
                for t in threads:
                    data = t.result
                    result.append(data[0])
                    self.connects.append(data[1])
                for j in range(len(result)):
                    if result[j] == 1:
                        ssc += 1
                    else:
                        fls += 1
                dlg = wx.MessageDialog(self, u"登录成功%s个账号，失败%s个账号"%(ssc,fls), u"提示", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()
        except:
            dlg = wx.MessageDialog(self, u"数量不能输入非数字的字符！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()

    def evt_button_mlsend(self, event):
        #批量发送协议
        if len(self.connects) > 0:
            self.protoname = self.protoCheckList.GetStringSelection()
            if self.protoname == u"发送GM命令":
                self.protoname = u"c2s_world_chat"
            content = self.inputContentField.GetValue()
            if content == u"":
                content = self.protoname
            else:
                content = self.protoname + u" " + content
            pttime = TimeTreatment().getlocaltimestamp() + 2#延迟操作，用于多线程创建的延迟
            for connect in self.connects:
                t = SocketThread(Socket_Msg().send_proto_repeate, args=(connect,content,pttime))
                t.start()
            while TimeTreatment().getlocaltimestamp() < pttime:
                time.sleep(0.1)
            dlg = wx.MessageDialog(self, u"协议批量发送成功！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, u"请先批量登录账号！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()

    def evt_button_cancellogin(self, event):
        # 关闭窗口事件
        if len(self.connects) > 0:
            #关闭连接中的socket，释放占用连接
            for connect in self.connects:
                connect.shutdown(2)
                connect.close()
        self.Destroy()

class Datch_DialogBox(wx.Dialog):
    # 批量生成协议界面与批量跑脚本界面
    def __init__(self, *args, **kw):
        super(Datch_DialogBox, self).__init__(*args, **kw)
        self.socket_com = Socket_Msg()
        self.manage = File_Manage()
        self.sysList = []
        self.protoList = []
        self.protoname = ""
        self.connect = None
        self.t = None #线程数，用于处理多工作流的问题

        wx.Frame.__init__(self, None, title=u"协议流测试", size=(500, 250), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        self.SetMaxSize((500, 280))
        self.SetMinSize((500, 280))
        self.Center(wx.Center)
        self.datchPanel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.evt_button_close)

        #登录部分
        self.viewFieldPL = wx.StaticText(self.datchPanel, label=u"登录账号", pos=(0, 10), size=(200, 20),style=wx.ALIGN_CENTER)
        self.viewField1 = wx.StaticText(self.datchPanel, label=u"账号名：", pos=(10,42), size=(60, 20))
        self.inputAccnameField = wx.TextCtrl(self.datchPanel,pos=(75,40),size=(125,25),style=wx.TE_PROCESS_ENTER)
        self.viewField2 = wx.StaticText(self.datchPanel, label=u"密码：", pos=(10,82), size=(60, 20))
        self.inputNumField = wx.TextCtrl(self.datchPanel,pos=(75,80),size=(125,25),style=wx.TE_PROCESS_ENTER)
        self.btn_login = wx.Button(self.datchPanel,label=u"登录",pos=(60,120),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_login,self.btn_login)

        #选择协议流部分
        self.viewFieldLN = wx.StaticText(self.datchPanel, label=u"选择测试集", pos=(250, 10), size=(250, 20),style=wx.ALIGN_CENTER)
        self.viewField3 = wx.StaticText(self.datchPanel, label=u"选择系统：", pos=(250,42), size=(60, 20))
        self.sysCheckList = wx.Choice(self.datchPanel,pos=(310,40),size=(160,30))
        self.Bind(wx.EVT_CHOICE,self.evt_sys_choice,self.sysCheckList)
        self.viewField4 = wx.StaticText(self.datchPanel, label=u"选择协议：", pos=(250,82), size=(60, 20))
        self.protoCheckList = wx.Choice(self.datchPanel,pos=(310,80),size=(160,30))
        self.btn_run = wx.Button(self.datchPanel,label=u"开始测试",pos=(335,120),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_run,self.btn_run)

        #工程进度条
        self.viewField5 = wx.StaticText(self.datchPanel, label=u"执行进度：", pos=(10, 180), size=(60, 20))
        self.gauge = wx.Gauge(self.datchPanel,range=200,pos=(70,180),size=(300,20),name="gauge")
        self.btn_stop = wx.Button(self.datchPanel,label=u"停止测试",pos=(390,175),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_stop,self.btn_stop)
        self.viewFieldGg = wx.StaticText(self.datchPanel, pos=(170, 205), size=(100, 20),style=wx.ALIGN_CENTER)

    def evt_sys_choice(self,event):
        #系统列表选择事件
        xlsName = self.sysCheckList.GetStringSelection()
        self.protoList = [] #列表重置
        if xlsName == "all":
            #处理全选事件
            self.protoList.append("all")
            self.protoCheckList.SetItems(self.protoList)
            self.protoCheckList.SetSelection(0)
        else:
            self.protoList = self.manage.get_sheetname_all(xlsName)
            self.protoList.insert(0,"all")
            self.protoCheckList.SetItems(self.protoList)
            self.protoCheckList.SetSelection(0)

    def evt_button_close(self, event):
        # 关闭窗口事件
        if self.connect is not None:
            # 关闭连接中的socket，释放占用连接
            self.connect.shutdown(2)
            self.connect.close()
            self.connect = None
        self.Destroy()

    def evt_login(self,event):
        #登录事件
        if self.connect is None:
            accname = self.inputAccnameField.GetValue()
            if accname == u"":
                #空字符串账号事件
                dlg = wx.MessageDialog(self, u"账号名不能为空！", u"提示", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()
            else:
                host_data = LJS_ProtoTest_Client().login_getway()
                res = LJS_ProtoTest_Client().connect_and_login(host_data, accname)
                if res[0] == 1:
                    #检查账号登录结果，若登录失败，则断开socket，避免重复建立连接
                    self.connect = res[1]
                    dlg = wx.MessageDialog(self, u"登录成功！", u"提示", wx.OK)
                    dlg.ShowModal()  # 显示对话框
                    dlg.Destroy()
                    self.sysList = self.manage.get_filename_all()
                    self.sysList.insert(0,"all")
                    self.sysCheckList.SetItems(self.sysList)
                    self.sysCheckList.SetSelection(0)
                else:
                    dlg = wx.MessageDialog(self, u"登录失败，请检查输入内容！", u"提示", wx.OK)
                    dlg.ShowModal()  # 显示对话框
                    dlg.Destroy()
                    try:
                        res[1].shutdown(2)
                        res[1].close()
                    except:
                        print u"未产生socket连接"
        else:
            #处理已登录状态
            dlg = wx.MessageDialog(self, u"当前已有账号登录！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()

    def evt_run(self,event):
        #开启任务事件
        if self.connect is None:
            dlg = wx.MessageDialog(self, u"请先登录账号！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            if self.t is None:
                self.t = threading.Thread(target=self.working_run)
                self.t.start()
            else:
                dlg = wx.MessageDialog(self, u"不允许开展多个测试工作流！", u"警告", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()

    def evt_stop(self,event):
        #停止任务事件
        if self.t is not None:
            self._async_raise(self.t.ident, SystemExit)
            dlg = wx.MessageDialog(self, u"任务已停止！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
            self.gauge.SetValue(0)
            self.viewFieldGg.SetLabel("")
            self.t = None
        else:
            dlg = wx.MessageDialog(self, u"当前并无工作流在执行！", u"提示", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()

    def working_run(self):
        #任务工作流
        self.viewFieldGg.SetLabel(u"初始化中...")
        xlsName = self.sysCheckList.GetStringSelection()
        sheetName = self.protoCheckList.GetStringSelection()
        status = 0
        if xlsName == "all":
            #运行分支，选择所有系统
            self.sysList.pop(0)
            sysList = self.sysList
            paramlist = []
            maxstatus = 0
            for xlsName in sysList:
                xlist = []
                protoList = self.manage.get_sheetname_all(xlsName)
                for sheetName in protoList:
                    plist = self.manage.read_params_from_excel(xlsName, sheetName)
                    maxstatus += len(plist)
                    xlist.append(plist)
                paramlist.append(xlist)
            self.gauge.SetRange(maxstatus)
            for i in range(len(sysList)):
                #依次读取所有系统表
                xlsName = sysList[i]
                protoList = self.manage.get_sheetname_all(xlsName)
                for j in range(len(protoList)):
                    #依次读取所有表单
                    sheetName = protoList[j]
                    for k in range(len(paramlist[i][j])):
                        #依次读取表单中所有测试用例
                        self.gauge.SetValue(status)
                        info = u"当前进度：" + unicode(format(float(status) / float(maxstatus) * 100, '.2f')) + u"%"
                        self.viewFieldGg.SetLabel(info)
                        if paramlist[i][j][k].has_key(u'values'):
                            print u"有参数"
                            value_str = ""
                            for each in paramlist[i][j][k][u'values']:
                                value_str += " " + unicode(each)
                            protodata = paramlist[i][j][k][u'c2s'] +  value_str
                            resproto = paramlist[i][j][k][u"s2c"]
                            resdata,restime = self.socket_com.send_and_resrve_data(self.connect, protodata, resproto)
                            self.manage.write_result(xlsName,sheetName,k+1,4,resdata)
                            self.manage.write_result(xlsName,sheetName,k+1,6,restime)
                        else:
                            print u"无参数"
                            protodata = paramlist[i][j][k][u'c2s']
                            resproto = paramlist[i][j][k][u"s2c"]
                            resdata,restime = self.socket_com.send_and_resrve_data(self.connect,protodata, resproto)
                            self.manage.write_result(xlsName,sheetName,k+1,4,resdata)
                            self.manage.write_result(xlsName,sheetName,k+1,6,restime)
                        status += 1
                        self.gauge.SetValue(status)
                        info = u"当前进度：" + unicode(format(float(status) / float(maxstatus) * 100, '.2f')) + u"%"
                        self.viewFieldGg.SetLabel(info)
        else:
            # 运行分支，选择指定系统
            if sheetName == "":
                #选择空协议处理
                dlg = wx.MessageDialog(self, u"选择的协议不能为空！", u"警告", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()
            elif sheetName == "all":
                # 运行分支，选择所有协议
                self.protoList.pop(0)
                sheetList = self.protoList
                paramlist = []
                maxstatus = 0
                for sheetName in sheetList:
                    plist = self.manage.read_params_from_excel(xlsName,sheetName)
                    maxstatus += len(plist)
                    paramlist.append(plist)
                self.gauge.SetRange(maxstatus)
                for i in range(len(sheetList)):
                    sheetName = sheetList[i]
                    for j in range(len(paramlist[i])):
                        self.gauge.SetValue(status)
                        info = u"当前进度：" + unicode(format(float(status) / float(maxstatus) * 100, '.2f')) + u"%"
                        self.viewFieldGg.SetLabel(info)
                        if paramlist[i][j].has_key(u'values'):
                            print u"有参数"
                            value_str = ""
                            for each in paramlist[i][j][u'values']:
                                value_str += " " + unicode(each)
                            protodata = paramlist[i][j][u'c2s'] +  value_str
                            resproto = paramlist[i][j][u"s2c"]
                            resdata,restime = self.socket_com.send_and_resrve_data(self.connect, protodata, resproto)
                            self.manage.write_result(xlsName,sheetName,j+1,4,resdata)
                            self.manage.write_result(xlsName,sheetName,j+1,6,restime)
                        else:
                            print u"无参数"
                            protodata = paramlist[i][j][u'c2s']
                            resproto = paramlist[i][j][u"s2c"]
                            resdata,restime = self.socket_com.send_and_resrve_data(self.connect,protodata, resproto)
                            self.manage.write_result(xlsName,sheetName,j+1,4,resdata)
                            self.manage.write_result(xlsName,sheetName,j+1,6,restime)
                        status += 1
                        self.gauge.SetValue(status)
                        info = u"当前进度：" + unicode(format(float(status) / float(maxstatus) * 100, '.2f')) + u"%"
                        self.viewFieldGg.SetLabel(info)
            else:
                # 运行分支，选择指定协议
                paramlist = self.manage.read_params_from_excel(xlsName,sheetName)
                maxstatus = len(paramlist)
                self.gauge.SetRange(maxstatus)
                while status < maxstatus:
                    self.gauge.SetValue(status)
                    info = u"当前进度：" + unicode(format(float(status) / float(maxstatus) * 100, '.2f')) + u"%"
                    self.viewFieldGg.SetLabel(info)
                    if paramlist[status].has_key(u'values'):
                        print u"有参数"
                        value_str = ""
                        for each in paramlist[status][u'values']:
                            value_str += " " + unicode(each)
                        protodata = paramlist[status][u'c2s'] +  value_str
                        resproto = paramlist[status][u"s2c"]
                        resdata,restime = self.socket_com.send_and_resrve_data(self.connect, protodata, resproto)
                        self.manage.write_result(xlsName,sheetName,status+1,4,resdata)
                        self.manage.write_result(xlsName,sheetName,status+1,6,restime)
                    else:
                        print u"无参数"
                        protodata = paramlist[status][u'c2s']
                        resproto = paramlist[status][u"s2c"]
                        resdata,restime = self.socket_com.send_and_resrve_data(self.connect,protodata, resproto)
                        self.manage.write_result(xlsName,sheetName,status+1,4,resdata)
                        self.manage.write_result(xlsName,sheetName,status+1,6,restime)
                    status += 1
                    self.gauge.SetValue(status)
                    info = u"当前进度：" + unicode(format(float(status) / float(maxstatus) * 100, '.2f')) + u"%"
                    self.viewFieldGg.SetLabel(info)
        time.sleep(0.5)
        dlg = wx.MessageDialog(self, u"任务已全部完成！", u"提示", wx.OK)
        dlg.ShowModal()  # 显示对话框
        dlg.Destroy()
        self.t = None

    def _async_raise(self, tid, exctype):
        #结束线程方法
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")