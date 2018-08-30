# -*- coding: UTF-8 -*-
import wx
import LJS_ProtoTest_Client
from Protoget import *
from LJS_ProtoTest_Client import *
from Transcode import *
import Socket_Com
from Dialog_Frame import *

#菜单宏
ID_REGISTER = 10001
ID_LOGIN = 10002
ID_FILE2 = 10003
ID_FILE3 = 10004

ID_PARALLEL = 10021
ID_STREAM = 10022

class Proto_Window(wx.Frame):

    def __init__(self, parent, title):
        # 系统类初始化
        self.protoget = Protoget()
        self.proto_client = LJS_ProtoTest_Client()
        self.socket_com = Socket_Msg()

        # 登录状态初始化（0：未登录，1：已登录）
        self.login_state = 0
        # 登录账号初始化
        self.login_accname = ""
        # 返回协议信息初始化
        self.proto_logger = ""
        # 系统列表初始化
        self.sysList = self.protoget.getsystem()
        # 协议列表字典初始化
        self.protoList = self.protoget.getproto()
        #配置内容预定义
        self.itemList = Transexcel().readexcel("Goods.xlsx", u"Sheet1")
        self.partnerList = Transexcel().readexcel("Partner.xlsx", u"Sheet1")
        self.majorList = Transexcel().readexcel("Major.xlsx", u"Major")
        self.petList = Transexcel().readexcel("Pet.xlsx",u"Sheet1")

        wx.Frame.__init__(self, parent, title=title, size=(1200, 800), style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)
        # self.SetMaxSize((1200, 800))
        # self.SetMinSize((1200, 800))
        self.Center(wx.Center)
        self.UserPanel = wx.Panel(self,size=(1200,800),pos=(0,0))
        # self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        # 重定义关闭方法
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # 设置菜单
        filemenu = wx.Menu()
        self.menu_register = filemenu.Append(ID_REGISTER,u"注册账户")
        self.Bind(wx.EVT_MENU,self.evt_register,self.menu_register)
        self.menu_about = filemenu.Append(ID_LOGIN, u"登录账号")
        self.Bind(wx.EVT_MENU, self.evt_login, self.menu_about)
        filemenu.AppendSeparator()
        self.menu_close = filemenu.Append(wx.ID_EXIT, u"退出")
        self.Bind(wx.EVT_MENU, self.evt_Exit, self.menu_close)
        #功能菜单
        functionmenu = wx.Menu()
        self.menu_parallel = functionmenu.Append(ID_PARALLEL,u"压力测试")
        self.Bind(wx.EVT_MENU, self.evt_parallel, self.menu_parallel)
        self.menu_stream = functionmenu.Append(ID_STREAM,u"协议流测试")
        self.Bind(wx.EVT_MENU, self.evt_stream, self.menu_stream)

        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"开始")
        menuBar.Append(functionmenu, u"功能")
        self.SetMenuBar(menuBar)

        # 创建玩家交互控件
        # 系统选择列表
        self.viewField1 = wx.StaticText(self.UserPanel, label=u"系统选择：", pos=(10,20), size=(100, 20))
        self.sysCheckList = wx.Choice(self.UserPanel,pos=(10,50),size=(180,30),choices=self.sysList)
        self.sysCheckList.Bind(wx.EVT_CHOICE,self.evt_sysCheckBox_Choose)
        self.sysCheckList.SetSelection(0)  # 默认选择第1个
        # 协议选择列表
        self.viewField2 = wx.StaticText(self.UserPanel, label=u"协议选择：", pos=(10,100), size=(100, 20))
        self.protoCheckList = wx.Choice(self.UserPanel,pos=(10,120),size=(180,30))
        self.protoCheckList.Bind(wx.EVT_CHOICE,self.evt_protoCheckBox_Choose)
        # 协议输入框
        self.viewField3 = wx.StaticText(self.UserPanel,label=u"输入协议各字段参数：",pos=(200,20),size=(150,20))
        self.textField = wx.TextCtrl(self.UserPanel,pos=(200,50),size=(550,25),style=wx.TE_PROCESS_ENTER)
        # 并发次数选择列表
        choiceList = ["%d" % i for i in range(1,31)]
        self.viewField4 = wx.StaticText(self.UserPanel,label=u"并发发送次数：",pos=(200,90),size=(100,20))
        self.concurrencyCheckList = wx.Choice(self.UserPanel,pos=(300,85),size=(60,25),choices=choiceList)
        self.concurrencyCheckList.SetSelection(0)
        # 发送协议按钮
        self.btn_ck = wx.Button(self.UserPanel, label=u'发送',pos=(670,85),size=(80,30))
        self.Bind(wx.EVT_BUTTON, self.Evt_button_Send, self.btn_ck)
        # 协议说明文本框
        self.viewField5 = wx.StaticText(self.UserPanel, label=u"协议说明：", pos=(200, 130), size=(100, 30))
        self.prototrsform_logger = wx.TextCtrl(self.UserPanel, pos=(200,160), size=(550,220),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)
        #查询结果文本框
        self.viewField6 = wx.StaticText(self.UserPanel, label=u"查询结果：", pos=(400, 395), size=(100, 15),style=wx.ALIGN_LEFT)
        self.checkout_logger = wx.TextCtrl(self.UserPanel, pos=(400,425), size=(350,305),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 协议接收
        self.viewField7 = wx.StaticText(self.UserPanel, label=u"接收消息队列：", pos=(800,20), size=(100, 30))
        # 消息队列文本框
        self.proto_msg_logger = wx.TextCtrl(self.UserPanel, pos=(800,50), size=(380,680),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 清空消息文本
        self.btn_clear_logger = wx.Button(self.UserPanel, label=u'清空消息',pos=(1090,15),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.evt_button_clearLogger,self.btn_clear_logger)

        # 功能区域部分
        # 使用GM功能
        self.viewFieldGM = wx.StaticText(self.UserPanel, label=u"输入GM命令：", pos=(10, 180), size=(100, 20))
        self.textFieldGM = wx.TextCtrl(self.UserPanel,pos=(10,210),size=(170,25),style=wx.TE_PROCESS_ENTER)
        self.btn_sdGM = wx.Button(self.UserPanel, label=u'发送GM',pos=(100,250),size=(80,30))
        self.Bind(wx.EVT_BUTTON, self.evt_button_SendGM, self.btn_sdGM)
        self.btn_GMBox = wx.ToggleButton(self.UserPanel, label=u'<<GM盒子',pos=(10,250),size=(80,30))
        self.Bind(wx.EVT_TOGGLEBUTTON, self.evt_GMBox, self.btn_GMBox)
        # 结果码查询
        self.viewFieldCode = wx.StaticText(self.UserPanel, label=u"输入结果码查询说明：", pos=(10, 290), size=(150, 20))
        self.textFieldCode = wx.TextCtrl(self.UserPanel,pos=(10,320),size=(170,25),style=wx.TE_PROCESS_ENTER)
        self.btn_ckCode = wx.Button(self.UserPanel, label=u'查询', pos=(100, 350), size=(80, 30))
        self.Bind(wx.EVT_BUTTON,self.evt_button_ckCode,self.btn_ckCode)
        self.viewFieldFC = wx.StaticText(self.UserPanel, label=u"查询功能区域", pos=(0, 400), size=(400, 30),style=wx.ALIGN_CENTER)
        fontFC = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.BOLD)
        self.viewFieldFC.SetFont(fontFC)
        # 查询背包道具按钮
        self.btn_lkpbp =  wx.Button(self.UserPanel, label=u'背包', pos=(10, 450), size=(80, 30))
        self.Bind(wx.EVT_BUTTON,self.evt_button_bbget,self.btn_lkpbp)
        # 查询玩家信息按钮
        self.btn_lkppl = wx.Button(self.UserPanel, label=u'玩家信息',pos=(100,450),size=(80,30))
        self.Bind(wx.EVT_BUTTON, self.evt_button_plget, self.btn_lkppl)
        # 查询伙伴列表
        self.btn_lkpptr = wx.Button(self.UserPanel, label=u'伙伴列表',pos=(190,450),size=(80,30))
        self.Bind(wx.EVT_BUTTON, self.evt_button_ptrget, self.btn_lkpptr)
        # 查询法宝列表
        self.btn_lkpmjr = wx.Button(self.UserPanel, label=u'主角列表',pos=(280,450),size=(80,30))
        self.Bind(wx.EVT_BUTTON, self.evt_button_mjrget, self.btn_lkpmjr)
        #################################################################
        # 查询灵宠列表
        self.btn_lkppet = wx.Button(self.UserPanel, label=u'灵宠列表',pos=(10,490),size=(80,30))
        self.Bind(wx.EVT_BUTTON, self.evt_button_petget, self.btn_lkppet)

        #GM盒子，快速GM命令
        self.gmBoxPanel = wx.Panel(self,size=(300,800),pos=(0,0))
        self.gmBoxPanel.Show(False)
        #刷资源
        self.view_ResourceChField1 = wx.StaticText(self.gmBoxPanel,pos=(5,10),size=(100,20),label=u"选择资源:")
        self.view_ResourceChField2 = wx.StaticText(self.gmBoxPanel,pos=(100,10),size=(100,20),label=u"输入数量:")
        gm_ResourceList = [u"灵石",u"玄天晶",u"体力",u"灵符",u"超级灵符",u"竞技场积分"]
        self.gm_ResourceChoice = wx.Choice(self.gmBoxPanel,pos=(5,40),size=(85,30),choices=gm_ResourceList)
        self.gm_ResourceChoice.SetSelection(0)
        self.text_GmRscNum_Input = wx.TextCtrl(self.gmBoxPanel,pos=(100,45),size=(100,20))
        self.text_GmRscNum_Input.SetValue("0")
        self.btn_gmResource = wx.Button(self.gmBoxPanel,pos=(210,20),size=(80,30),label=u"获取资源")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_resource,self.btn_gmResource)
        #系统解锁、模拟五点刷新、清除购买体力次数
        self.btn_gmUnlockall = wx.Button(self.gmBoxPanel,pos=(5,80),size=(80,30),label=u"系统解锁")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_unlock,self.btn_gmUnlockall)
        self.btn_gmRefresh5 = wx.Button(self.gmBoxPanel,pos=(110,80),size=(80,30),label=u"模拟刷新")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_refresh5,self.btn_gmRefresh5)
        self.btn_gmClearBuy = wx.Button(self.gmBoxPanel,pos=(210,80),size=(80,30),label=u"清除体力购买")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_clearbuy,self.btn_gmClearBuy)
        self.view_cut_line1 = wx.StaticText(self.gmBoxPanel,pos=(0,115),size=(300,10),label=u"————————————————————————————————")
        self.view_cut_line1.SetForegroundColour(wx.Colour(255,0,0))
        #刷伙伴
        self.view_PartnerChField1 = wx.StaticText(self.gmBoxPanel,pos=(5,130),size=(100,20),label=u"选择伙伴:")
        self.view_PartnerChField2 = wx.StaticText(self.gmBoxPanel,pos=(100,130),size=(50,20),label=u"星级:")
        self.view_PartnerChField3 = wx.StaticText(self.gmBoxPanel,pos=(150,130),size=(50,20),label=u"等级:")
        gm_PartnerList = [u"全部伙伴"]
        for index in range(4,len(self.partnerList)):
            gm_PartnerList.append(self.partnerList[index][1])
        self.gm_PartnerChoice = wx.Choice(self.gmBoxPanel,pos=(5,160),size=(85,30),choices=gm_PartnerList)
        self.gm_PartnerChoice.SetSelection(0)
        self.text_GmPtrStar_Input = wx.TextCtrl(self.gmBoxPanel,pos=(100,165),size=(45,20))
        self.text_GmPtrStar_Input.SetValue("0")
        self.text_GmPtrLv_Input = wx.TextCtrl(self.gmBoxPanel,pos=(155,165),size=(45,20))
        self.text_GmPtrLv_Input.SetValue("0")
        self.btn_gmPartner = wx.Button(self.gmBoxPanel,pos=(210,145),size=(80,30),label=u"获取伙伴")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_partner,self.btn_gmPartner)
        self.btn_gmdelPartner = wx.Button(self.gmBoxPanel,pos=(5,200),size=(80,30),label=u"清空伙伴")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_delpartner,self.btn_gmdelPartner)
        self.view_cut_line2 = wx.StaticText(self.gmBoxPanel,pos=(0,235),size=(300,10),label=u"————————————————————————————————")
        self.view_cut_line2.SetForegroundColour(wx.Colour(255,0,0))
        #刷主角
        self.view_MajorChField1 = wx.StaticText(self.gmBoxPanel,pos=(5,255),size=(95,20),label=u"选择主角:")
        gm_MajorList = []
        for index in range(4,len(self.majorList)):
            gm_MajorList.append(self.majorList[index][1])
        self.gm_MajorChoice = wx.Choice(self.gmBoxPanel,pos=(100,250),size=(85,30),choices=gm_MajorList)
        self.gm_MajorChoice.SetSelection(0)
        self.btn_gmMajor = wx.Button(self.gmBoxPanel,pos=(210,250),size=(80,30),label=u"获取主角")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_major,self.btn_gmMajor)
        self.view_MajorChField2 = wx.StaticText(self.gmBoxPanel,pos=(5,295),size=(95,20),label=u"输入等级:")
        self.text_GmMjrLv_Input = wx.TextCtrl(self.gmBoxPanel,pos=(100,295),size=(95,20))
        self.text_GmMjrLv_Input.SetValue("0")
        self.btn_gmMjLv = wx.Button(self.gmBoxPanel,pos=(210,290),size=(80,30),label=u"设主角等级")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_majorlv,self.btn_gmMjLv)
        self.view_MajorChField3 = wx.StaticText(self.gmBoxPanel,pos=(5,335),size=(95,20),label=u"输入经验:")
        self.text_GmMjrEx_Input = wx.TextCtrl(self.gmBoxPanel,pos=(100,335),size=(95,20))
        self.text_GmMjrEx_Input.SetValue("0")
        self.btn_gmMjEx = wx.Button(self.gmBoxPanel,pos=(210,330),size=(80,30),label=u"加主角经验")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_majorexp,self.btn_gmMjEx)
        self.view_cut_line3 = wx.StaticText(self.gmBoxPanel,pos=(0,365),size=(300,10),label=u"————————————————————————————————")
        self.view_cut_line3.SetForegroundColour(wx.Colour(255,0,0))
        #刷灵宠
        self.view_PetChField1 = wx.StaticText(self.gmBoxPanel,pos=(5,380),size=(100,20),label=u"选择灵宠:")
        self.view_PetChField2 = wx.StaticText(self.gmBoxPanel,pos=(100,380),size=(100,20),label=u"输入等级:")
        gm_PetList = []
        for index in range(4,len(self.petList)):
            gm_PetList.append(self.petList[index][1])
        self.gm_PetChoice = wx.Choice(self.gmBoxPanel,pos=(5,410),size=(85,30),choices=gm_PetList)
        self.gm_PetChoice.SetSelection(0)
        self.text_GmPetLv_Input = wx.TextCtrl(self.gmBoxPanel,pos=(100,415),size=(100,20))
        self.btn_gmPet = wx.Button(self.gmBoxPanel,pos=(210,395),size=(80,30),label=u"获取灵宠")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_pet,self.btn_gmPet)
        self.btn_gmdelPet = wx.Button(self.gmBoxPanel,pos=(5,450),size=(80,30),label=u"清空灵宠")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_delpet,self.btn_gmdelPet)
        self.view_cut_line4 = wx.StaticText(self.gmBoxPanel,pos=(0,485),size=(300,10),label=u"————————————————————————————————")
        self.view_cut_line4.SetForegroundColour(wx.Colour(255,0,0))
        #刷物品
        self.view_ItemChField1 = wx.StaticText(self.gmBoxPanel,pos=(5,500),size=(100,20),label=u"物品名称或id:")
        self.view_ItemChField2 = wx.StaticText(self.gmBoxPanel,pos=(100,500),size=(100,20),label=u"输入数量:")
        self.text_GmItem_Input = wx.TextCtrl(self.gmBoxPanel,pos=(5,530),size=(80,20))
        self.text_GmItem_Input.SetValue("0")
        self.text_GmItemNum_Input = wx.TextCtrl(self.gmBoxPanel,pos=(100,530),size=(80,20))
        self.text_GmItemNum_Input.SetValue("0")
        self.btn_gmItem = wx.Button(self.gmBoxPanel,pos=(210,515),size=(80,30),label=u"获取道具")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_item,self.btn_gmItem)
        self.view_ItemPlField1 = wx.StaticText(self.gmBoxPanel,pos=(5,560),size=(65,20),label=u"起始id:")
        self.view_ItemPlField2 = wx.StaticText(self.gmBoxPanel,pos=(70,560),size=(65,20),label=u"结束id:")
        self.view_ItemPlField3 = wx.StaticText(self.gmBoxPanel,pos=(140,560),size=(65,20),label=u"数量:")
        self.text_GmItemPls_Input = wx.TextCtrl(self.gmBoxPanel,pos=(5,590),size=(55,20))
        self.text_GmItemPls_Input.SetValue("0")
        self.text_GmItemPle_Input = wx.TextCtrl(self.gmBoxPanel,pos=(70,590),size=(55,20))
        self.text_GmItemPle_Input.SetValue("0")
        self.text_GmItemPln_Input = wx.TextCtrl(self.gmBoxPanel,pos=(140,590),size=(60,20))
        self.text_GmItemPln_Input.SetValue("0")
        self.btn_gmItem = wx.Button(self.gmBoxPanel,pos=(210,575),size=(80,30),label=u"获取批量道具")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_plitem,self.btn_gmItem)
        self.btn_gmdelItem = wx.Button(self.gmBoxPanel,pos=(5,620),size=(80,30),label=u"清空背包")
        self.Bind(wx.EVT_BUTTON,self.evt_GMBox_btn_clearpack,self.btn_gmdelItem)
        self.view_cut_line5 = wx.StaticText(self.gmBoxPanel,pos=(0,655),size=(300,10),label=u"————————————————————————————————")
        self.view_cut_line5.SetForegroundColour(wx.Colour(255,0,0))

        # socekt初始化
        self.login_hosts = self.proto_client.login_getway()
        self.connect = self.proto_client.long_connect(self.login_hosts, self.proto_msg_logger)

    def OnClose(self,event):
        # 关闭方法重定义
        self.connect.shutdown(2)
        self.connect.close()
        event.Skip()

    # 菜单选择事件
    def evt_Exit(self,event):
        # 退出程序
        self.Close(True)

    def evt_register(self,event):
        #注册账号
        self.register_box = Register_DialogBox(self.proto_client,self.connect)
        self.register_box.ShowModal()

    def evt_login(self,event):
        # 登录游戏对话框
        self.login_box = Login_DialogBox(self.proto_client,self.login_state,self.login_accname,self.connect,self.proto_msg_logger)
        self.login_box.ShowModal()
        self.login_state = self.login_box.state
        self.login_accname = self.login_box.accname
        self.connect = self.login_box.connect
        if self.login_state == 0 and self.btn_GMBox.GetValue() is True:
            self.UserPanel.SetPosition((0, 0))
            self.SetSize(size=(1200, 800))
            self.gmBoxPanel.Show(False)
            self.btn_GMBox.SetValue(False)
            self.btn_GMBox.SetLabel(u"<<GM盒子")


    def evt_parallel(self,event):
        #压力测试对话框
        self.parallel_box = Parallel_DialogBox(self.proto_client,self.sysList,self.protoList)
        self.parallel_box.ShowModal()

    def evt_stream(self,event):
         #协议流测试对话框
         self.stream_box = Datch_DialogBox()
         self.stream_box.ShowModal()

    # 列表选择事件
    def evt_sysCheckBox_Choose(self, event):
        # 系统选择
        if self.login_state == 1:
            protolist = []
            sysname = self.sysCheckList.GetStringSelection()
            for key,value in self.protoList.items():
                if sysname == key:
                    protolist = value
                    break
            self.protoCheckList.SetItems(protolist)
            # 默认选中第1个协议，初始化协议选中状态
            self.protoCheckList.SetSelection(0)
            self.protoname = self.protoCheckList.GetStringSelection()
            startprotoname = self.protoCheckList.GetStringSelection()
            transinfo = (self.protoget.getnote(startprotoname))
            self.prototrsform_logger.SetValue(transinfo)
        else:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()
            login_dlg.Destroy()

    def evt_protoCheckBox_Choose(self, event):
        # 协议选择事件
        if self.login_state == 1:
            self.protoname = self.protoCheckList.GetStringSelection()
            transinfo = (self.protoget.getnote(self.protoname))
            self.prototrsform_logger.SetValue(transinfo)
        else:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()
            login_dlg.Destroy()

    # 按钮点击事件
    def Evt_button_Send(self,event):
        # 发送协议按钮点击事件
        if self.login_state == 0:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            self.proto_parm = self.textField.GetValue()
            self.sendtimes = int(self.concurrencyCheckList.GetStringSelection())
            if self.sendtimes == 1:
                # 单条协议发送
                if self.proto_parm == "":
                    self.proto_parm = self.protoname
                else:
                    self.proto_parm = self.protoname + " " + self.proto_parm
                self.socket_com.send_proto(self.connect,self.proto_parm)
            else:
                # 并发协议发送
                if self.proto_parm == "":
                    self.proto_parm = self.protoname
                else:
                    self.proto_parm = self.protoname + " " + self.proto_parm
                pttime = TimeTreatment().getlocaltimestamp() + 1
                for i in range(self.sendtimes):
                    t = threading.Thread(target=self.socket_com.send_proto_repeate, args=(self.connect, self.proto_parm,pttime))
                    t.start()

    def evt_button_SendGM(self, event):
        # 发送GM功能
        if self.login_state == 0:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            gmValue = self.textFieldGM.GetValue()
            if gmValue == "":
                login_dlg = wx.MessageDialog(self, u"不能发送空字符串！", u"提示", wx.OK)
                login_dlg.ShowModal()  # 显示对话框
                login_dlg.Destroy()
            else:
                protoname = u"c2s_world_chat"
                c2s = protoname + u" " + u"\"" +gmValue + u"\""
                self.socket_com.send_proto(self.connect, c2s)
                login_dlg = wx.MessageDialog(self, u"发送成功！", u"提示", wx.OK)
                login_dlg.ShowModal()  # 显示对话框
                login_dlg.Destroy()

    def evt_button_ckCode(self, event):
        # 协议码查询
        ck_code = self.textFieldCode.GetValue()
        if ck_code =="":
            code_dlg = wx.MessageDialog(self, u"不能输入空编码！", u"提示", wx.OK)
            code_dlg.ShowModal()  # 显示对话框
            code_dlg.Destroy()
        else:
            transcode = Transcode()
            try:
                code = int(ck_code)
                result = transcode.transcode(code)
                code_dlg = wx.MessageDialog(self, result, u"提示", wx.OK)
                code_dlg.ShowModal()  # 显示对话框
                code_dlg.Destroy()
            except IOError:
                code_dlg = wx.MessageDialog(self, u"没有找到配置文件！", u"提示", wx.OK)
                code_dlg.ShowModal()  # 显示对话框
                code_dlg.Destroy()
            except:
                code_dlg = wx.MessageDialog(self, u"输入编码格式错误！", u"提示", wx.OK)
                code_dlg.ShowModal()  # 显示对话框
                code_dlg.Destroy()

    def evt_button_bbget(self,event):
        #查询玩家中背包数据事件
        if self.login_state == 0:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            proto = "c2s_goods_list"
            logger = u"道具名       道具id        UID       数量\n"
            self.socket_com.send_proto(self.connect,proto)
            time.sleep(0.1)
            pbdatas = Socket_Com.protodata
            pbdatas.reverse()
            print pbdatas
            for proto in pbdatas:
                if proto[0] == "s2c_goods_list":
                    data = proto[1]
                    break
            if len(data) > 0:
                for item in data:
                    for each in self.itemList:
                        if each[0] == unicode(item[0]):
                            logger += each[1]
                            break
                    logger += u"      %s      %s      %s\n"%(item[0],item[1],item[2])
                self.checkout_logger.SetValue(logger)
            else:
                self.checkout_logger.SetValue(u"背包是空的")

    def evt_button_plget(self,event):
        #查询玩家信息事件
        logger = u""
        if self.login_state == 0:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            proto = "c2s_get_player_info"
            self.socket_com.send_proto(self.connect,proto)
            time.sleep(0.1)
            pbdatas = Socket_Com.protodata
            pbdatas.reverse()
            for proto in pbdatas:
                if proto[0] == "s2c_get_player_info":
                    data = proto[1]
                    break
            for index in range(len(data)):
                if index == 0:
                    logger += u"玩家ID:    "
                elif index == 1:
                    logger += u"玩家昵称:   "
                elif index == 2:
                    logger += u"拥有灵石:   "
                elif index == 3:
                    logger += u"拥有玄天晶:   "
                elif index == 4:
                    logger += u"拥有体力:   "
                elif index == 5:
                    logger += u"主角ID:   "
                elif index == 6:
                    logger += u"主角等级:   "
                elif index == 7:
                    logger += u"当前经验:   "
                if index < 8:
                    if isinstance(data[index],unicode) is True:
                        logger += data[index] + u"\n"
                    else:
                        logger += str(data[index]) + u"\n"
            self.checkout_logger.SetValue(logger)

    def evt_button_ptrget(self,event):
        #查询玩家伙伴列表事件
        logger = u""
        if self.login_state == 0:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            proto = "c2s_get_partner_list"
            logger = u"伙伴名            UID            星级      等级\n"
            self.socket_com.send_proto(self.connect,proto)
            time.sleep(0.1)
            pbdatas = Socket_Com.protodata
            pbdatas.reverse()
            for proto in pbdatas:
                if proto[0] == "s2c_get_partner_list":
                    data = proto[1]
                    break
            if len(data) > 0:
                for partner in data:
                    for each in self.partnerList:
                        if each[0] == unicode(partner[0]):
                            logger += each[1]
                            break
                    logger += u"        %s        %s      %s\n" % (partner[1], partner[2], partner[3])
                    self.checkout_logger.SetValue(logger)
            else:
                self.checkout_logger.SetValue(u"伙伴为空")

    def evt_button_mjrget(self,event):
        #查询玩家主角列表事件
        logger = u""
        if self.login_state == 0:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            proto = "c2s_get_major_list"
            logger = u"主角名      UID\n"
            self.socket_com.send_proto(self.connect,proto)
            time.sleep(0.1)
            pbdatas = Socket_Com.protodata
            pbdatas.reverse()
            for proto in pbdatas:
                if proto[0] == "s2c_get_major_list":
                    data = proto[1]
                    break
            if len(data) > 0:
                for major in data:
                    for each in self.majorList:
                        if each[0] == unicode(major[0]):
                            logger += each[1]
                            break
                    logger += u"        %s\n" % major[0]
                    self.checkout_logger.SetValue(logger)
            else:
                self.checkout_logger.SetValue(u"主角为空")

    def evt_button_petget(self,event):
        #查询玩家灵宠列表事件
        logger = u""
        if self.login_state == 0:
            login_dlg = wx.MessageDialog(self, u"请先登录账号！", u"提示", wx.OK)
            login_dlg.ShowModal()  # 显示对话框
            login_dlg.Destroy()
        else:
            proto = "c2s_get_pet_list"
            logger = u"灵宠名      UID      等级\n"
            self.socket_com.send_proto(self.connect,proto)
            time.sleep(0.1)
            pbdatas = Socket_Com.protodata
            pbdatas.reverse()
            for proto in pbdatas:
                if proto[0] == "s2c_get_pet_list":
                    data = proto[1]
                    break
            if len(data) > 0:
                for pet in data:
                    for each in self.petList:
                        if each[0] == unicode(pet[0]):
                            logger += each[1]
                            break
                    logger += u"      %s      %s\n" %(pet[1],pet[2])
                    self.checkout_logger.SetValue(logger)
            else:
                self.checkout_logger.SetValue(u"主角为空")

    def evt_button_clearLogger(self,event):
        # 清空协议文本框内容
        self.proto_msg_logger.Clear()

    def evt_GMBox(self, event):
        #GM盒子开关
        if self.login_state:
            state = event.GetEventObject().GetValue()
            if state is False:
                self.UserPanel.SetPosition((0,0))
                self.SetSize(size=(1200,800))
                self.gmBoxPanel.Show(False)
                # self.SetMaxSize((1200, 800))
                # self.SetMinSize((1200, 800))
                self.btn_GMBox.SetLabel(u"<<GM盒子")
            else:
                # self.SetMaxSize((1500, 800))
                # self.SetMinSize((1500, 800))
                self.SetSize(size=(1500,800))
                self.UserPanel.SetPosition((300,0))
                self.gmBoxPanel.Show(True)
                self.btn_GMBox.SetLabel(u">>GM盒子")
        else:
            event.GetEventObject().SetValue(False)
            dlg = wx.MessageDialog(self, u"请先登录账号！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()

    def evt_GMBox_btn_resource(self ,event):
        #GM刷资源事件
        resC = self.gm_ResourceChoice.GetStringSelection()
        try:
            resNum = int(self.text_GmRscNum_Input.GetValue())
            fl = True
        except:
            fl = False
        if fl is False:
            dlg = wx.MessageDialog(self, u"输入数量只能为整数且不能为空值！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            #分段处理不同的资源gm
            if resC == u"灵石":
                gmValue = u"-加灵石 " + str(resNum)
            elif resC == u"玄天晶":
                gmValue = u"-加元宝 " + str(resNum)
            elif resC == u"体力":
                gmValue = u"-设体力 " + str(resNum)
            elif resC == u"灵符":
                gmValue = u"-加灵符 " + str(resNum)
            elif resC == u"超级灵符":
                gmValue = u"-加超级灵符 " + str(resNum)
            elif resC == u"竞技场积分":
                gmValue = u"-设积分 100 " + str(resNum)
            self.send_GM(gmValue)

    def evt_GMBox_btn_unlock(self ,event):
        #系统激活事件
        gmValue = u"-激活所有系统"
        self.send_GM(gmValue)

    def evt_GMBox_btn_refresh5(self ,event):
        #模拟5点刷新事件
        gmValue = u"-模拟五点刷新"
        self.send_GM(gmValue)

    def evt_GMBox_btn_clearbuy(self ,event):
        #清除体力购买次数事件
        gmValue = u"-清除体力购买次数"
        self.send_GM(gmValue)

    def evt_GMBox_btn_partner(self, event):
        #GM刷伙伴事件
        partner_id = None
        partner = self.gm_PartnerChoice.GetStringSelection()
        try:
            star = int(self.text_GmPtrStar_Input.GetValue())
            lv = int(self.text_GmPtrLv_Input.GetValue())
            fl = True
        except:
            fl = False
        if fl is False:
            dlg = wx.MessageDialog(self, u"伙伴星级与伙伴等级只能为整数且不能为空值！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            if partner == u"全部伙伴":
                gmValue = u"-全部伙伴 " + str(star) + " " + str(lv)
            else:
                for cfg_ptr in self.partnerList:
                    if partner == cfg_ptr[1]:
                        partner_id = cfg_ptr[0]
                        break
                gmValue = u"-加伙伴 " + partner_id + " " + str(star) + " " + str(lv)
            self.send_GM(gmValue)

    def evt_GMBox_btn_delpartner(self ,event):
        #清空伙伴事件
        gmValue = u"-删除所有伙伴"
        self.send_GM(gmValue)

    def evt_GMBox_btn_major(self, event):
        #GM刷主角事件
        major_id = None
        major = self.gm_MajorChoice.GetStringSelection()
        for cfg_mjr in self.majorList:
            if major == cfg_mjr[1]:
                major_id = cfg_mjr[0]
                break
        gmValue = u"-加主角 " + major_id
        self.send_GM(gmValue)

    def evt_GMBox_btn_majorlv(self, event):
        #GM刷主角等级事件
        try:
            lv = int(self.text_GmMjrLv_Input.GetValue())
            fl = True
        except:
            fl = False
        if fl is False:
            dlg = wx.MessageDialog(self, u"输入等级只能为整数且不能为空值！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            gmValue = u"-设等级 " + str(lv)
            self.send_GM(gmValue)

    def evt_GMBox_btn_majorexp(self, event):
        #GM刷主角经验事件
        try:
            exp = int(self.text_GmMjrEx_Input.GetValue())
            fl = True
        except:
            fl = False
        if fl is False:
            dlg = wx.MessageDialog(self, u"输入经验只能为整数且不能为空值！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            gmValue = u"-加经验 " + str(exp)
            self.send_GM(gmValue)

    def evt_GMBox_btn_pet(self, event):
        #GM刷灵宠事件
        pet_id = None
        pet = self.gm_PetChoice.GetStringSelection()
        try:
            lv = int(self.text_GmPetLv_Input.GetValue())
            fl = True
        except:
            fl = False
        if fl is False:
            dlg = wx.MessageDialog(self, u"灵宠等级只能为整数且不能为空值！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            for cfg_pet in self.petList:
                if pet == cfg_pet[1]:
                    pet_id = cfg_pet[0]
                    break
            gmValue = u"-加灵宠 " + pet_id + " " + str(lv)
            self.send_GM(gmValue)

    def evt_GMBox_btn_delpet(self ,event):
        #清空灵宠事件
        gmValue = u"-清空灵宠"
        self.send_GM(gmValue)

    def evt_GMBox_btn_item(self, event):
        #GM刷物品事件
        item_id = None
        item = self.text_GmItem_Input.GetValue()
        try:
            num = int(self.text_GmItemNum_Input.GetValue())
            fl = True
        except:
            fl = False
        if fl is False:
            dlg = wx.MessageDialog(self, u"道具数量只能为整数且不能为空值！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            for cfg_item in self.itemList:
                if item == cfg_item[0] or item == cfg_item[1]:
                    item_id = cfg_item[0]
                    break
            if item_id is None:
                login_dlg = wx.MessageDialog(self, u"没有找到指定的道具！", u"警告", wx.OK)
                login_dlg.ShowModal()  # 显示对话框
                login_dlg.Destroy()
            else:
                gmValue = u"-加物品 " + item_id + " " + str(num)
                self.send_GM(gmValue)

    def evt_GMBox_btn_plitem(self, event):
        #GM批量刷物品事件
        item_id = None
        try:
            id_1 = int(self.text_GmItemPls_Input.GetValue())
            id_2 = int(self.text_GmItemPle_Input.GetValue())
            num = int(self.text_GmItemPln_Input.GetValue())
            fl = True
        except:
            fl = False
        if fl is False:
            dlg = wx.MessageDialog(self, u"道具id与道具数量只能为整数且不能为空值！", u"警告", wx.OK)
            dlg.ShowModal()  # 显示对话框
            dlg.Destroy()
        else:
            if id_1 > id_2:
                dlg = wx.MessageDialog(self, u"起始道具ID不能在结束道具ID之后！", u"警告", wx.OK)
                dlg.ShowModal()  # 显示对话框
                dlg.Destroy()
            else:
                gmValue = u"-加物品 " + str(id_1) + " " + str(id_2) + " " + str(num)
                self.send_GM(gmValue)

    def evt_GMBox_btn_clearpack(self ,event):
        #清空背包事件
        gmValue = u"-清空背包"
        self.send_GM(gmValue)

    def send_GM(self, gmValue):
        #发送指定GM通用接口
        protoname = "c2s_world_chat"
        c2s = protoname + " " + "\"" +gmValue + "\""
        self.socket_com.send_proto(self.connect, c2s)
        dlg = wx.MessageDialog(self, u"GM发送成功！", u"提示", wx.OK)
        dlg.ShowModal()  # 显示对话框
        dlg.Destroy()

class App(wx.App):

    def OnInit(self):
        self.frame = Proto_Window(parent=None, title=u'协议测试')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()