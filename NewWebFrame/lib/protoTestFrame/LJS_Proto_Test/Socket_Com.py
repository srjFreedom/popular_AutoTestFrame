# -*- coding:utf8 -*-

import socket
import threading
import wx
from Protopack import *
import pbjson
import Protounpack
import struct
from Protoencoder import *
import protofile.rpc_pb2 as rpc_pb2
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

import time
lock = threading.RLock()

# 协议体缓存数据，用于其他显示或比对
# 该缓存数据只储存最新5条协议
protodata = []


class SocketThread(threading.Thread):

    def __init__(self, func, args=()):
        super(SocketThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None

class TimeTreatment():

    def getlocaltimestamp(self):
        """获取本地时间戳
        :param:
        :return:timeStamp
        """
        timeArray = time.localtime(time.time())
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    def getlocaltime(self):
        """
        获取本地时间
        :param:
        :return:timeStr
        """
        nowtime =time.localtime(time.time())
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", nowtime).split(" ")[1]
        return timeStr

class Socket_Msg():

    def __init__(self):
        self.s2c_proto_class = Protounpack.S2C_PROTO()
        self.data = []

    def encapsulated_headers(self, c2s):
        """包头封装，加入body长度
        :param:c2s:协议体内容
        :return:整包内容，包括协议体长度与协议体内容
        """
        lenth = len(c2s)
        btlth = struct.pack(">I", lenth)
        return btlth + c2s

    def analysis_headers(self, msg):
        """包头解析，获取协议体长度
        :param:msg:包头数据
        :return:协议体长度
        """
        msg_str = bytes(msg)
        lenth = struct.unpack(">I", msg_str)[0]
        return lenth

    def send_proto(self, connect, prototy):
        """
        发送协议多次（用于单次）
        :param connect:socket通信 
        :param prototy:协议体 
        :return: 
        """
        rpc_res = self.inputproto(prototy, connect)
        rpc_pkg = self.rpc(rpc_res)
        c2s = self.encapsulated_headers(rpc_pkg)
        print u"发送数据的二进制是：", ''.join((r'\x%02x' % ord(c) for c in c2s))
        connect.send(c2s)

    def send_proto_repeate(self, connect, prototy, sdtime):
        """
        发送协议多次（用于并发）
        :param connect:socket通信 
        :param prototy:协议体 
        :param sdtime:并发执行时间,默认为1秒后，由客户端代码给出 
        :return: 
        """
        localtime = TimeTreatment().getlocaltimestamp()
        # 并发处理，需求相同时间下做并发行为
        while localtime < sdtime:
            time.sleep(0.01)
            localtime = TimeTreatment().getlocaltimestamp()
        rpc_res = self.inputproto(prototy, connect)
        rpc_pkg = self.rpc(rpc_res)
        c2s = self.encapsulated_headers(rpc_pkg)
        connect.send(c2s)
        #后续部分仅用于内部调试，打包前注意注释掉
        # revlmsg = connect.recv(4)
        # lenth = self.analysis_headers(revlmsg)
        # time.sleep(0.01)
        # revmsg = connect.recv(lenth)
        # self.s2cdata(revmsg)

    def reserve_proto(self, connect, loggerField):
        """接收并打印协议内容
        :param:msg:包头数据
        :param:loggerField:输出文本框实例
        :param:cf:开关状态
        :return:
        """
        lock.acquire()
        while True:
            try:
                # 防止协议断开后还在持续接收
                revlmsg = connect.recv(4)
                lenth = self.analysis_headers(revlmsg)
                time.sleep(0.01)
                revmsg = connect.recv(lenth)
            except:
                print "Link  Disconnected! "
                break
            proto_name,proto_msg,proto = self.s2cdata(revmsg)
            pbs = [proto_name,proto]#单条协议
            global protodata
            if len(protodata) > 5:
                # 每五条协议清空协议buffer
                protodata = []
            protodata.append(pbs)
            logger = u"收到协议消息("+TimeTreatment().getlocaltime()+u")：\n"\
                    +proto_name+"\n"+proto_msg+"\n\n"
            loggerField.AppendText(logger)
        lock.release()

    def send_and_resrve_data(self, connect, prototy, s2c, overtime=3.00):
        # 发送并在规定时间内接收协议字段
        rpc_res = self.inputproto(prototy, connect)
        rpc_pkg = self.rpc(rpc_res)
        c2s = self.encapsulated_headers(rpc_pkg)
        connect.settimeout(overtime)  # 协议接收超时时间，避免无限处于阻塞状态
        connect.send(c2s)
        protodata = ""
        localtime1 = time.time()
        while True:
            try:
                # 超时后抛出超时异常
                revlmsg = connect.recv(4)
                lenth = self.analysis_headers(revlmsg)
                time.sleep(0.01)
                revmsg = connect.recv(lenth)
            except:
                # 接收超时
                localtime2 = time.time()
                usetime = format(localtime2 - localtime1, ".2f")
                usetime = u"超时，执行时长为：" + unicode(usetime)
                break
            proto_name, proto_msg, proto = self.s2cdata(revmsg)
            if proto_name == s2c:
                #返回协议检查
                protodata = proto_msg
                localtime2 = time.time()
                usetime = format(localtime2 - localtime1, ".2f")
                break
        if s2c == u"":
            protodata = u"该协议没有设置返回协议"
        return protodata,usetime

    def rpc(self, c2s):
        """
        把协议体装进rpc协议中，并把rpc序列化
        :param c2s: 协议体
        :return: 
        """
        if isinstance(c2s, list):
            for each in rpc_pb2._SERVICENO.values:
                if each.name == c2s[0]:
                    proto_id = each.number
                    break
            else:
                raise BaseException, u"没有找到对应协议名"
            # 将proto_id转换成16进制字符串
            proto_id_bin = int2varint(proto_id)
            # 将参数转换成bytes
            if c2s[1]:
                param_bin = ''
                for index, each in enumerate(c2s[1]):
                    index_str = bin(index+1).split('b')[1]
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
                        each_value = eval(each[0][1:])
                        print type(each_value)
                        if isinstance(each_value, int):
                            int_str = int2bytestr(each_value, index_str)
                            param_bin += int_str
                        if isinstance(each_value, unicode):
                            uni_str = uni2bytestr(each_value, index_str)
                            param_bin += uni_str
                        if isinstance(each_value, float):
                            float_str = float2bytestr(each, index_str)
                            param_bin += float_str
                # 计算协议总长度
                param_bin_len = strlen(param_bin)
                param_bin = param_bin_len + param_bin
            else:
                # 什么参数都不填的情况
                param_bin = r'\x00'
            rpcc2s_str = r'\x08\x01\x10%s\x1a%s' % (proto_id_bin, param_bin)
            rpcc2s = eval("'"+rpcc2s_str+"'")
        else:
            proto_name = c2s.DESCRIPTOR.name
            c2s_bytes = c2s.SerializeToString()
            rpc = rpc_pb2.c2senvelope()
            rpc.correlation_id = 1
            # 通过协议名查询id
            for each in rpc_pb2._SERVICENO.values:
                if each.name == proto_name:
                    proto_id = each.number
                    break
            else:
                raise BaseException, u"没有找到对应的协议名"
            rpc.service_no = proto_id
            rpc.payload = c2s_bytes
            rpcc2s = rpc.SerializeToString()
        return rpcc2s

    def s2cdata(self, data):
        """
        处理接收到的二进制数据
        :param data: 二进制数据
        :param s2cname: 
        :return: 
        """
        s2clist = []
        # 实例化rpc
        s2crpc = rpc_pb2.s2cenvelope()
        # 反序列化rpc
        s2crpc.ParseFromString(data)
        # 返回的协议id
        protoid = s2crpc.service_no
        # 返回的协议数据
        protodata = s2crpc.payload
        # 通过id反查协议名
        for each in rpc_pb2._SERVICENO.values:
            if each.number == protoid:
                s2cname = each.name
                break
        else:
            raise BaseException, u"cannot find s2c proto name, maybe new add"
        # 打印协议名
        print u"返回数据的协议名为：", s2cname
        # 实例化对应的协议
        s2cproto = eval(s2cname)()
        # 反序列化协议
        s2cproto.ParseFromString(protodata)
        # 用json格式打印协议
        protojson = pbjson.pb2json(s2cproto)
        print u"返回数据的json格式为："
        print protojson
        # 提取协议中需要的数据
        try:
            s2clist = getattr(self.s2c_proto_class, s2cname)(s2cproto)
        except AttributeError as e:
            print e
            print u"没有需要提取的数据"
        return s2cname, protojson, s2clist

    def inputproto(self, cmd, connect=None):
        """
        通过协议名返回协议体
        """
        if cmd.find(' ') != -1:
            # cmd = cmd.split(' ')
            func = cmd.split(' ')[0]
            param = cmd.split(' ', 1)[1]
            originalparam = []
            transparam = []
            param_each = ''
            for i, c in enumerate(param):
                if c == "'" or c == '"':
                    if param_each and param_each != '$':
                        param_each += c
                        originalparam.append(param_each)
                        param_each = ''
                    else:
                        param_each += c
                elif c == ' ':
                    if '"' in param_each or "'" in param_each:
                        param_each += c
                    elif param_each:
                        originalparam.append(param_each)
                        param_each = ''
                else:
                    param_each += c
            if param_each:
                originalparam.append(param_each)
            for each in originalparam:
                try:
                    each_param = eval(each)
                except SyntaxError:
                    if each.startswith('$'):
                        each_param = [each]
                    else:
                        raise SyntaxError, u"你输入的参数格式有误，1.str必须加上引号,2.每个参数之间加上一个空格,3.末尾不能有空格"
                except NameError as e:
                    if each.startswith('hbid'):
                        print u"输入的是伙伴id，转换uid后发送"
                        ptime = 0.0
                        while ptime < 1.00:
                            self.proto_hb_uid(connect)
                            revlmsg = connect.recv(4)
                            lenth = self.analysis_headers(revlmsg)
                            time.sleep(0.01)
                            revmsg = connect.recv(lenth)
                            s2cname, protojson, s2clist = self.s2cdata(revmsg)
                            print s2cname
                            if s2cname == 's2c_get_partner_list':
                                break
                            ptime += 0.01
                        if ptime == 1.00:
                            print u"协议接收超时！"
                        for pt in s2clist:
                            if pt[0] == int(each[4:]):
                                uid = pt[1]
                                break
                        else:
                            raise BaseException, u"not find fb id!!"
                        print uid
                        each_param = uid
                    else:
                        print e
                        raise NameError(e)
                # 支持'$123'、'$"123"'这种格式作为新加参数
                if isinstance(each_param, str):
                    if each_param.startswith('$'):
                        each_param = [each_param]
                # 解决中文编码问题
                if type(each_param) == str:
                    transparam.append(each_param.decode('utf-8'))
                else:
                    transparam.append(each_param)
            param = transparam
        else:
            func = cmd
            param = None
        protofunc = getattr(C2S_PROTO(), func)
        if param:
            for each in param:
                # 支持$123、$'123'这种格式作为新加参数
                if isinstance(each, list):
                    print u"有新加的参数，直接修改二进制后发送"
                    return [func, param]
                # 支持'$123'、'$"123"'这种格式作为新加参数
                if isinstance(each, unicode):
                    if each.startswith('$'):
                        print u"有新加的参数，直接修改二进制后发送"
                        return [func, param]
                if each is None:
                    print u"有不要的参数，直接修改二进制后发送"
                    return [func, param]
            try:
                c2s = protofunc(param)
            except TypeError as e:
                print e
                raise BaseException, u"你输入的参数格式与正确格式不符，直接修改二进制后发送"
        else:
            try:
                c2s = protofunc()
            except TypeError:
                print u"没有输入参数，直接修改二进制后发送"
                return [func, None]
        return c2s

    def proto_hb_uid(self, connect):
        """
        获取伙伴UID
        :id_list: 伙伴ID
        :return: 
        """
        print u"发送获取伙伴UID协议"
        c2s = c2s_get_partner_list()
        rpc_pkg = self.rpc(c2s)
        send_data = self.encapsulated_headers(rpc_pkg)
        connect.send(send_data)

    def text_alignment(self, strings, width, just="left"):
        #文本对齐接口（主要处理中文与其他字符混搭）
        #:param:strings:输入文本，注意必须是unicode或者utf-8码)
        #:param:width:整体长度,若超出长度，则直接增加4个空格
        #:param:just:对齐方式
        #:return:strings:格式化字符串
        cn_count = 0
        for uchar in strings:
        #判断字符是否是中文
            if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
                cn_count += 2  # 计算中文字符占用的宽度
            else:
                cn_count += 1  # 计算英文字符占用的宽度
        if just == "right":
            if width - cn_count > 4:
                return " " * (width - cn_count) + strings
            else:
                return " " * 4 + strings
        elif just == "left":
            if width - cn_count > 4:
                return strings + " " * (width - cn_count)
            else:
                return strings + " " * 4

    def return_data(self):
        data = self.data
        return data
