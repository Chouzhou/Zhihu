# -*- coding:utf-8 -*-
__author__ = 'Jack'
import cookielib
import re, urllib, urllib2


class Zhuhu(object):
    def __init__(self):
        self.LoginUrl = 'https://www.zhihu.com/login/email'
        self.cookies = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.loginHeaders = {
            'Host': 'www.zhihu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Xsrftoken': 'd01c8d8973e105b2d2ed2ff45bec7fc2',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.zhihu.com/',
            'Content-Length': '118',
            'Cookie': 'q_c1=d5f683773a534f89bee418e870c5a544|1469586239000|1469586239000; l_cap_id="ZmE3Zjg1MWQzNmZlNDc1Njg1YTQxNmQ3MDk0MzIwODM=|1471261220|1c13d6416ad8405882f8e78eba1ee3c68c17bc79"; cap_id="YjkwNDc3NjQwYTM0NDQ3OThhODYwNzJmNzU2ODQwNTM=|1471261220|168349a88424eca7ad8f8d360fbf9849453927be"; d_c0="AHCA5UyeSgqPTj1ClBHf3aZ5YhtGBv6LEwQ=|1469586245"; __utma=51854390.795653221.1470380498.1470380498.1471261223.2; __utmz=51854390.1471261223.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; login="YjczMjlmODBhNzhhNDIwZWE3YTJmZWFkMTVjNmYyOTU=|1469586258|923fc577f29f654368b72e50edbc0977752ea149"; _zap=5aed987a-56fb-4d9c-93b6-3dcc4e862aee; _za=952eff98-87b6-458d-969f-ad0fe4c507a6; _xsrf=d01c8d8973e105b2d2ed2ff45bec7fc2; __utmv=51854390.000--|2=registration_date=20140909=1^3=entry_date=20160727=1; n_c=1; __utmb=51854390.2.10.1471261223; __utmc=51854390; __utmt=1',
            'Connection': 'keep-alive',
        }
        self.loginPostData = urllib.urlencode({
            '_xsrf': 'd01c8d8973e105b2d2ed2ff45bec7fc2',
            'password': 'zsw19941202.',
            'captcha': 'cn',
            'remember_me': 'true',
            'email': '846204062@qq.com',

        })

    def login(self):
        try:
            request = urllib2.Request(self.LoginUrl, self.loginPostData, self.loginHeaders)
            result = self.opener.open(request)
            print result.read().decode('gbk')
        except urllib2.URLError, e:
            print '错误原因', e.reason


zhuhu = Zhuhu()
zhuhu.login()
