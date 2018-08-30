# -*- coding: utf-8 -*-

from lib.sqlLib.sqlConnect import SqlConnect
import requests


class GetProtoDir(object):

    def create_proto_db(self):
        sql_str = "CREATE TABLE IF NOT EXISTS PROTO_SERVER" \
                  "(SERVER_ID INT, PROJECT TEXT, IP TEXT, HOST INT, PROJECT_NAME TEXT, SERVER_NAME TEXT)"
        SqlConnect('sql/webFrame.db').commit_excute(sql_str)

    def get_proto_server(self, project):
        # sql_str = "SELECT * FROM PROTO_SERVER WHERE PROJECT == '%s'" % project
        # server_info = SqlConnect('sql/webFrame.db').excute(sql_str)
        # server_dict_info = []
        # for each in server_info:
        #     server_dict = {
        #         'project': each[0],
        #         'host': each[1],
        #         'port': each[2],
        #         'p_name': each[3],
        #         'name': each[4]
        #     }
        #     server_dict_info.append(server_dict)
        if project == 'LJS':
            request = requests.get('http://192.168.1.184/get_server_list.php')
            server_dict_info = request.json().get(u'list')
            # {u'port': 8091, u'ip': u'192.168.1.184', u'id': 1, u'name': u'\u5f00\u53d1\u670d'}
            return server_dict_info

    def get_proto_host_port(self, project, server_id):
        if project == 'LJS':
            request = requests.get('http://192.168.1.184/get_server_list.php')
            server_dict_info = request.json().get(u'list')
            for each in server_dict_info:
                if server_id == each.get('id'):
                    # {u'port': 8091, u'ip': u'192.168.1.184', u'id': 1, u'name': u'\u5f00\u53d1\u670d'}
                    return each
            else:
                raise BaseException('error server id: %s' % server_id)
