# coding= utf-8
from testcase.tools import *
import sys,os
class getcommand:
    """
    功能：获取类
    描述：获取包名，界面信息等...     
    """
    def __init__(self):
        pass
    def get_index_min(self,listA):
        """
        获取列表中最小值的位置
        :param listA: 
        :return: 
        """
        val = min(listA)
        index_now = list.index(val)
        return index_now

    def get_testdata(self,filename):
        """
        Function：获取包名等信息
        param:
            filename：文件路径,string
        return: dict
        Author:lxf
        Create Time:2017-06-08
        Update:
        Update Time
        """
        # filename = __file__+'\\'+filename
        dict_data = {}
        with open(filename,'r') as f:
            for line in f.readlines():
                if not line:
                    continue
                line = line.strip()
                titmes =line.split(':')
                strkey = (titmes[0].split('_'))[1]
                strtemp = titmes[1]
                dict_data[strkey] = strtemp
        return dict_data

    def _get_filename(self):
        """
        获取当前文件的文件名
        :return: 
        """
        argv0_list = sys.argv[0].split('\\')
        filename = (argv0_list[len(argv0_list)-1])[0:-3]
        return filename

    def _get_filepath(self):
        """
        获取当前文件路径,绝对路径
        :return: 
        """
        dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
        return dirname

    def get_wait_element(self,path,timeout=10):
        """
        等待控件出现
        :param timeout: 超时时间
        :return: 
        """
        element = None
        t1 = time.time()
        while time.time()-t1<timeout:
            try:
                element = engine.find_element(path)
            except WeTestRuntimeError as e:
                logger.warn(e)
                print(u"获取控件失败...")
            if element:
                return element

    def get_elements_click_by_name(self, path,timesleep=2, **kwargs):
        """
        Function：按照路径名获取控件
        param:
            name：string，路径名
        return: bool
        Author:lxf
        Create Time:2017-06-08
        Update:
        Update Time：
        """
        element = find_elment_wait(path)
        if element is not None:
            logger.debug("Button:{0}".format(element))
            result = engine.click(element)
            time.sleep(timesleep)
            if result:
                return True
            else:
                print u'本次操作无效，将再次点击'
                result = engine.click(element)
                time.sleep(timesleep)
                if not result:
                    result = engine.click(element)
                    if not result:
                        report.screenshot()
                        raise BaseException, u'点击此控件无效，已经截图'
        else:
            element = find_elment_wait(path)
            if element is not None:
                result = engine.click(element)
                if not result:
                    report.screenshot()
                    raise BaseException,u'未获取到此控件'

    def get_elments_click_by_txt(self,path,name,timesleep=2,**kwargs):
        """
        Function：按照路径名和控件txt
        param:
            path: 字符串  控件路径
            name：字符串 控件txt
        return: bool
        Author:lxf
        Create Time:2017-06-09
        Update:
        Update Time：
        """
        path_txt = path + '{txt=%s}' % name
        element = engine.find_elements_path(path_txt)
        if len(element) > 0:
            result = engine.click(element[0])
            time.sleep(timesleep)
            if result:
                return True
            else:
                element = engine.find_elements_path(path_txt)
                result = engine.click(element[0])
                time.sleep(timesleep)
                if result:
                    return True
                else:
                    report.screenshot()
                    raise BaseException, u'点击此控件无效，已经截图'
        else:
            report.screenshot()
            raise BaseException,u'未获取到此控件'


    def get_elments_click_by_img(self, path, img, **kwargs):
        """
        Function：按照路径名和控件txt
        param:
            path: 字符串  控件路径
            img：字符串 img名称
            check:Boolean 检查当前控件是否还存在
        return: bool
        Author:lxf
        Create Time:2017-06-09
        Update:
        Update Time：
        """
        check = kwargs.get('check',False)
        path_txt = path + '{img=%s}' % img
        element = engine.find_elements_path(path_txt)
        if len(element) > 0:
            result = engine.click(element[0])
            time.sleep(2)
            if result:
                return True
            else:
                result = engine.click(element[0])
                time.sleep(2)
                if result:
                    return True
                else:
                    report.screenshot()
                    raise BaseException, u'点击此控件无效，已经截图'
        else:
            report.screenshot()
            raise BaseException,u'未获取到此控件'

    def get_find_element_by_img(self,path,img):
        """
        通过img获取控件
        :param path: 
        :param img: 
        :return: 
        """

        path_txt = path + '{img=%s}' % img
        # val = find_elment_wait(name=path_txt, max_count=5)
        element = engine.find_elements_path(path_txt)
        if len(element)>0:
            return element
        return None

    def get_find_element(self,path):
        """
        检查控件是否存在，不做错误处理
        :param path: 
        :return: 
        """
        element = engine.find_element(path)
        if element is not None:
            print(u"该控件存在:%s"%path)
            return True
        else:
            print(u"该控件不存在：%s"%path)
            return False

    def get_elments_click_by_index(self, path, index=0, sleeptime=2,**kwargs):
        """
        Function：按照路径名和控件txt
        param:
            path: 字符串  控件路径
            index：整型 点击的索引
        return: bool
        Author:lxf
        Create Time:2017-06-09
        Update:
        Update Time：
        """
        element = engine.find_elements_path(path)
        if len(element) > 0:
            result = engine.click(element[index])
            time.sleep(sleeptime)
            if result:
                return True
            else:
                result = engine.click(element[index])
                time.sleep(sleeptime)
                if result:
                    return True
                else:
                    report.screenshot()
                    raise BaseException, u'点击此控件无效，已经截图'
        else:
            report.screenshot()
            raise BaseException,u'未获取到此控件'

    def get_elements_text_by_name(self,path,text='',**kwargs):
        """
        Function：获取控件text
        param:
            path: 字符串  控件路径
         return: 字符串
        Author:lxf
        Create Time:2017-06-09
        Update:
        Update Time：
        """
        path_txt = path + '/*{txt=%s}' % text
        element = engine.find_elements_path(path_txt)
        if len(element) > 0:
            text = engine.get_element_text(element[0])
            return text
        else:
            report.screenshot()
            raise BaseException, u'此控件不存在'

    def get_Checkelements_by_txt(self,path,name,**kwargs):
        """
        Function：通过控件及txt获取控件
        param:
            path: 字符串  控件路径
            name: 字符串 控件txt信息
         return: 字符串
        Author:lxf
        Create Time:2017-06-09
        Update:
        Update Time：
        """
        path_txt = path + '{txt=%s}' % name
        element = engine.find_elements_path(path_txt)
        if len(element) == 0:
            return False
        else:
            return True

    def get_elements_text_by_onlyElement(self,path):
        """
        Function：获取控件text
        param:
            path: 字符串  控件路径
         return: 字符串
        Author:lxf
        Create Time:2017-06-09
        Update:
        Update Time：
        """
        element = engine.find_element(path)
        if element is not None:
            text = engine.get_element_text(element)
            return text
        else:
            return False

    def get_txtlist_by_elements(self, path):
        """
        获取txt 文字信息
        :param path: 字符串 路径或名称
        :return: 列表
        """
        elements = engine.find_elements_path (path)
        list_info = []
        if len(elements) > 0:
            for element in elements:
                txt = engine.get_element_text (element)
                list_info.append (txt)
        else:
            report.screenshot ()
            raise BaseException, u'此控件不存在'
        return list_info

    def get_screen_size(self):
        """ 
        获取屏幕尺寸
        :return: 
        """
        size = device.get_display_size()
        val = size.__str__().split(',')
        width = val[0].split('=')[1].strip()
        height = val[1].split('=')[1].strip()
        screenSize = {'width':float(width),'height':float(height)}
        return screenSize

    def get_text_by_path(self,path):
        """        
        :param path: 字符串 路径
        :return: 
        """
        listInfo = []
        element = engine.find_elements_path(path)
        for e in element:
            txt = engine.get_element_text(e)
            listInfo.append(txt)
        return listInfo

    def get_check_element(self,path):
        """
        
        :param path: 
        :return: 
        """
        val = find_elment_wait(path)
        if val is None:
            report.screenshot()
            raise BaseException,u'等待的控件未出现，无法继续运行，请检查环境'
        else:
            return val
    def get_index_by_path_name(self,path,name):
        """
        当控件很多时，获取指定文字的控件索引位置
        :param path:字符串 控件路径或名称名称 
        :param name: 字符串 需要检查的信息（特别说明：GA很多信息为unicode编码，检查文字时可以传入Unicode编码的形式） 
        :return: 
        """
        list1 = []
        elements = engine.find_elements_path(path)
        for e in elements:
            txt = engine.get_element_text(e)
            list1.append(''.join(txt))
        if name in list1:
            x = list1.index(name)
            return x
        else:
            report.screenshot()
            raise BaseException,u'查询的信息不存在'

    def get_data_set(self,name,level,m):
        """
        配置表里面查询城建中建筑物的标准信息
        :param name: 建筑物名称
        :param level: 建筑物等级
        :param m: 整型,取值,1:对匠人CD消耗 2:银两消耗 3:粮草消耗 4:需要占领城市的个数
        :return: 
        """
        #查找的建筑物级其等级
        list_name = {'君主府':'BUILDING_PALACE','银矿':'BUILDING_SILVERMINE'
                        ,'民居':'BUILDING_DWELLINGS','兵营':'BUILDING_BARRACKS'
                        ,'校场':'BUILDING_DRILLING_GROUND','拜将厅':'BUILDING_BAR'
                        ,'天策府':'BUILDING_TECHNOLOGY','医疗所':'BUILDING_HOSPITAL'
                        ,'烽火台':'BUILDING_FIRETOWER','城墙':'BUILDING_WALL'}
        str_ar = '(?' + list_name[name] +','+str(level)+')'
        list1 = []
        file=os.path.abspath('.')
        if 'SLG_Newer' not in file:
            file = file +r'\SLG_Newer'+r'\data_building_level.erl'
        else:
            file = file + r'\data_building_level.erl'
        f = open(file,'r')
        number = 0
        info = ''
        value = ''
        for num,value in enumerate(f):
            if str_ar in value:
                number = num+1
            if number == num:
                val1 = str(value.strip())
                info = val1.split('build_cost')
        val = (list(info))[1].split(',')[int(m)]
        print u'当前等级升级需要信息:',val
        f.close
        return int(val)

    def _check_find_timeout(self,name):
        """
        检查查找控件是否超时
        :param name: 
        :return: 
        """
        timeout = 0
        flag = True
        while flag:
            val = engine.find_element(name)
            val_list = engine.find_elements_path(name)
            if val is not None or len(val_list)>0:
                time.sleep(1)
                timeout = +1
                flag = False
            if timeout ==20:
                report.screenshot()
                raise BaseException,u'20秒未找到，超时'

    def get_img_name(self,name):
        """
        获取图片名称
        :param name: 字符串 控件名或者路径
        :return: 
        """
        element = engine.find_element(name)
        if element is not None:
            imgname = engine.get_element_image(element)
            return imgname
        else:
            report.screenshot()
            raise BaseException,u'控件不存在，请检查控件获取是否正确'

    def get_imglist_name(self,path):
        """
        获取相同控件名所有图片
        :param path: 
        :return: 
        """
        elements = engine.find_elements_path(path)
        imglist = []
        if len(elements)>0:
            for element in elements:
                imgname = engine.get_element_image(element)
                imglist.append(imgname)
            return imglist
        else:
            report.screenshot()
            raise BaseException, u'控件不存在，请检查控件获取是否正确'

    def get_element_by_name(self,path):
        """
        查找控件
        :param path: 
        :return: 
        """
        element = engine.find_element(path)
        if element is not None:
            return element
        else:
            print(u"此控件不存在，将继续后面的操作")
            return None

    def get_elements_by_paths(self,path):
        """
        通过路径或者控件获取Elements控件列表信息
        :param path: 
        :return: 
        """
        elements = engine.find_elements_path(path)
        if len(elements) > 0:
            return elements
        else:
            report.screenshot()
            print(u"此控件不存在，将继续后面的操作")
            return None

    def get_set_element_offset(self,element,offset=(0,0)):
        """
        设置控件的偏移量
        :param element: 
        :param offset: 
        :return: 
        """
        locator = engine.get_element_bound(element)
        print locator
        point1 = (locator.x + locator.width / 2, locator.y + locator.height / 2)
        print point1
        point = (locator.x + locator.width / 2+offset[0],locator.y + locator.height / 2+offset[1])
        return point

    def get_data_Tech_set(self, name, level, m):
        """
        配置表里面查询科技研究的标准信息
        :param name: 科技名称
        :param level: 科技等级等级
        :param m: 整型,取值,0.科技ID, 1.科技等级, 2.需要的前置科技,3.需要的建筑id,4.需要达到的等级5.需要达到等级的该类型建筑的数量
                            6.需要的升级时间（秒）,7.科技点消耗,8.科技效果	 
        :return: 
        """
        # 查找的建筑物级其等级
        list_name = {'铸币': '0', '玉石': '1'
                    , '轻骑兵强化': '2', '双枪兵强化': '3'
                    , '床弩强化': '4', '刀盾兵强化': '5'
                    , '金甲重骑强化': '6', '统御论': '7'
                    , '枪盾兵强化': '8', '机关木兽强化': '9'
                    , '双刀死士强化': '10', '虎骑兵强化': '11'
                    , '禁卫军强化': '12', '轰天雷强化': '13'
                    , '金刀卫强化': '14','白马义从强化':'15'
                    , '戚家军强化':'16','机关火龙强化':'17'
                    , '金刚强化':'18'}
        str_ar = '(' + list_name[name] + ',' + str (level) + ')'
        list1 = []
        file = os.path.abspath ('.')
        if 'SLG_Tech' not in file:
            file = file + r'\SLG_Tech' + r'\data_building_tech.erl'
        else:
            file = file + r'\data_building_tech.erl'
        print file
        f = open(file, 'r')
        number = 0
        info = ''
        value = ''
        for num, value in enumerate (f):
            if str_ar in value:
                number = num + 1
            if number == num:
                val1 = str (value.strip ())
                info = val1.split ('build_tech,')
                # print info
        val = (list (info))[1].split (',')[int (m)]
        print u'当前等级升级需要信息:', val
        f.close
        return int(val)
