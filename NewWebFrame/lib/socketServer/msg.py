# -*- coding: utf-8 -*-

from multiprocessing import Queue
from multiprocessing import Pipe


# from Queue import Queue

class Msg_for_pipe(object):
    def __init__(self):
        self.parent_pipe, self.child_pipe = Pipe()
        self.msgText = None

    def send(self, m):
        self.msgText = m
        self.child_pipe.send(self.msgText)

    def receive(self):
        return self.parent_pipe.recv()

    def p_send(self, m):
        self.p_msgText = m
        self.parent_pipe.send(self.p_msgText)

    def p_receive(self):
        return self.child_pipe.recv()



class Msg_for_queue(object):
    def __init__(self):
        self.que = Queue(maxsize=0)
        self.msgText = None

    def send(self, m):
        self.msgText = m
        self.que.put(self.msgText)

    def receive(self, ):
        return self.que.get()