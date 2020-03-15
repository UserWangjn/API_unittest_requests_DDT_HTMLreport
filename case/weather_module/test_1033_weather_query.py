# coding=utf-8
# @Author: wjn
from api.weather_module.api_1033_weather_query import Api1033WeatherQuery
from common.util import JYRequest
import unittest
from common.get_value import GetValue
from common.get_log import LogInfo


class TestWeatherQuery(unittest.TestCase, GetValue, LogInfo):

    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('Weather/query测试用例开始执行')
        api = Api1033WeatherQuery()
        cls.url = api.api_weather_query()
        cls.log.info('URL获取成功, URL:' + cls.url)
        cls.request = JYRequest()

    @LogInfo.get_error
    def test_weather_query_success(self):
        # url = api_weather_query()
        # url = 'http://apis.juhe.cn/simpleWeather/query'
        body = {
            'city': '北京',
            'key': None
        }
        # print('self.url:',self.url)
        res = self.request.getInterfaceRes_no_cookie(url=self.url, body=body)
        # print('res:',type(res))
        res_json = res.json()
        self.log.debug(res_json)
        self.assertEqual(res.status_code, 200, msg='接口返回错误码，code={}'.format(str(res.status_code)))
        self.assertEqual(res_json.get('resultcode'), '101',
                         msg='接口返回错误码，code={}'.format(str(res_json.get('resultcode'))))
        self.assertEqual(res_json.get('reason'), '错误的请求KEY', msg=res_json.get('reason'))
        # print(res.json().get('resultcode'))

    @LogInfo.get_error
    def test_weather_fail_city(self):
        self.assertEqual('1','2')
