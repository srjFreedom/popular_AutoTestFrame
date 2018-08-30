# -*- coding: utf-8 -*-

from flask import Blueprint, session, redirect, url_for, request, render_template
from lib import *

bak = Blueprint('bak',__name__)


@bak.route('/TestPro')
def TestPro():
    tmpType = 0
    func = request.args.get('func')
    if request.args.get('pageCount'):
        pageCount = int(request.args.get('pageCount'))
    else:
        pageCount = 1
    tableList = GetProjectDir().getProject(pageCount)
    proCount = GetProjectDir().getProCount()[0][0]
    tablePageCount = proCount / 10 + 1
    return render_template('index/tables/projectTable/projectTable.html',
                           tmpType=tmpType, tableList=tableList,
                           tablePageCount=tablePageCount, pageCount=pageCount,
                           func=func)

@bak.route('/autoTestReport', methods=['POST', 'GET'])
def autoTestReport():
    if request.method == 'POST':
        reportName = request.form['reportName']
        testRunner = request.form['testRunner']
        projectCode = request.form['projectCode']
        pageCount = request.form['pageCount']
        tmpType = 1
        rpoCount = GetReportDir().getSrcRpoCount(projectCode, reportName, testRunner)[0][0]
        tablePageCount = rpoCount / 10 + 1
        tableList = GetReportDir().getSrcReport(projectCode, pageCount, reportName, testRunner)
        proList = GetProjectDir().getProList()
        nameList = GetUser().getAllUser()
        return render_template('index/tables/reportTable/reportTable.html',
                               tmpType=tmpType, tableList=tableList,
                               tablePageCount=tablePageCount, pageCount=int(pageCount),
                               proList=proList, nameList=nameList,
                               reportName=reportName, testRunner=testRunner,
                               projectCode=projectCode)
    elif request.method == 'GET':
        tmpType = 1
        rpoCount = GetReportDir().getRpoCount()[0][0]
        tablePageCount = rpoCount / 10 + 1
        if request.args.get('pageCount'):
            pageCount = request.args.get('pageCount')
        else:
            pageCount = 1
        tableList = GetReportDir().getReport(pageCount)
        proList = GetProjectDir().getProList()
        nameList = GetUser().getAllUser()
        return render_template('index/tables/reportTable/reportTable.html',
                               tmpType=tmpType, tableList=tableList,
                               tablePageCount=tablePageCount, pageCount=int(pageCount),
                               proList=proList, nameList=nameList)

@bak.route('/autoTestReport/checkReport')
def checkReport():
    reportName = request.args.get('reportName')
    return render_template('index/autoTest/reportResource/' + reportName)

@bak.route('/autoTestScript')
def autoTestScript():
    projectCode = request.args.get('projectCode')
    directorList = Program_director().createDirHtml('D:/Script/'+projectCode)
    return render_template('index/autoTest/scriptsList/autoTestDirector.html',
                           directorList=directorList, projectCode=projectCode)

@bak.route('/autoTestRunner', methods=['GET', 'POST'])
def autoTestRunner():
    if request.method == "POST":
        phone_ip = request.form['phone_ip']
        testRunner = GetUser().getCurrentUser(session.get('username'))[0][0]
        scripts_list = request.form.getlist('scripts_point')
        TransferServer().runServer(phone_ip)
        AutoTestRunnerForWeb(scripts_list, testRunner, phone_ip).start()
        return '自动化运行成功！'
    return redirect(url_for('.index'))

@bak.route('/autoTestLogView')
def autoTestLogView():
    logName = request.args.get('logName')
    requestType = request.args.get('requestType')
    return render_template('index/AutoTest/logView/logView.html',
                           logName=logName, requestType=requestType)

@bak.route('/autoTestLogRun', methods=['GET', 'POST'])
def autoTestLogRun():
    if request.method == "POST":
        logpath = request.form['logName'].split('_')[0]
        logname = logpath + '.log'
        log = open('templates/index/autoTest/reportLog/' + logname, 'r')
        logInfo = log.read()
        log.close()
        return logInfo
    return redirect(url_for('.index'))