# -*- coding: utf-8 -*-

from flask import Flask, session, redirect, url_for, render_template, request
from lib import *
from backstage_for_flask import bak
from proto_flask import proto
from project_manege_flask import pjm

app = Flask(__name__)
app.secret_key = '0501#$%yanLONG/.,kEjI2018'
app.register_blueprint(bak, url_prefix='/index')
app.register_blueprint(proto, url_prefix='/')
app.register_blueprint(pjm, url_prefix='/pjm')

@app.before_request
def msg_save():
    if session.get('username'):
        msg_dict_pipe.setdefault(session.get('username'), Msg_for_pipe())
        msg_dict_queue.setdefault(session.get('username'), Msg_for_queue())

@app.route('/')
def urlForLogin():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session.pop('username', None)
        session.pop('password', None)
        session.permanent = True
        app.permanent_session_lifetime = 1800
        return render_template('/login/login.html')
    elif request.method == 'POST':
        loginLimit = LoginVerify().isUser(request.form['username'], request.form['password'])
        if loginLimit:
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if not session.get('username'):
        return redirect(url_for('login'))
    else:
        return render_template('index/index.html',
                                username=session.get('username'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888', threaded=True)