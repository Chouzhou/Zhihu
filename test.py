import urllib2

request = urllib2.urlopen('https://www.zhihu.com/#signin')
print request.read()
