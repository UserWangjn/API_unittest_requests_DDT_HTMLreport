# coding=utf-8
# @Author: wjn
from api.weather_module.api_1033_weather_query import *
from common.util import *
import unittest


class TestWeatherQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = api_weather_query()

    def test_weather_query_success(self):
        # url = api_weather_query()
        # url = 'http://apis.juhe.cn/simpleWeather/query'
        body = {
            'city': '北京',
            'key': None
        }
        # print('self.url:',self.url)
        res = getInterfaceRes(url=self.url, body=body)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('resultcode'), '101')
        self.assertEqual(res.json().get('reason'), '错误的请求KEY')
        # print(res.json().get('resultcode'))

    def test_weather_fail_city(self):
        pass
