# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, url_for, redirect, request, session, g
from lib import *
import json

proto = Blueprint('proto', __name__)
user_local = Local()


@proto.route('/choose_proto_project', methods=['GET', 'POST'])
def choose_proto_project():
    request_value = request.values.get('request')
    if request_value:
        session['proto_project'] = request_value
        return redirect(url_for('.choose_server'))
    else:
        return redirect(url_for('index'))


@proto.route('/choose_server', methods=['GET', 'POST'])
def choose_server():
    request_value = request.values.get('request')
    if request_value == 'js_choose_server':
        if g.proto_project:
            id = request.values.get('id')
            if id is not None:
                host_port_dict = GetProtoDir().get_proto_host_port(g.proto_project, int(id))
                session['proto_host'] = host_port_dict['ip']
                session['proto_port'] = host_port_dict['port']
                session['proto_server_name'] = host_port_dict['name']
            if session.get('proto_host') and session.get('proto_port'):
                return json.dumps({"response": 1})
            else:
                return json.dumps({"response": 2})
        else:
            # 没有获取到项目
            return json.dumps({"response": 2})
    else:
        if g.proto_project:
            server_info = GetProtoDir().get_proto_server(g.proto_project)
            if server_info:
                return render_template('proto/choose_server.html', serverlist=server_info)
            else:
                return u'此项目没有协议测试'
        else:
            # 没有项目，退回到项目选择界面
            return redirect(url_for('index'))


@proto.route('/proto_regist', methods=['GET', 'POST'])
def proto_regist():
    regist = request.values.get('request')
    if regist == 'js_game_register':
        username = request.values.get('username')
        password = request.values.get('password')
        nickname = request.values.get('nickname')
        host = session.get('proto_host')
        port = session.get('proto_port')
        if not host or not port:
            regist_state = False
            regist_info = u'没有获取到服务器信息，请返回服务器列表'
        else:
            proto_socket = Proto_socket(project=g.proto_project, server=host, port=port)
            proto_socket.create_socket()
            if username and nickname and password:
                proto_dict = proto_socket.get_acc_register(username, nickname, password)
                regist_state, regist_info = proto_socket.check_acc_register(proto_dict)
            else:
                regist_state = False
                regist_info = u'没有获取到账号名和昵称信息'
        if regist_state:
            return json.dumps({"response": 6})
        else:
            return json.dumps({"response": 7, 'info': regist_info})
    elif regist == 'js_goto_login':
        # response:8 跳转登录页面
        return json.dumps({"response": 8})
    else:
        return render_template('proto/proto_register.html')


@proto.route('/proto_login', methods=['GET', 'POST'])
def proto_login():
    login = request.values.get('request')
    if login == 'js_game_login':
        username = request.values.get('username')
        password = request.values.get('password')
        host = session.get('proto_host')
        port = session.get('proto_port')
        if not host or not port:
            login_state = False
            login_info = u'没有获取到服务器信息，请返回服务器列表'
        else:
            if username and password:
                proto_socket = Proto_socket(project=g.proto_project, server=host, port=port)
                if user_local.socket:
                    user_local.socket.close_socket()
                    user_local.socket = None
                user_local.socket = proto_socket
                proto_socket.create_socket()
                proto_dict = proto_socket.get_acc_login(username, password)
                login_state, login_info = proto_socket.check_acc_login(proto_dict)
            else:
                login_state = False
                login_info = u"没有输入账号或密码"
        if login_state:
            session['proto_username'] = username
            return json.dumps({"response": 3})
        else:
            return json.dumps({"response": 4, 'info': login_info})
    elif login == 'js_goto_register':
        # response:4 跳转注册页面
        return json.dumps({"response": 5})
    else:
        return render_template('/proto/proto_login.html')


@proto.route('/proto_test', methods=['GET', 'POST'])
def proto_test():
    if user_local.socket.a_socket is None:
        if request.method == 'GET':
            # 跳转到玩家登录界面
            return redirect(url_for('.proto_login'))
        else:
            return json.dumps({"response": -3})
    proto_socket = user_local.socket
    test = request.values.get('request')
    if test == 'js_system_choose':
        system = request.values.get('system')
        system_proto_list = proto_socket.get_xieyi_list(system)
        if system_proto_list:
            return json.dumps({"response": 9, "list": system_proto_list})
        else:
            return json.dumps({"response": 10, "list": system_proto_list})
    elif test == 'js_proto_choose':
        proto = request.values.get('proto')
        proto_info = proto_socket.get_shuoming_info(proto)
        if proto_info:
            return json.dumps({"response": 11, "info": proto_info})
        else:
            return json.dumps({"response": 12, "info": proto_info})
    elif test == 'js_send_proto':
        c2s = request.values.get('c2s')
        values = request.values.get('values')
        counts = request.values.get('counts')
        try:
            proto_socket.send_c2s_values(c2s, values, int(counts))
            send_state = True
        except:
            send_state = False
        if send_state:
            return json.dumps({"response": 13})
        else:
            return json.dumps({"response": 14})
    elif test == 'js_check_code':
        code = request.values.get('code')
        code_info = proto_socket.get_jieguoma(code)
        if code_info:
            return json.dumps({"response": 15, "info": code_info})
        else:
            return json.dumps({"response": 16, "info": code_info})
    elif test == 'js_send_gm':
        gm = request.values.get('gm')
        proto_socket.send_gm(gm)
        gm_state = True
        if gm_state:
            return json.dumps({"response": 17})
        else:
            return json.dumps({"response": 18})
    elif test == 'js_check_details':
        fuc = request.values.get('fuc')
        fuc_info = proto_socket.get_xiangqing(int(fuc))
        if fuc_info is True:
            detail_dict = proto_socket.recv_xiangqing(int(fuc))
            print detail_dict
            if detail_dict is not None:
                detail_info = proto_socket.trans_xiangqing(detail_dict)
                return json.dumps({"response": 19, "info": detail_info})
            else:
                return json.dumps({"response": 20, "info": u"没有收到对应的协议消息"})
        else:
            # 没有找到对应的协议
            return json.dumps({"response": 20, "info": u"没有找到对应的协议名"})
    elif test == 'js_game_logout':
        if user_local.socket:
            user_local.socket.close_socket()
            user_local.socket = None
        return json.dumps({"response": 21})
    elif test == 'js_request_nickname':
        # 获取玩家昵称
        proto_socket.send_player_name()
        nickname = proto_socket.recv_player_name()
        return json.dumps({"response": 22, "info": nickname})
    else:
        msg = msg_dict_queue[session.get('username')]
        ws = Real_webSocketServer(socketServer, msg)
        ws.start()
        # 开启接收线程(在线程不存在或者线程已结束时)
        if user_local.thread is None or user_local.thread.result is False:
            print u'创建循环接受消息的线程'
            t = SocketThread(func=proto_socket.recv_proto_for_loop, args=(msg, ws))
            t.start()
            user_local.thread = t
        xitonglist = proto_socket.get_xitong_list()
        gongnenglist = proto_socket.get_gongneng_list()
        proto_main_dict = {'xitonglist': xitonglist,
                           'gongnenglist': gongnenglist,
                           'project': g.proto_project,
                           'server': g.proto_server_name,
                           'username': g.proto_username}
        return render_template('proto/proto_main.html', **proto_main_dict)


@proto.route('/code_pic', methods=['GET','POST'])
def code_pic():
    if request.method == 'POST':
        path = request.base_url.split("code_pic")[0]
        return path


@proto.before_request
def before_request():
    if not session.get('username'):
        if request.method == 'GET':
            # 跳转到登录界面
            return redirect(url_for('login'))
        else:
            return json.dumps({"response": -1})
    if request.path in ['/choose_server', '/proto_test', '/proto_login', '/proto_regist'] \
            and not session.get('proto_project'):
        if request.method == 'GET':
            # 跳转到选择界面
            return redirect(url_for('.choose_proto_project'))
        else:
            return json.dumps({"response": -2})
    if request.path in ['/proto_test'] and not session.get('proto_username'):
        if request.method == 'GET':
            # 跳转到玩家登录界面
            return redirect(url_for('.proto_login'))
        else:
            return json.dumps({"response": -3})
    g.username = session.get('username')
    g.proto_project = session.get('proto_project')
    g.proto_server_name = session.get('proto_server_name')
    g.proto_username = session.get('proto_username')


