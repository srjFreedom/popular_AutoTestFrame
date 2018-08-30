# -*- coding:utf8 -*-
"""
pb协议规定的数据类型对应ID
ID  含义          数据类型
0   varint       int，bool，enum
1   64位         double
2   不限长度      string，message，repeated
3   start group  groups
4   end group    groups  
5   32位         float
"""
from protofile.test_pb2 import *


# def EncodeVarint(value):
#     """
#     目前只能转换-129~+无穷，有局限性
#     :param value:
#     :return:
#     """
#     if value >= 0:
#         varint = b''
#         bits = value & 0x7f
#         value >>= 7
#         while value:
#             varint += chr(0x80 | bits)
#             bits = value & 0x7f
#             value >>= 7
#         varint += chr(bits)
#         return varint
#     else:
#         varint = b''
#         value = -value
#         bits = value & 0x7f
#         value >>= 7
#         while value:
#             varint += chr(0x80 | bits)
#             bits = value & 0x7f
#             value >>= 7
#         varint += chr(bits)
#         varint_value = eval(r'0x' + ''.join(bytes2str(varint).split(r'\x')))
#         re_result = 0x01ffffffffffffffffff - varint_value + 1
#         result = hex(re_result)
#         result = result.replace('x', '')
#         each_hex = ''
#         hex_list = []
#         for i in xrange(20):
#             each_hex += result[i]
#             if i%2 != 0:
#                 hex_list.append(each_hex)
#                 each_hex = ''
#         hex_list.reverse()
#         result_hex = ''.join((r'\x%s' % c for c in hex_list))
#         print result_hex


def bytes2str(byte_value):
    return ''.join((r'\x%02x' % ord(c)for c in byte_value))


def unicode2str(uni):
    return ''.join((r'\x%02x' % ord(c)for c in uni.encode('utf8')))


def strlen(str_value):
    """
    计算16进制字符串代表的字节长度
    :param str_value: 
    :return: 
    """
    return r'\x%02x' % eval(hex(len(str_value)/4))


def int2bytestr(int_value, index_str):
    """
    通过int值和参数序号得出二进制数据的字符串
    :param int_value: int值
    :param index_str: 参数序号
    :return: 
    """
    type_str = '000'
    head_str = index_str + type_str
    head_hex = hex(int(head_str, 2)).split('x')[1].zfill(2)
    head_hex_str = r'\x%s' % head_hex
    valint_str = int2varint(int_value)
    int_str = head_hex_str + valint_str
    return int_str


def uni2bytestr(uni_value, index_str):
    """
    通过unicode值和参数序号得出二进制数据的字符串
    :param uni_value: 
    :param index_str: 
    :return: 
    """
    type_str = '010'
    head_str = index_str + type_str
    head_hex = hex(int(head_str, 2)).split('x')[1].zfill(2)
    head_hex_str = r'\x%s'%head_hex
    str_str = unicode2str(uni_value)
    len_str = strlen(str_str)
    uni_str = head_hex_str + len_str + str_str
    return uni_str

# 通过测试协议序列化得出相应的二进制


def int2varint(int_value):
    """
    通过int值得出16进制的字符串
    :param int_value: int值
    :return: varint的二进制字符串
    """
    c2s = c2s_test()
    c2s.test_int32 = int_value
    c2s_serial = c2s.SerializeToString()
    c2s_hex_str = ''.join((r'\x%02x' % ord(c) for c in c2s_serial))
    # 把头部的类型去掉，只保留数据本身
    c2s_data_hex_str = c2s_hex_str[4:]
    return c2s_data_hex_str


def float2hexstr(float_value):
    """
    :param int_value: float值
    :return: varint的二进制字符串
    """
    c2s = c2s_test()
    c2s.test_float = float_value
    c2s_serial = c2s.SerializeToString()
    c2s_hex_str = ''.join((r'\x%02x' % ord(c) for c in c2s_serial))
    # 把头部的类型去掉，只保留数据本身
    c2s_data_hex_str = c2s_hex_str[4:]
    return c2s_data_hex_str


def float2bytestr(float_value, index_str):
    """
    通过float值和参数序号得出二进制数据的字符串
    :param uni_value: 
    :param index_str: 
    :return: 
    """
    type_str = '101'
    head_str = index_str + type_str
    head_hex = hex(int(head_str, 2)).split('x')[1].zfill(2)
    head_hex_str = r'\x%s' % head_hex
    str_str = float2hexstr(float_value)
    float_str = head_hex_str + str_str
    return float_str

