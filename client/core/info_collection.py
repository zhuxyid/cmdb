#-*- coding:utf-8 -*-

import sys
import platform
from plugins.collect_windows_info import Win32Info
from plugins.collect_linux_info import collect


class InfoCollection:
    def collect(self):
        #收集平台信息，
        #根据平台不同执行不同方法
        try:
            func = getattr(self,platform.system().lower())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exti('不支持当前[%s]操作系统!' %platform.system())

    @staticmethod
    def linux():
        return collect()

    @staticmethod
    def windows():
        return Win32Info().collect()

    @staticmethod
    def build_report_data(data):
        '''预留接口'''
        return data