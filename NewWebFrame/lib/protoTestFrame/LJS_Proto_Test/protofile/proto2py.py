# -*- coding:utf8 -*-

import os
protolist = os.listdir(os.path.dirname(__file__))
for proto in protolist:
    if r".proto" in proto:
        protoc = 'protoc --python_out=./ ./%s' % proto
        os.system(protoc)
os.system('pause')