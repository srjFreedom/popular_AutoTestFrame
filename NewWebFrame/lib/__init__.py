# -*- coding: utf-8 -*-

import sys
from log import LoggerEat, LoggerVomit
from scriptsDir.program_director import Program_director
from autoTestFrame.autoTestRunnerForWeb import AutoTestRunnerForWeb
from autoTestFrame.transferServer import TransferServer
from sqlLib.sqlConnect import SqlConnect
from sqlLib.sqlOpration.loginVerify import LoginVerify
from sqlLib.sqlOpration.getProjectDir import GetProjectDir
from sqlLib.sqlOpration.getReportDir import GetReportDir
from sqlLib.sqlOpration.getUser import GetUser
from socketServer.real_webSocketServer import Real_webSocketServer, init_webSocketServer
from socketServer.msg import Msg_for_queue, Msg_for_pipe
from sqlLib.sqlOpration.getProtoDir import GetProtoDir
from proto.proto_socket import Proto_socket
from proto.proto_socket import SocketThread
from proto.local import Local


sys.stderr = LoggerVomit()
sys.stdout = LoggerEat()
socketServer = init_webSocketServer()
msg_dict_pipe = {}
msg_dict_queue = {}