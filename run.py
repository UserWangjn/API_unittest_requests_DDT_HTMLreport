#coding=utf-8
# @Author: wjn

import unittest
from common import HTMLTestRunnerCN
import time

dir = './case/'
suite = unittest.defaultTestLoader.discover(dir,'test_*.py')



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
        tester='王佳宁'
    )
    # 运行测试用例
    runner.run(suite)
    # 关闭文件，否则会无法生成文件
    fp.close()

