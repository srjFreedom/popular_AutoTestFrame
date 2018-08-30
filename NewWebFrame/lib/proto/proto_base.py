# -*- coding: utf-8 -*-
"""
这个文件下的方法与具体项目的协议无关，但会在协议测试中用到
"""


def get_func_from_cmd(cmd):
    if cmd.find(' ') == -1:
        func = cmd
    else:
        func = cmd.split(' ')[0]
    return func


def get_params_from_cmd(cmd):
    if cmd.find(' ') == -1:
        params_list = []
    else:
        param_str = cmd.split(' ', 1)[1]
        each_param = ''
        params_list = []
        for e in param_str:
            if e == ' ' and '"' not in each_param and "'" not in each_param and each_param:
                params_list.append(each_param)
                each_param = ''
            elif e == '"' and '"' in each_param:
                each_param += e
                params_list.append(each_param)
                each_param = ''
            elif e == "'" and "'" in each_param:
                each_param += e
                params_list.append(each_param)
                each_param = ''
            else:
                each_param += e
        if each_param:
            params_list.append(each_param)
    return params_list


def clear_params_list(params_list):
    after_clear_params_list = []
    for each in params_list:
        try:
            each_param = eval(each)
        except SyntaxError as e:
            if each.startswith('$'):
                add_param = eval(each[1:])
                if type(add_param) == str:
                    add_param = add_param.decode('utf8')
                each_param = [add_param]
            else:
                raise SyntaxError(e)
        if type(each_param) == str:
            each_param = each_param.decode('utf-8')
        after_clear_params_list.append(each_param)
    return after_clear_params_list


def int2varint(int_value):
    """
    PB协议，通过int值得出varint的16进制的字符串
    :param int_value: int值
    :return: varint的二进制字符串
    """
    import protobuf_test_pb2
    c2s = protobuf_test_pb2.c2s_test()
    c2s.test_int32 = int_value
    c2s_serial = c2s.SerializeToString()
    c2s_hex_str = ''.join((r'\x%02x' % ord(c) for c in c2s_serial))
    # 把头部的类型去掉，只保留数据本身
    c2s_data_hex_str = c2s_hex_str[4:]
    return c2s_data_hex_str


def int2bytestr(int_value, index_str):
    """
    PB协议，通过int值和参数序号得出二进制数据的字符串
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
    PB协议，通过unicode值和参数序号得出二进制数据的字符串
    :param uni_value: 
    :param index_str: 
    :return: 
    """
    type_str = '010'
    head_str = index_str + type_str
    head_hex = hex(int(head_str, 2)).split('x')[1].zfill(2)
    head_hex_str = r'\x%s' % head_hex
    str_str = ''.join((r'\x%02x' % ord(c)for c in uni_value.encode('utf8')))
    len_str = strlen(str_str)
    uni_str = head_hex_str + len_str + str_str
    return uni_str


def float2bytestr(float_value, index_str):
    """
    PB协议，通过float值和参数序号得出二进制数据的字符串
    :param float_value: 
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


def strlen(str_value):
    """
    计算varint的16进制的字符串代表的字节长度
    :param str_value: 
    :return: 
    """
    return r'\x%02x' % eval(hex(len(str_value)/4))


def pb2dict(obj):
    """
    处理PB协议数据并转换成字典形式
    """
    from google.protobuf.descriptor import FieldDescriptor as FD
    adict = {}
    if not obj.IsInitialized():
        return None
    for field in obj.DESCRIPTOR.fields:
        if not getattr(obj, field.name):
            # no param
            adict[field.name] = field.default_value
            continue
        if not field.label == FD.LABEL_REPEATED:
            if not field.type == FD.TYPE_MESSAGE:
                adict[field.name] = getattr(obj, field.name)
            else:
                value = pb2dict(getattr(obj, field.name))
                # if value:
                adict[field.name] = value
        else:
            if field.type == FD.TYPE_MESSAGE:
                adict[field.name] = \
                    [pb2dict(v) for v in getattr(obj, field.name)]
            else:
                adict[field.name] = [v for v in getattr(obj, field.name)]
    return adict


def pb2json(obj):
    """
    处理PB协议数据并转换成JSON字符串形式
    """
    import simplejson
    return simplejson.dumps(pb2dict(obj), sort_keys=True, indent=4, ensure_ascii=True)



