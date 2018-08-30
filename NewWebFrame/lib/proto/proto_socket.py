# -*- coding: utf-8 -*-

import socket
import threading
import time
import sys
import os
from proto_base import *

# print os.path.normpath(os.path.join(os.path.dirname(__file__), 'lib/protobuf2'))
class Proto_socket(object):

    def __init__(self, project, server='', port=0):
        self.server = server
        self.port = int(port)
        self.proto_data_list = []  # 存储最近的几条返回数据
        self.a_socket = None
        self.project = project

    def _project_import(self, project):
        if project == 'LJS':
            import proj.LJS.proto_LJS as proto_Project
            return proto_Project

    def create_socket(self):
        self.a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.a_socket.connect((self.server, self.port))
        except socket.timeout:
            return None
        # 请求网关
        proto_proj = self._project_import(self.project)
        data = proto_proj.get_host_by_proto()
        c2s = self.get_proto_c2s(data)
        self.send_proto(c2s)
        self.a_socket.settimeout(3)
        proto_dict = self.recv_proto()
        ip, port = proto_proj.get_host_by_dict(proto_dict)
        self.a_socket.shutdown(2)
        self.a_socket.close()
        self.a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.a_socket.connect((ip, port))
        return self.a_socket

    def get_proto_c2s(self, cmd):
        proto_proj = self._project_import(self.project)
        params_list = get_params_from_cmd(cmd)
        after_clear_params_list = clear_params_list(params_list)
        func = get_func_from_cmd(cmd)
        rpc_c2s = proto_proj.rpc_serialize(func, after_clear_params_list)
        c2s = proto_proj.encapsulated_headers(rpc_c2s)
        # print u"发送数据的二进制是：", ''.join((r'\x%02x' % ord(c) for c in c2s))
        return c2s

    def get_acc_register(self, accname, nickname, password):
        proto_proj = self._project_import(self.project)
        # 灵剑山项目注册前需要先尝试登录一下
        if self.project == 'LJS':
            cmd = proto_proj.acc_login(accname)
            c2s = self.get_proto_c2s(cmd)
            self.send_proto(c2s)
            proto_dict = self.recv_proto()
        cmd = proto_proj.acc_register(accname, nickname)
        c2s = self.get_proto_c2s(cmd)
        self.send_proto(c2s)
        proto_dict = self.recv_proto()
        return proto_dict

    def check_acc_register(self, proto_dict):
        proto_proj = self._project_import(self.project)
        return proto_proj.check_acc_register_dict(proto_dict)

    def get_acc_login(self, accname, password):
        proto_proj = self._project_import(self.project)
        cmd = proto_proj.acc_login(accname)
        c2s = self.get_proto_c2s(cmd)
        self.send_proto(c2s)
        proto_dict = self.recv_proto()
        return proto_dict

    def check_acc_login(self, proto_dict):
        proto_proj = self._project_import(self.project)
        return proto_proj.check_acc_login_dict(proto_dict)

    def send_player_name(self):
        proto_proj = self._project_import(self.project)
        cmd = proto_proj.player_name_c2s_proto()
        c2s = self.get_proto_c2s(cmd)
        self.send_proto(c2s)

    def recv_player_name(self):
        # time.sleep(0.2)
        proto_proj = self._project_import(self.project)
        s2c_name = proto_proj.player_name_s2c_proto()
        num = 300
        while True and num:
            num -= 1
            time.sleep(0.01)
            for data in self.proto_data_list:
                if data.get(s2c_name):
                    return proto_proj.get_player_name(data.get(s2c_name))
        return u'未获取到昵称'

    def send_gm(self, gm):
        proto_proj = self._project_import(self.project)
        cmd = proto_proj.trans_gm(gm)
        c2s = self.get_proto_c2s(cmd)
        self.send_proto(c2s)

    def send_c2s_values(self, c2s, values, counts=1):
        if values:
            cmd = c2s + ' ' + values
        else:
            cmd = c2s
        msg = self.get_proto_c2s(cmd)
        assert counts >= 1
        for times in xrange(counts):
            self.send_proto(msg)

    def send_proto(self, c2s):
        try:
            self.a_socket.send(c2s)
        # socket关闭后不再发送消息
        except AttributeError as e:
            print e
        except socket.error as e:
            print 'send game proto: %s' % e
            self.close_socket()

    def recv_proto(self):
        proto_proj = self._project_import(self.project)
        if self.a_socket:
            msg = proto_proj.get_recv_msg(self.a_socket)
        else:
            raise BaseException('no socket to recv msg')
        if msg is None:
            return None
        s2c = proto_proj.get_recv_data_from_msg(msg)
        proto_dict = proto_proj.get_dict_from_data(s2c[1])
        return proto_dict

    def recv_proto_for_loop(self, message=None, webSocket=None, user=None):
        while True:
            if webSocket and getattr(webSocket, 'isRun', True) is False:
                break
            proto_proj = self._project_import(self.project)
            if self.a_socket is None:
                return False
            self.a_socket.settimeout(2)
            msg = proto_proj.get_recv_msg(self.a_socket)
            if msg is False:
                break
            if msg:
                s2c = proto_proj.get_recv_data_from_msg(msg)
                self.clear_proto_data_list()
                s2c_need_dict = proto_proj.get_need_dict_from_data(*s2c)
                if s2c_need_dict:
                    self.proto_data_list.append(s2c_need_dict)
                proto_json = proto_proj.get_json_from_data(s2c[1])
                if message:
                    print u'玩家 %s 接收到协议：%s' % (user, s2c[0])
                    msg_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    msg_title = '<b>%s (%s)</b>' % (s2c[0], msg_time)
                    message.send(msg_title + '\n' + proto_json)
        print u'与游戏服务器断开连接'
        self.close_socket()
        return False

    def clear_proto_data_list(self):
        lenth = len(self.proto_data_list)
        if lenth > 5:
            self.proto_data_list.pop(0)

    def close_socket(self):
        """
        如果有socket，关闭socket
        :return: 
        """
        if self.a_socket:
            temp_socket = self.a_socket
            self.a_socket = None
            temp_socket.shutdown(2)
            temp_socket.close()

    def get_xitong_list(self):
        """
        获取协议的系统名称列表
        :return: 
        """
        proto_proj = self._project_import(self.project)
        return proto_proj.get_system_list()

    def get_gongneng_list(self):
        """
        获取特殊功能查询按钮列表
        :return: 
        """
        proto_proj = self._project_import(self.project)
        return proto_proj.get_query_list()

    def get_xieyi_list(self, system_name):
        """
        获取指定系统的协议名称
        :return: 
        """
        proto_proj = self._project_import(self.project)
        return proto_proj.get_protoname_list(system_name)

    def get_shuoming_info(self, protoname):
        proto_proj = self._project_import(self.project)
        return proto_proj.get_note_info(protoname)

    def get_jieguoma(self, code):
        proto_proj = self._project_import(self.project)
        return proto_proj.get_code_info(code)

    def get_xiangqing(self, fuc):
        proto_proj = self._project_import(self.project)
        cmd = proto_proj.get_detail_c2s(fuc)
        if cmd:
            c2s = self.get_proto_c2s(cmd)
            self.send_proto(c2s)
            return True
        else:
            return False

    def recv_xiangqing(self, func):
        time.sleep(0.2)
        proto_proj = self._project_import(self.project)
        s2c_name = proto_proj.get_detail_s2c(func)
        for retry in xrange(10):
            for data in self.proto_data_list[::-1]:
                if s2c_name in data:
                    self.proto_data_list.remove(data)
                    return data
            time.sleep(0.2)

    def trans_xiangqing(self, detail_dict):
        proto_proj = self._project_import(self.project)
        detail_info = proto_proj.trans_detail(detail_dict)
        return detail_info


class SocketThread(threading.Thread):

    def __init__(self, func, args=()):
        super(SocketThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)