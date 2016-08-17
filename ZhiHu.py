# -*- coding:utf-8 -*-
# import asyncio

__author__ = 'Jack'
import cookielib
import re, urllib, urllib2


class Zhuhu(object):
    def __init__(self):
        self.baseUrl = 'https://www.zhihu.com/login/email'
        self.loginUrl = 'https://www.zhihu.com/#signin'
        self.cookies = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.loginHeaders = {
            'Host': 'www.zhihu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.zhihu.com/',
            'Cookie': 'q_c1=d5f683773a534f89bee418e870c5a544|1469586239000|1469586239000; l_cap_id="ODhiNGY1NmFjYTI5NGJlMjk1YTNhNzhhYmE3Y2QwMWI=|1471276434|b12f373748dc7023bc6234a73224a6f2c08fd863"; cap_id="MmFjOWUxZDQyOTc0NGQzYmFlMGIwMzA3ZGUwMGZhMTc=|1471276434|766ca747e1eccb61a69d45ae2a44298a22f0a920"; d_c0="AHCA5UyeSgqPTj1ClBHf3aZ5YhtGBv6LEwQ=|1469586245"; __utma=51854390.2041924003.1471276395.1471276395.1471276395.1; __utmz=51854390.1471276395.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); login="NzVjYTIxYzJlM2IwNDRjMWJiNDI0ZTI5YmE1Y2ZjYzc=|1471276679|bafc8a13afe55125423bb49b1ab337db298bad11"; _zap=5aed987a-56fb-4d9c-93b6-3dcc4e862aee; _za=952eff98-87b6-458d-969f-ad0fe4c507a6; _xsrf=d01c8d8973e105b2d2ed2ff45bec7fc2; __utmb=51854390.4.10.1471276395; __utmc=51854390; __utmv=51854390.000--|2=registration_date=20140909=1^3=entry_date=20160727=1; __utmt=1; n_c=1; a_t="2.0AABAxds2AAAXAAAAiHPZVwAAQMXbNgAAAHCA5UyeSgoXAAAAYQJVTYdz2VcAL9HhvhMaASzgkE4bb5sqZOyZyB5Bk3M8kDRK0XsBN2mqDfnhn2Ahtw=="; z_c0=Mi4wQUFCQXhkczJBQUFBY0lEbFRKNUtDaGNBQUFCaEFsVk5oM1BaVndBdjBlRy1FeG9CTE9DUVRodHZteXBrN0puSUhn|1471276680|cb6cf0a20969c690085375da2b0b992743d6999b',
            'Connection': 'keep-alive',
        }
        self.loginPostData = urllib.urlencode({
            '_xsrf': 'd01c8d8973e105b2d2ed2ff45bec7fc2',
            'password': 'zsw19941202.',
            'captcha': 'cn',
            'remember_me': 'true',
            'email': '846204062@qq.com',

        })

    # 登录进知乎
    def login(self):
        try:
            request = urllib2.Request(self.baseUrl, self.loginPostData, self.loginHeaders)
            request1 = urllib2.Request(self.loginUrl)
            # request2 = urllib2.Request('https://www.zhihu.com/people/zhu-shi-wen-11')
            result = self.opener.open(request)
            result = self.opener.open(request1)
            # result = self.opener.open(request2)
            self.second(result)

            # print result.read().decode('utf-8')
        except urllib2.URLError, e:
            print '错误原因', e.reason
    @asyncio.coroutine
    def second(self, result):
        try:
            # result = result
            request1 = urllib2.Request(self.loginUrl)
            result = self.opener.open(request1)
            print result.read().decode('utf-8')
        except urllib2.URLError, e:
            print '错误原因', e.reason


zhuhu = Zhuhu()
zhuhu.login()
