# -*- coding:utf8 -*-

import socket
import threading


lock = threading.RLock()

class ClientSide():
    def __init__(self):
        self.Host = '127.0.0.1'
        self.Port = 21228
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # self.s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.s.connect((self.Host, self.Port))

    def testClient(self):
        lock.acquire()
        #while 1:
        cmd = raw_input('Please input: ')
        self.s.sendall(cmd.encode('utf8'))
        # self.s.sendall('a')
        data = self.s.recv(1024)
        if data is None:
            print 'Have not data response!'
        else:
            print data
        lock.release()

    #threading中Thread函数多线程并发
    def threadTest(self):
        for i in range(10):
            t = threading.Thread(target=self.testClient)
            t.start()


if __name__ == '__main__':
    ClientSide().threadTest()