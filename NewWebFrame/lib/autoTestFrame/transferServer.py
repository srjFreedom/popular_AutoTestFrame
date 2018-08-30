# -*- coding: utf8 -*-

import os
import random

class TransferServer(object):
    def __init__(self):
        pass

    def runServer(self, phone_ip):
        if phone_ip == '':
            pass
        else:
            os.environ['LOCAL_PHONE_IP'] = phone_ip
            os.popen('adb connect ' + phone_ip)
            enginePort = random.randint(49153, 65534)
            os.environ['LOCAL_ENGINE_PORT'] = str(enginePort)