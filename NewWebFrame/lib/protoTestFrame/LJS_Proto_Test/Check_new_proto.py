# -*- coding: UTF-8 -*-
import os
from Protopack import C2S_PROTO

proto_file = r'D:\灵剑山\Branches\Server\trunk\proto'.decode('utf-8')

proto_file_list = os.listdir(proto_file)

proto_c2s_list = []

print 'proto_file_list: ', proto_file_list

for each_proto in proto_file_list:
    print 'each_proto: ', each_proto
    each_proto_name = os.path.join(proto_file, each_proto)
    with open(each_proto_name, 'r') as f:
        proto_read_list = f.readlines()
        pattern = 'message c2s'
        for proto_read in proto_read_list:
            if proto_read.startswith(pattern):
                proto_c2s = proto_read.split('message')[1].split('{')[0].strip()
                print 'proto_c2s: ', proto_c2s
                proto_c2s_list.append(proto_c2s)

print 'proto_c2s_list: ', proto_c2s_list

funclist = dir(C2S_PROTO)
funclist.remove('__doc__')
funclist.remove('__module__')
funclist.append('c2senvelope')
print 'funclist: ', funclist

for func in funclist:
    if func not in proto_c2s_list:
        print 'have ex proto: ', func
for proto_c2s in proto_c2s_list:
    if proto_c2s not in funclist:
        print 'have new proto: ', proto_c2s
