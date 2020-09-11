#-*- coding:utf-8 -*-

import os

#服务端接收数据
Params = {
    'server':'127.0.0.1',
    'port':8000,
    'url':'/assets/report/',
    'request_timeout':30,
}

#日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()),'logs','cmdb.log')


#配置都收集在此文件中