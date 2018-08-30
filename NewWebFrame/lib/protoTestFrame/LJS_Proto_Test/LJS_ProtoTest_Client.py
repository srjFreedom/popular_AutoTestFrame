# -*- coding:utf8 -*-

import socket
import threading
import struct
import time
import wx
from Protopack import *
from Protounpack import *
from Socket_Com import *
import Socket_Com
import requests,json

class LJS_ProtoTest_Client():

    def __init__(self):
        self.socketmethod = Socket_Msg()
        self.logger = ""
        self.serverlist = None

    def login_getway(self, getwayhost, getwayport):
        #登录网关获取网关给出的ip、端口,返回
        getways = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        getways.connect((getwayhost,getwayport))
        #实体封装
        proto_file = "c2s_get_login_host"
        self.socketmethod.send_proto(getways,proto_file)
        getways.settimeout(5)#设置超时
        revmsg = getways.recv(65535)
        if revmsg is None or "":
            getways.shutdown(2)
            getways.close()
            raise BaseException,u"未能正确获取到网关协议！"
        else:
            getways.shutdown(2)
            getways.close()
            host_name,host_info,host_data = self.socketmethod.s2cdata(revmsg)
            return host_data

    def heart_check(self,connect):
        #心跳检测
        c2s = "c2s_heart_check"
        while True:
            #每隔5秒持续发送心跳包，直到接收失败抛出
            try:
                Socket_Msg().send_proto(connect, c2s)
            except:
                break
            time.sleep(5)

    def long_connect(self,loginhosts,loggerField):
        """
        与服务器进行一次socket长连接
        :param loginhosts:连接地址参数 
        :param loggerField:输出文本框实例 
        :return:self.connect:长连接实例 
        """
        login_info = loginhosts
        host = login_info[1]
        port = login_info[2]
        connect = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connect.connect((host,port))
        reserveThread = SocketThread(self.socketmethod.reserve_proto,args=(connect,loggerField))
        reserveThread.start()
        #进行心跳检测
        # t_heart_check = SocketThread(self.heart_check,args=(self.connect,))
        # t_heart_check.start()
        return connect

    def logout(self,host,port,connect,loggerField):
        """
        注销，关闭原有socket，重新建立socekt
        :param connect:原有连接
        :param host:新连接地址
        :param port:新连接端口
        :param loggerField:输出文本框实例 
        :return: 
        """
        old_connect = connect
        old_connect.shutdown(2)
        old_connect.close()
        time.sleep(0.1)
        new_connect = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        new_connect.connect((host,port))
        self.reserveThread = SocketThread(self.socketmethod.reserve_proto,args=(new_connect,loggerField))
        self.reserveThread.start()
        return new_connect

    def connect_and_register(self,host_data,accname,name):
        """
        创建连接并进行建号操作，结束后会自动断开连接
        :return:code:建号结果 
        """
        host = host_data[1]
        port = host_data[2]
        sleeptime = 0.0
        code = 0
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.connect((host,port))
        registdata = 'c2s_register' + " '%s' '%s' '' 2000" % (accname, name)
        self.socketmethod.send_proto(connection, registdata)
        while True:
            revlmsg = connection.recv(4)
            lenth = self.socketmethod.analysis_headers(revlmsg)
            time.sleep(0.01)
            revmsg = connection.recv(lenth)
            proto_name, proto_msg, proto = self.socketmethod.s2cdata(revmsg)
            if proto_name == "s2c_register":
                code = proto[0]
                break
            sleeptime += 0.01
            #超时时长2秒
            if sleeptime > 2.0:
                break
        connection.shutdown(2)
        connection.close()
        return code

    def connect_and_login(self,host_data,accname):
        """
        创建连接并进行登录操作
        :param:host_data:连接参数
        :param:accname:账号基名 
        :return:result：登录结果
        """
        host = host_data[1]
        port = host_data[2]
        sleeptime = 0.0
        code = 0
        result = []
        connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.connect((host,port))
        logindata = 'c2s_login' + " '%s' ''" %accname
        self.socketmethod.send_proto(connection, logindata)
        while True:
            revlmsg = connection.recv(4)
            lenth = self.socketmethod.analysis_headers(revlmsg)
            time.sleep(0.01)
            revmsg = connection.recv(lenth)
            proto_name, proto_msg, proto = self.socketmethod.s2cdata(revmsg)
            if proto_name == "s2c_login":
                code = proto[0]
                break
            sleeptime += 0.01
            #超时时长2秒
            if sleeptime > 2.0:
                break
        result.append(code)
        result.append(connection)
        return result

    def get_serverlist(self):
        #获取服务器网关地址/端口，返回一组字典
        request = requests.get('http://192.168.1.184/get_server_list.php')
        serverlist = request.json()
        return serverlist

if __name__ == "__main__":
    ljs = LJS_ProtoTest_Client()
    aaa = ljs.get_serverlist()
    print aaa