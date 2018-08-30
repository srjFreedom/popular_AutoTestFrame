# -*- coding: utf-8 -*-

from flask import Blueprint, session, redirect, url_for, request, render_template
from lib import *
import json

pjm = Blueprint('pjm',__name__)


@pjm.route('/project_manege', methods=['GET', 'POST'])
def protoMain():
    return render_template('project_manege/project_manege.html')

# 获取服务器数据
@pjm.route('/get_sql', methods=['GET', 'POST'])
def get_sql():
    data =  SqlConnect("sql/webFrame.db").excute("select * from project")
    return json.dumps(data)

@pjm.route('/add_sql', methods=['GET', 'POST'])
def add_sql():
    pro_id = request.values.get("pro_id")
    pro_name = request.values.get("pro_name")
    pro_list = SqlConnect("sql/webFrame.db").excute("select procode from project")
    pro_list_trans = []
    for p in pro_list:
        pro_list_trans.append(p[0])
    print pro_list_trans
    for pro in pro_list_trans:
        if str(pro) == pro_id:
            print "add project fail"
            return "fail"
    else:
        SqlConnect("sql/webFrame.db").commit_excute("insert into project ('procode','proname') values ('"+pro_id+"','"+pro_name+"')")
        print "add project success"
        return "success"

@pjm.route('/delete_sql', methods=['GET', 'POST'])
def delete_sql():
    pro_id = request.values.get("pro_id")
    SqlConnect("sql/webFrame.db").commit_excute("delete from project where procode = '"+pro_id+"'")
    print "delete project success"
    return "success:"+pro_id

