# coding=utf-8
# @Author: wjn
from config import choice_environment


# @property
def api_weather_query():
    domain = choice_environment.current_url
    api = '/simpleWeather/query'
    url = str(domain) + api
    # body = {
    #     'city': '北京',
    #     'key': None
    # }
    return url
