#!/usr/bin/env python
#-*- coding:utf-8 -*-
from core import info_collection
from conf import settings

import json
import time
import urllib.parse
import urllib.request

class ArgvHandler:
    def __init__(self,args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        '分析参数,如果有参数指定的方法,则执行该功能，如果没有打印帮助说明'
        if len(self.args) > 1 and hasattr(self,self.args[1]):
            if self.args[1] == 'parse_args':
                exit(self.help())
            func = getattr(self,self.args[1])
            func()
        else:
            self.help()

    @staticmethod
    def help():
        '''
        帮助说明:
        :return:
        '''
        msg = '''
                参数名           功能
                collect_data    测试收集硬件信息的功能
                report_data     收集硬件信息并汇报
              '''
        print(msg)

    @staticmethod
    def collect_data():
        '''收集硬件信息,用于测试'''
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        print(asset_data)

    @staticmethod
    def report_data():
        '''收集硬件信息,发送服务器'''
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        data = {'asset_data':json.dumps(asset_data)}
        url = "http://{}:{}{}".format(settings.Params['server'],settings.Params['port'],settings.Params['url'])
        print('数据往{},发送'.format(url))
        try:
            #使用python内置urllib.request库,发送post请求
            #需要将数据进行封装,并转换成Bytes类型
            data_encode = urllib.parse.urlencode(data).encode()
            response = urllib.request.urlopen(url=url,data=data_encode,timeout=settings.Params['request_timeout'])
            message = response.read().decode()
            print('服务器返回结果: %s' % message)
        except Exception as e:
            message = "发送失败，错误原因:{}".format(e)
            print(message)
        with open(settings.PATH,'ab') as f:
            log = "发送时间:{},URL地址{},\n返回结果{}\n".format(time.strftime('%Y-%m-%d %H:%M:%S'),url,message)
            f.write(log.encode())
            print('日志记录成功')