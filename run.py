# coding=utf-8
# @Author: wjn

import unittest
from common import HTMLTestRunnerCN
import time

dir = './case/'
suite = unittest.defaultTestLoader.discover(dir, 'test_*.py')

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    cur_time = time.strftime('%Y-%m-%d %H-%M-%S')
    filePath = './reports/{}report.html'.format(cur_time)
    fp = open(filePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='自动化测试报告',
        description='天气模块测试',
        tester='王佳宁',
        # 显示用例打印内容
        verbosity=2
    )
    '''
    verbosity:
    =1的时候 默认值为1，不限制完整结果，即单个用例成功输出’.’,失败输出’F’,错误输出’E’
    =0的时候。不输出信息
    =2的时候，需要打印详细的返回信息
    '''
    # 运行测试用例
    runner.run(suite)
    # 关闭文件，否则会无法生成文件
    fp.close()
