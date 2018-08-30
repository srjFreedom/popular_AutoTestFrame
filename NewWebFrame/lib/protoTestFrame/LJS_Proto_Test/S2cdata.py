# -*- coding:utf8 -*-

import rpc_pb2
from protofile.Protounpack import *
from protofile.accname_pb2 import *
from protofile.achieve_pb2 import *
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
from protofile.realtime_PVP_pb2 import *
from protofile.rpc_pb2 import *
from protofile.shop_pb2 import *
from protofile.sign_pb2 import *
from protofile.task_pb2 import *
from protofile.trial_pb2 import *
from protofile.wonderland_pb2 import *
import pbjson


class S2CDATA():


    def s2cdata(self, data):
        """
        处理返回的二进制数据
        :param data: 二进制数据
        :param s2cname: 
        :return: 
        """
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
            raise BaseException, u"没有找到对应的协议名"
        # 打印协议名
        print u"返回数据的协议名为："
        print s2cname
        # 实例化对应的协议
        s2cproto = eval(s2cname)()
        # 反序列化协议
        s2cproto.ParseFromString(protodata)
        # 用json格式打印协议
        print u"返回数据的json格式为："
        print pbjson.pb2json(s2cproto)
        # 提取协议中需要的数据
        s2clist = getattr(S2C_PROTO(), s2cname)(s2cproto)
        return s2clist


