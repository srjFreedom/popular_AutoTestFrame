# -*- coding: utf8 -*-

import socket

class ServerSide():
    def __init__(self):
        self.Host = '127.0.0.1'
        self.Port = 21228
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.Host,self.Port))
        self.s.listen(1)

    def testServer(self):
        while 1:
            conn,addr = self.s.accept()
            print 'Connected by: ', addr
            try:
                while 1:
                    data = conn.recv(1024)
                    print data
                    conn.sendall('OK!')
            except Exception,e:
                print str(e).decode('gbk')
        conn.close()

if __name__ == '__main__':
    ServerSide().testServer()