# -*- coding: utf-8 -*-
"""
灵剑山的协议
"""

import time,requests,json,struct,sys,os,socket
import protofile.rpc_pb2 as rpc_pb2
from lib.proto.proto_base import *
import xlrd
import Protounpack
import Protopack
from pypinyin import lazy_pinyin
from protofile.accname_pb2 import *
from protofile.achieve_pb2 import *
from protofile.active_pb2 import *
from protofile.arena_pb2 import *
from protofile.chat_pb2 import *
from protofile.compose_pb2 import *
from protofile.draw_pb2 import *
from protofile.dungeon_pb2 import *
from protofile.exp_train_pb2 import *
from protofile.friend_pb2 import *
from protofile.goods_pb2 import *
from protofile.guide_pb2 import *
from protofile.mail_pb2 import *
from protofile.major_pb2 import *
from protofile.mcity_pb2 import *
from protofile.partner_pb2 import *
from protofile.pet_pb2 import *
from protofile.player_pb2 import *
from protofile.pve_pb2 import *
from protofile.pvp_global_pb2 import *
from protofile.pvp_pb2 import *
from protofile.realtime_PVP_pb2 import *
from protofile.shop_pb2 import *
from protofile.sign_pb2 import *
from protofile.task_pb2 import *
from protofile.trial_pb2 import *
from protofile.wonderland_pb2 import *

def rpc_serialize(func, after_clear_params_list):
    """
    序列化协议成二进制
    :param func: 
    :param after_clear_params_list: 
    :return: 
    """
    manual_serialize = False
    for each_param in after_clear_params_list:
        if isinstance(each_param, list):
            manual_serialize = True
            break
    if manual_serialize:
        proto_id = self.find_proto_id(func)
        proto_id_hex_str = int2varint(proto_id)
        param_bin = ''
        for index, each in enumerate(after_clear_params_list):
            index_str = bin(index + 1).split('b')[1]
            if isinstance(each, int):
                int_str = int2bytestr(each, index_str)
                param_bin += int_str
            if isinstance(each, unicode):
                uni_str = uni2bytestr(each, index_str)
                param_bin += uni_str
            if isinstance(each, float):
                float_str = float2bytestr(each, index_str)
                param_bin += float_str
            # 新加的参数会被转换成list
            if isinstance(each, list):
                each_value = each[0]
                if isinstance(each_value, int):
                    int_str = int2bytestr(each_value, index_str)
                    param_bin += int_str
                if isinstance(each_value, unicode):
                    uni_str = uni2bytestr(each_value, index_str)
                    param_bin += uni_str
                if isinstance(each_value, float):
                    float_str = float2bytestr(each, index_str)
                    param_bin += float_str
        param_bin_len = strlen(param_bin)
        param_bin = param_bin_len + param_bin
        rpcc2s_str = r'\x08\x01\x10%s\x1a%s' % (proto_id_hex_str, param_bin)
        rpcc2s = eval("'" + rpcc2s_str + "'")
    else:
        protofunc = getattr(Protopack.C2S_PROTO(), func)
        if after_clear_params_list:
            c2s = protofunc(after_clear_params_list)
        else:
            c2s = protofunc()
        proto_name = c2s.DESCRIPTOR.name
        c2s_bytes = c2s.SerializeToString()
        rpc = rpc_pb2.c2senvelope()
        rpc.correlation_id = 1
        # 通过协议名查询id
        proto_id = find_proto_id(proto_name)
        rpc.service_no = proto_id
        rpc.payload = c2s_bytes
        rpcc2s = rpc.SerializeToString()
    return rpcc2s


def find_proto_id(proto_name):
    """
    通过协议名查协议ID
    :param proto_name: 
    :return: 
    """
    for each in rpc_pb2._SERVICENO.values:
        if each.name == proto_name:
            return each.number
    else:
        raise BaseException("cannot find s2c proto id, maybe new add")


def find_proto_name(proto_id):
    """
    通过协议ID查协议名
    :param proto_id: 
    :return: 
    """
    for each in rpc_pb2._SERVICENO.values:
        if each.number == proto_id:
            return each.name
    else:
        raise BaseException("cannot find s2c proto name, maybe new add")


def encapsulated_headers(c2s):
    """
    包头封装，加入body长度
    :param:c2s:协议体内容
    :return:整包内容，包括协议体长度与协议体内容
    """
    lenth = len(c2s)
    btlth = struct.pack(">I", lenth)
    return btlth + c2s


def analysis_headers(msg):
    """
    包头解析，获取协议体长度
    :param:msg:包头数据
    :return:协议体长度
    """
    msg_str = bytes(msg)
    lenth = struct.unpack(">I", msg_str)[0]
    return lenth

def get_recv_msg(a_socket):
    """
    获取返回数据的二进制
    :param a_socket: 
    :return: msg
    """
    try:
        revlmsg = a_socket.recv(4)
        if revlmsg:
            total = struct.unpack_from(">I", revlmsg)[0]
        view = memoryview(bytearray(total))
        next_offset = 0
        while total - next_offset > 0:
            recv_size = a_socket.recv_into(view[next_offset:], total - next_offset)
            next_offset += recv_size
        return view.tobytes()
    except socket.timeout:
        pass
    except BaseException as e:
        print "Link Disconnected! Because %s" % e
        return False


def get_recv_data_from_msg(msg):
    """
    反序列化接受到的消息,返回协议名和协议体
    :param msg: 
    :return: 
    """
    # 实例化rpc
    s2crpc = rpc_pb2.s2cenvelope()
    # 反序列化rpc
    s2crpc.ParseFromString(msg)
    # 返回的协议id
    protoid = s2crpc.service_no
    # 返回的协议数据
    protodata = s2crpc.payload
    # 通过id反查协议名
    s2cname = find_proto_name(protoid)
    # 实例化对应的协议
    s2cproto = eval(s2cname)()
    # 反序列化协议
    s2cproto.ParseFromString(protodata)
    return [s2cname, s2cproto]


def get_dict_from_data(s2cproto):
    # 用json格式打印协议
    s2c_dict = pb2dict(s2cproto)
    return s2c_dict


def get_json_from_data(s2cproto):
    # 用json格式打印协议
    s2c_json = pb2json(s2cproto)
    return s2c_json


def get_need_dict_from_data(s2cname, s2cproto):
    # 提取协议中需要的数据
    try:
        s2clist = getattr(Protounpack.S2C_PROTO(), s2cname)(s2cproto)
        s2cdict = {s2cname: s2clist}
    except AttributeError:
        s2cdict = {}
    return s2cdict


def get_platform_verify(userdata):
    # 登录与注册前先做平台验证，然后进行数据处理
    # 传入的数据是一个预定义好的字符串：
    #   登录：协议号+空格+账号
    #   注册：协议号+空格+注册账号+注册昵称
    if userdata.find('c2s_login') > -1:
        nowtime = getlocaltimestamp()
        account = userdata.split(" ")[1].split("'")[1]
        data = {"channel": "TWGG", "client": "PC", "deviceId": "198bd4cc5ec842ad06dfc3d504adf73a", "version": 1,
                "signType": "MD5", "account": account, "password": 111111, "timestamp": nowtime}
        verification = get_platform_response(data)
        userdata = "c2s_login" + " '" + verification['content'][
            'accessToken'] + "'" + " 5555" + " 'TWGG'" + " '198bd4cc5ec842ad06dfc3d504adf73a'" + " 'PC'"
    elif userdata.find('c2s_register') > -1:
        nowtime = getlocaltimestamp()
        account = userdata.split(" ")[1].split("'")[1]
        data = {"channel": "TWGG", "client": "PC", "deviceId": "198bd4cc5ec842ad06dfc3d504adf73a", "version": 1,
                "signType": "MD5", "account": account, "password": 111111, "timestamp": nowtime}
        verification = get_platform_response(data)
        userdata = "c2s_register" + " '" + verification['content']['accessToken'] + "'" \
                   + " '" + userdata.split(" ")[2].split("'")[1] + "'"
    return userdata


def get_platform_response(data):
    #向平台申请验证数据，登录注册前必须请求
    #返回一个参数字典
    url = 'http://192.168.1.119:9006/user/loginOrRegister'
    request = requests.post(url=url,data=data)
    response = json.loads(request.text)
    return response


def getlocaltimestamp():
    """获取本地时间戳
    :param:
    :return:timeStamp
    """
    timeArray = time.localtime(time.time())
    timeStamp = int(time.mktime(timeArray))
    return timeStamp


def getlocaltime():
    """
    获取本地时间
    :param:
    :return:timeStr
    """
    nowtime =time.localtime(time.time())
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", nowtime).split(" ")[1]
    return timeStr


def get_serverlist():
    #获取服务器列表，返回一个服务器信息字典(type:服务器类型，list：服务器列表)
    request = requests.get('http://192.168.1.184/get_server_list.php')
    serverlist = request.json()
    return serverlist


def acc_register(accname, nickname):
    data_register = "c2s_register" + " '" + accname + "'" + " '" + nickname + "'"
    new_data_regisiter = get_platform_verify(data_register)
    return new_data_regisiter

def acc_login(accname):
    data_login = "c2s_login" + " '" + accname + "'"
    new_data_login = get_platform_verify(data_login)
    return new_data_login

def check_acc_register_dict(proto_dict):
    if proto_dict.get('code') == 1005:
        regist_state = False
        regist_info = u'玩家已经注册'
    elif proto_dict.get('code') == 1:
        regist_state = True
        regist_info = u'注册成功'
    elif proto_dict.get('code') == 1006:
        regist_state = False
        regist_info = u'玩家名已经占用'
    elif proto_dict.get('code') == 1001:
        regist_state = False
        regist_info = u'玩家名含有敏感字符'
    elif proto_dict.get('code') == 1007:
        regist_state = False
        regist_info = u'玩家名只能是1-6个汉字'
    elif proto_dict.get('code') == 1008:
        regist_state = False
        regist_info = u'玩家名含有非法字符'
    else:
        regist_state = False
        regist_info = u'未知原因'
    return regist_state, regist_info

def check_acc_login_dict(proto_dict):
    if proto_dict.get('code') == 1002:
        regist_state = False
        regist_info = u'玩家不存在'
    elif proto_dict.get('code') == 1:
        regist_state = True
        regist_info = u'登录成功'
    elif proto_dict.get('code') == 1003:
        regist_state = False
        regist_info = u'您已被封号，请联系管理员'
    elif proto_dict.get('code') == 1004:
        regist_state = False
        regist_info = u'登录超时'
    elif proto_dict.get('code') == 1012:
        regist_state = False
        regist_info = u'网络异常，请重试'
    elif proto_dict.get('code') == 1008:
        regist_state = False
        regist_info = u'玩家名含有非法字符'
    else:
        regist_state = False
        regist_info = u'未知原因'
    return regist_state, regist_info

def get_host_by_proto():
    """
    获取请求网关的协议名
    :return: 
    """
    data = 'c2s_get_login_host'
    return data

def get_host_by_dict(proto_dict):
    """
    通过返回的协议获取需要的网关ip和端口号
    :param proto_dict: 
    :return: 
    """
    ip = str(proto_dict['ip'])
    port = proto_dict['port']
    return [ip, port]

def player_name_c2s_proto():
    """
    获取玩家昵称的协议名
    :return: 
    """
    data = 'c2s_get_player_info'
    return data

def player_name_s2c_proto():
    """
    获取玩家昵称的协议名
    :return: 
    """
    data = 's2c_get_player_info'
    return data

def get_player_name(s2c_list):
    """
    从提取的列表中选出玩家昵称
    :param s2c_list: 
    :return: 
    """
    return s2c_list[1]

systemdict = {u"登录": 'C2S_ACCNAME', u"成就": 'C2S_ACHIEVE', u"活动": 'C2S_ACTIVE',
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

def get_system_list():
    """
    获取系统列表
    :return: 
    """
    system_list = systemdict.keys()
    # 按首字母拼音排序
    shouzi_list = [lazy_pinyin(each)[0] for each in system_list]
    sort_tuple = sorted(zip(shouzi_list, system_list))
    system_tuple = zip(*sort_tuple)[1]
    return list(system_tuple)

def get_protoname_list(system_name):
    """
    获取协议名称的列表
    :param system_name: 
    :return: 
    """
    protodict = {}
    for each in systemdict:
        funclist = dir(getattr(Protopack, systemdict[each]))
        funclist.remove('__doc__')
        funclist.remove('__module__')
        protodict.setdefault(each, funclist)
    return protodict.get(system_name)

def get_note_info(protoname):
    """
    获取协议注释
    :param protoname: 
    :return: 
    """
    note = getattr(Protopack.C2S_PROTO, protoname).__doc__
    note = note.replace('        :', '')
    note = note.replace('        ', '')
    # 参数说明
    param_desc = (u'每个参数之间以空格分隔\r\n'
                  u'int参数填写整数，str参数填写字符串，但也允许乱填类型（支持整数、字符串、浮点数）\r\n'
                  u'如果想新加参数，需要在参数前加上$符号，例如$123、$"abc"（支持整数、字符串、浮点数）\r\n'
                  u'如果想不填某参数，需要填入None作为代替\r\n'
                  u'如果想不填所有参数，可以不填直接发送\r\n'
                  u'\r\n'
                  u'具体参数说明：\r\n')
    return param_desc + note.decode('utf8')

def get_code_info(code):
    """
    获取结果码
    :param code: 
    :return: 
    """
    path = os.path.join(os.path.dirname(__file__), 'config', 'error_code.proto')
    with open(path, 'r') as f:
        for each in f.readlines():
            each = each.replace(' ', '')
            p = r'=%s;' % code
            if each.find(p) > -1:
                return u"结果码意思：" + each.split(r'//')[1].decode('utf-8')
        else:
            return u'没有找到对应的结果码'

def trans_gm(gm):
    """
    将gm名称转换成协议参数
    :param gm: 
    :return: 
    """
    return 'c2s_world_chat "%s"' % gm

query_list = [{'id': 1, 'name': u"背包", 'c2s': 'c2s_goods_list', 's2c': 's2c_goods_list'},
              {'id': 2, 'name': u"玩家", 'c2s': 'c2s_get_player_info', 's2c': 's2c_get_player_info'},
              {'id': 3, 'name': u"伙伴", 'c2s': 'c2s_get_partner_list', 's2c': 's2c_get_partner_list'},
              {'id': 4, 'name': u"灵宠", 'c2s': 'c2s_get_pet_list', 's2c': 's2c_get_pet_list'},
              {'id': 5, 'name': u"主角", 'c2s': 'c2s_get_major_list', 's2c': 's2c_get_major_list'}]

def get_query_list():
    """
    获取查询功能列表
    :return: 
    """
    return query_list


def get_detail_c2s(fuc):
    """
    获取查询功能的协议名
    :param fuc: 
    :return: 
    """
    for query in query_list:
        if query.get('id') == int(fuc):
            return query.get('c2s')


def get_detail_s2c(fuc):
    """
    获取查询功能的协议名
    :param fuc: 
    :return: 
    """
    for query in query_list:
        if query.get('id') == int(fuc):
            return query.get('s2c')


def get_dict_from_excel(xlsName, sheet_index=0):
    """
    从Excel中获取内容列表
    :file_path: 文件名称
    :return: list, 例如[{u'time': u'', u'id': 1.0, u'param': u'c2s_register', u'result': u''}]
    """
    file_path = os.path.join(os.path.dirname(__file__), 'config', xlsName)
    file_normpath = os.path.normpath(file_path)
    bk = xlrd.open_workbook(file_normpath)
    sh = bk.sheet_by_index(sheet_index)
    info_list = []
    for i in xrange(4, sh.nrows):
        info_dict = {}
        for col in xrange(0, sh.ncols):
            key_name = sh.cell_value(0, col)
            value = sh.cell_value(i, col)
            info_dict[key_name] = value
        info_list.append(info_dict)
    return info_list

def trans_detail(detail_dict):
    s2c_name = detail_dict.keys()[0]
    # 背包协议
    if s2c_name == query_list[0]['s2c']:
        table = u'<table>'
        title = u'<tr><th>道具名              </th><th>道具ID      </th><th>UID      </th><th>数量</th></tr>'
        detail_info = table + title
        for detail in detail_dict[s2c_name]:
            goods_list = get_dict_from_excel("Goods.xlsx")
            for goods in goods_list:
                if detail[0] == int(goods['goods_id']):
                    djname = goods['goods_name']
                    break
            djid = detail[0]
            djuid = detail[1]
            djnum = detail[2]
            info = u'<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (djname, djid, djuid, djnum)
            detail_info += info
        table_end = u'</table>'
        detail_info += table_end
        return detail_info
    # 玩家协议
    elif s2c_name == query_list[1]['s2c']:
        table = u'<table>'
        title = u'<tr><th>类别              </th><th>内容      </th></tr>'
        detail_info = table + title
        category = [u'玩家ID', u'玩家昵称', u'拥有灵石', u'拥有玄天晶', u'拥有体力', u'主角ID', u'主角等级', u'当前经验']
        for detail, category in zip(detail_dict[s2c_name], category):
            info = u'<tr><td>%s</td><td>%s</td></tr>'%(category, detail)
            detail_info += info
        table_end = u'</table>'
        detail_info += table_end
        return detail_info
    # 伙伴协议
    elif s2c_name == query_list[2]['s2c']:
        table = u'<table>'
        title = u'<tr><th>伙伴名称           </th><th>伙伴           </th><th>伙伴的UID                     </th><th>星级    </th><th>等级</th></tr>'
        detail_info = table + title
        for detail in detail_dict[s2c_name]:
            partnerid = detail[0]
            UID = detail[1]
            star = detail[2]
            lv = detail[3]
            partner_list = get_dict_from_excel("Partner.xlsx")
            for partner in partner_list:
                if detail[0] == int(partner['partner_id']):
                    name = partner['name']
                    break
            info = u'<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (name, partnerid, UID, star, lv)
            detail_info += info
        table_end = u'</table>'
        detail_info += table_end
        return detail_info
    # 灵宠协议
    elif s2c_name == query_list[3]['s2c']:
        table = u'<table>'
        title = u'<tr><th>灵宠           </th><th>灵宠的UID       </th><th>等级</th></tr>'
        detail_info = table + title
        for detail in detail_dict[s2c_name]:
            petid = detail[0]
            UID = detail[1]
            lv = detail[2]
            info = u'<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (petid, UID, lv)
            detail_info += info
        table_end = u'</table>'
        detail_info += table_end
        return detail_info
    # 主角协议
    elif s2c_name == query_list[4]['s2c']:
        table = u'<table>'
        title = u'<tr><th>主角名           </th><th>主角的UID       </th></tr>'
        detail_info = table + title
        for detail in detail_dict[s2c_name]:
            majorid = detail[0]
            major_list = get_dict_from_excel("Major.xlsx")
            for major in major_list:
                if detail[0] == int(major['major_id']):
                    majorname = major['name']
                    break
            info = u'<tr><td>%s</td><td>%s</td></tr>' % (majorname, majorid)
            detail_info += info
        table_end = u'</table>'
        detail_info += table_end
        return detail_info
    else:
        return u"尚未处理此查询数据"


