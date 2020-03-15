# -*- coding: utf-8 -*-
# @Author  : wjn
# @File    : get_value.py
# @describe: 配置文件读取

from common.read_config import ReadIni


class GetValue(object):
    # 读取配置文件

    # 获取debug开关的状态
    is_debug = ReadIni(node='MODEL').get_value("debug")