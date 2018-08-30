# -*- coding:utf8 -*-

from Protopack import *
from pypinyin import lazy_pinyin

class Protoget():
    def __init__(self):
        self.systemdict = {u"登录": 'C2S_ACCNAME', u"成就": 'C2S_ACHIEVE', u"活动": 'C2S_ACTIVE',
                           u"竞技场": 'C2S_ARENA', u"聊天": 'C2S_CHAT',
                           u"合成": 'C2S_COMPOSE', u"抽卡": 'C2S_DRAW',
                           u"三千世界": 'C2S_DUNGEON', u"练功房": 'C2S_EXP_TRAIN',
                           u"好友": 'C2S_FRIEND', u"背包": 'C2S_GOODS',
                           u"引导": 'C2S_GUDIE', u"邮件": 'C2S_MAIL',
                           u"主角": 'C2S_MAJOR', u"主城": 'C2S_MCITY',
                           u"伙伴": 'C2S_PARTNER', u"灵宠": 'C2S_PET',
                           u"玩家": 'C2S_PLAYER', u"历练": 'C2S_PVE',
                           u"战斗": 'C2S_PVP', u"全服对战": 'C2S_PVP_GOLOBAL',
                           u"群仙大会": 'C2S_REALTIME_PVP', u"商店": 'C2S_SHOP',
                           u"签到": 'C2S_SIGN', u"任务": 'C2S_TASK',
                           u"试炼": 'C2S_TRIAL', u"秘境": 'C2S_WONDERLAND', }

    def getsystem(self):
        """
        获取系统名称列表
        """
        iterkeys = self.systemdict.iterkeys()
        klist = list(iterkeys)
        # 按首字母拼音排序
        plist = [lazy_pinyin(each)[0] for each in klist]
        pzip = sorted(zip(plist, klist))
        ktuple = zip(*pzip)[1]
        return list(ktuple)

    def getproto(self):
        """
        获取协议系统-协议名称字典
        """
        protodict = {}
        for each in self.systemdict:
            funclist = dir(eval(self.systemdict[each]))
            funclist.remove('__doc__')
            funclist.remove('__module__')
            protodict.setdefault(each, funclist)
        return protodict

    def getnote(self, protoname):
        """
        根据协议名获得注释文本
        """
        note = getattr(C2S_PROTO, protoname).__doc__
        note = note.replace('        :', '')
        note = note.replace('        ', '')
        # 新增参数说明
        param_desc = (u'每个参数之间以空格分隔\r\n'
                      u'int参数填写整数，str参数填写字符串，但也允许乱填类型（支持整数、字符串、浮点数）\r\n'
                      u'如果想新加参数，需要在参数前加上$符号，例如$123、$"abc"（支持整数、字符串、浮点数）\r\n'
                      u'如果想不填某参数，需要填入None作为代替\r\n'
                      u'如果想不填所有参数，可以不填直接发送\r\n'
                      u'\r\n'
                      u'具体参数说明：\r\n')
        return param_desc + note.decode('utf8')

