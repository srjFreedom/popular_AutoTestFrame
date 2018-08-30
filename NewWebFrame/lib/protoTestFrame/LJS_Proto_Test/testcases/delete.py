# encoding=utf-8

import xlrd
from xlutils.copy import copy
import re
import os


def write_result(xls, sheet):
    """
    在表格中填写空字符，达到删除的效果
    :param row: 所在行
    :param col: 所在列
    :param value: 值
    :return: 
    """
    try:
        old_excel = xlrd.open_workbook(xls)
    except:
        raise BaseException, u"表格文件不存在，请检查"
    try:
        sh = old_excel.sheet_by_name(sheet)
    except:
        raise BaseException, u"表格页签不存在，请检查"
    min_row = 1
    max_row = sh.nrows
    min_col = 4
    max_col = 7
    new_excel = copy(old_excel)
    ws = new_excel.get_sheet(sheet)
    for row in range(min_row, max_row):
        for col in range(min_col, max_col):
            ws.write(row, col, '')
    new_excel.save(xls)


def get_all_xlsname():
    xlsname_list = []
    file_list = os.listdir(os.path.dirname(__file__))
    for each in file_list:
        if '.xls' in each:
            xlsname_list.append(each)
    return xlsname_list


def get_all_sheetname(xls):
    try:
        bk = xlrd.open_workbook(xls)
    except:
        raise BaseException, u"表格文件不存在，请检查"
    return bk._sheet_names


def run_del(xlsName):
    for each_xls in xlsName:
        for each_sheet in get_all_sheetname(each_xls):
            write_result(each_xls, each_sheet)
    print u'清除成功'

xlsName = get_all_xlsname()


if __name__ == '__main__':
    run_del(xlsName)