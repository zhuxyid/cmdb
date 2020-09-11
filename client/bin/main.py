#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
完全可以把信息收集做成windows和linux两个不同版本
'''

import os
import sys


BASEDIR = os.path.dirname(os.getcwd())
#设置工作目录,使包和模块正常导入

sys.path.append(BASEDIR)

from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)