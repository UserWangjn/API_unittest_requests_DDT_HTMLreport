# coding=utf-8
# @Author: wjn

import requests


def getInterfaceRes(url, body):
    '''
    发送post请求
    :return: 返回Response对象，例如：ret.status_code，ret.json()
    '''
    # url = 'http://apis.juhe.cn/simpleWeather/query'
    header = {
        'User-Agent': 'Apache-HttpClient/4.5.10 (Java/1.8.0_211)'
    }
    # body = {
    #     'city': '北京',
    #     'key': ''
    # }
    res = requests.post(url=url, headers=header, data=body)
    return res


if __name__ == '__main__':
    ret = getInterfaceRes()
    print(type(ret))
    print(ret.status_code)
    print(ret.json())
    print(type(ret.json()))
