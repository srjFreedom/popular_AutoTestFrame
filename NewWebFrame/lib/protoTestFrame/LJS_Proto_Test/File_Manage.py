# -*- coding: UTF-8 -*-
import os,sys,time,json,re
import xlrd
from xlutils.copy import copy

class File_Manage():

    def get_filename_all(self):
        """
        从文件夹目录中遍历所有xlsx文件并返回
        :return: 
        """
        path = os.path.join(os.path.dirname(sys.argv[0]),'testcases')
        dirlist = os.listdir(path)
        filelist = []
        for index in range(len(dirlist)):
            if dirlist[index].find(".xls") > 0:
                filelist.append(dirlist[index])
        return filelist

    def get_sheetname_all(self,xlsName):
        """
        从指定xls文件中获取所有表单名并返回
        :return: 
        """
        path = os.path.join(os.path.dirname(sys.argv[0]), 'testcases', xlsName)
        try:
            bk = xlrd.open_workbook(path)
        except:
            raise BaseException, u"表格文件不存在，请检查"
        sheetName = bk.sheet_names()
        return sheetName

    def read_params_from_excel(self, xlsName, sheetName):
        """
        从表格中读取参数，具体做法是先确定参数在哪几列，
        然后在每一行读取该行的所有参数作为参数列表，加上该行的协议号，组成字典，
        最后把每一行的字典组合成列表返回
        :return: 列表形式返回
        """
        params_name_list = []
        params_list = []
        min_col = 8
        max_col = 8
        path = os.path.join(os.path.dirname(sys.argv[0]), 'testcases', xlsName)
        try:
            bk = xlrd.open_workbook(path)
        except:
            raise BaseException, u"表格文件不存在，请检查"
        try:
            sh = bk.sheet_by_name(sheetName)
        except:
            raise BaseException, u"表格页签不存在，请检查"
        # 先确定有几列
        for i in xrange(min_col, sh.ncols):
            if sh.cell_value(0, i) == u"参数说明":
                max_col = i
                break
            params_str = sh.cell_value(0, i)
            params_name_list.append(params_str)

        for i in xrange(1, sh.nrows):
            params_dic = {}
            if min_col == max_col:
                #协议无参数，不在字典里进行保存
                pass
            else:
                values = []
                for j in xrange(min_col, max_col):
                    params_value = sh.cell_value(i, j)
                    if isinstance(params_value, unicode):
                        if '[' in params_value:
                            params_str = eval(str(params_value))
                        else:
                            params_str = params_value
                    else:
                        #科学计数法取整
                        dot_right = str(params_value).split('.')[1]
                        if 'e' in dot_right:
                            params_str = int(params_value)
                        else:
                            p_dot = r'[1-9]'
                            if re.search(p_dot, dot_right):
                                params_str = params_value
                            else:
                                params_str = int(params_value)
                    values.append(params_str)
                params_dic.setdefault(u"values", values)
            c2s = sh.cell_value(i, 1)
            params_dic.setdefault(u"c2s", c2s)
            s2c = sh.cell_value(i, 2)
            params_dic.setdefault(u"s2c", s2c)
            params_list.append(params_dic)
        return params_list

    def write_result(self, xls, sheet, row, col, value):
        """
        在表格中填写结果，具体做法是复制出来填写后再覆盖保存到原文件
        :param row: 所在行
        :param col: 所在列
        :param value: 值
        :return: 
        """
        path = os.path.join(os.path.dirname(sys.argv[0]), 'testcases', xls)
        try:
            old_excel = xlrd.open_workbook(path)
        except:
            raise BaseException, u"表格文件不存在，请检查"
        new_excel = copy(old_excel)
        ws = new_excel.get_sheet(sheet)
        ws.write(row, col, value)
        new_excel.save(path)

    def get_response_from_txt(server, resultName):
        """
        从txt文件中读取指定协议号的内容，持续6秒
        :param server: 协议号，通常以s开头
        :return: 协议返回数据
        """
        responses = []
        if os.path.exists(resultName):
            with open(resultName, 'r') as f:
                for line in f.readlines():
                    if line.find(server) > -1:
                        values = re.findall(r'{.*}', line)
                        print values[0]
                        responses.append(values[0])
            try:
                os.remove(resultName)
            except:
                print u"txt文件删除失败，再次尝试"
                os.remove(resultName)
        return responses

    # def set_gm(gm):
    #     """
    #     预置条件，使用gm达成
    #     :param gm:
    #     :return:
    #     """
    #     if not gm:
    #         return
    #     slg = slgCMPcommand()
    #     if u'yb' in str(gm):
    #         gm = str(gm).split(u'yb')[1] + u','
    #         p = r'(\d+?)[,，]'
    #         num_list = re.findall(p, gm)
    #         print num_list
    #         num = int(num_list[0])
    #         slg.slg_gm_sz_gold(num)
    #     time.sleep(2)

if __name__ == '__main__':
    obj = File_Manage()
    obj.write_result("shangcheng.xlsx","Sheet1",1,1,"asdas")