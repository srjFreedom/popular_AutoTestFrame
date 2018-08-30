# -*- coding: utf-8 -*-

import threading
import socket
import hashlib
import base64
import struct
import traceback

class init_webSocketServer(object):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 连接设置端口复用
        self.s.bind(('127.0.0.1', 7777))
        self.s.listen(10)
        print ' * socketServer已启动!'


class Real_webSocketServer(object):
    def __init__(self, server, msg):
        self.ss = server.s
        self.msg = msg


    def _sendMsg(self):
        self.con_ss, addr_ss = self.ss.accept()
        print 'Con Success! Connected by: ', addr_ss
        verifyMsg = self.con_ss.recv(1024)
        headers = parse_headers(verifyMsg)
        token = generate_token(headers['Sec-WebSocket-Key'])
        response = 'HTTP/1.1 101 Switching Protocols\r\n' \
                   'Connection: Upgrade\r\n' \
                   'Upgrade: websocket\r\n' \
                   'Sec-WebSocket-Accept: {0}\r\n\r\n'.format(token)
        self.con_ss.send(response)  # 请求连接
        self.isRun = True
        judgeConnect = threading.Thread(target=self._judgeConnect)
        judgeConnect.start()
        while self.isRun:
            try:
                pipeData = self.msg.receive()
                self.con_ss.sendall(write_msg(pipeData))
            except:
                pass
        judgeConnect.join()

    def _judgeConnect(self):
        while self.isRun:
            try:
                clientData = self.con_ss.recv(1024)
                conKeep = parse_data(clientData)
            except Exception:
                print traceback.format_exc()
                conKeep = '2'
            if conKeep == '1':
                continue
            elif conKeep == '0':
                print '用户离开，断开连接'
                self.isRun = False
                try:
                    self.con_ss.shutdown(socket.SHUT_RDWR)
                    self.con_ss.close()
                except Exception:
                    print str(traceback.format_exc()).decode('gbk')
            elif conKeep == '2':
                print '异常，断开连接'
                self.isRun = False
                try:
                    self.con_ss.shutdown(socket.SHUT_RDWR)
                    self.con_ss.close()
                except Exception:
                    print str(traceback.format_exc()).decode('gbk')

    def start(self):
        sendMsg = threading.Thread(target=self._sendMsg)
        sendMsg.start()


# web端返回数据处理
def parse_headers(msg):
    headers = {}
    header, data = msg.split('\r\n\r\n', 1)
    for line in header.split('\r\n')[1:]:
        key, value = line.split(': ', 1)
        headers[key] = value
    return headers

# 创建密钥
def generate_token(msg):
    key = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    ser_key = hashlib.sha1(key).digest()
    return base64.b64encode(ser_key)

# 接收数据解码
def parse_data(msg):
    v = ord(msg[1]) & 0x7f
    if v == 0x7e:
        p = 4
    elif v == 0x7f:
        p = 10
    else:
        p = 2
    mask = msg[p:p + 4]
    data = msg[p + 4:]
    return ''.join([chr(ord(v) ^ ord(mask[k % 4])) for k, v in enumerate(data)])

# 发送数据封装
def write_msg(message):
    data = struct.pack('B', 129) # 第一个字节:10000001
    msg_len = len(message) # 长度
    if msg_len <= 125:
        data += struct.pack('B', msg_len)
    elif msg_len <= (2 ** 16 -1):
        data += struct.pack('!BH', 126, msg_len)
    elif msg_len <= (2 ** 64 - 1):
        data += struct.pack('!BQ', 127, msg_len)
    else:
        print '消息过长!'
        return
    data += bytes(message) # 消息本体
    return data