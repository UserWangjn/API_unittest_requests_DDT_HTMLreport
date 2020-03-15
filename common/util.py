# coding=utf-8
# @Author: wjn

import requests
import random
import time


class JYRequest():
    def getInterfaceRes_no_cookie(self, url, body):
        '''
        发送post请求,没有前置cookie登录的需要。
        目前只支持post登录，后续优化加入get功能，把method作为入参传进方法。
        :return: 返回Response对象，例如：ret.status_code，ret.json()
        '''
        # url = 'http://apis.juhe.cn/simpleWeather/query'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        # body = {
        #     'city': '北京',
        #     'key': ''
        # }
        res = requests.post(url=url, headers=self.header, data=body)
        return res

    def getInterfaceRes_need_cookie(self, url, body):
        '''
        发送post请求,接口需要前置cookie登录的需要。
        目前只支持post登录，后续优化加入get功能，把method作为入参传进方法。
        :param body:
        :return:
        '''
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.s = requests.session()
        # 之后用self.s发送请求，就会一直保持会话
        res = self.s.post(url=url, data=body, headers=header)
        return res


        '''
        方法二：追加cookie：
        https://www.cnblogs.com/hanmk/p/8907746.html
        第一个接口：
        r = requests.get('登录')
        r.cookies  # 这里就可以获取到登录后返回的cookie
        
        s = requests.Session()  # 开启一个会话Session
        jar = requests.cookies.RequestsCookieJar()   # 创建一个Cookie Jar对象
        jar.set('49BAC005-7D5B-4231-8CEA-1XXXXBEACD67','cktXXXX001')  # 向Cookie Jar对象中添加cookie值
        jar.set('JSESSIONID','F4FFF69B8CXXXX80F0C8DCB4C061C0')
        jar.set('JSESSIONIDSSO','9D49C7XXXX448FDF5B0F294242B44A')
        s.cookies.update(jar)  # 把cookies追加到Session中
        
        
        整体思路：
        比如一共发两个接口，第一个是登录，第二个是发送交易下单，第二个接口中需要第一个接口登录中返回的cookie，
        就可以把第一个接口的返回报文cookie取出，之后set进下一个报文的cookie中
        
        
        方法三：跟方法二思路一样
        https://www.cnblogs.com/hz-blog/p/8150719.html
            def __init__(self):
        self.cookies = requests.cookies.RequestsCookieJar()

        def go(self, url, method, post_data):
                response = requests.request(method, url
                                            , data=post_data
                                            , headers=info.headers
                                            , cookies=self.cookies) #传递cookie
    
                self.cookies.update(response.cookies) # 保存cookie
        '''


class CreateData():
    '''
    在case中如果需要随机创建名字、手机号等测试数据可以使用此类，调用示例：
    def setUp(self):
    self.name = CreateData.create_name()
    self.phone = CreateData.create_phone()
    '''
    @staticmethod
    def create_phone():
        last = random.randint(999999999, 10000000000)
        phone = "9{}".format(last)
        return phone

    @staticmethod
    def create_name():
        last = random.randint(99, 1000)
        name = "AutoTest{}".format(last)
        return name

    @staticmethod
    def get_millis():
        millis = int(round(time.time() * 1000))
        return millis

    @staticmethod
    def create_coursename():
        last = random.randint(99, 1000)
        course_name = "自动化测试{}".format(last)
        return course_name


if __name__ == '__main__':
    req = JYRequest()
    ret = req.getInterfaceRes_no_cookie()
    print(type(ret))
    print(ret.status_code)
    print(ret.json())
    print(type(ret.json()))
