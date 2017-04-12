#!/usr/bin/env python
#coding=utf-8
import  urllib
import urllib2
import  cookielib
from bs4 import BeautifulSoup
def login():
#    url = 'https://passport.csdn.net/?service=http://write.blog.csdn.net/'
    loginUrl = 'http://www.maiziedu.com/user/login/'
    values = {'account_l':'13681412268','password_l':'helloxue123'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode(values)
    result = opener.open(loginUrl,postdata)
    cookie.save(ignore_discard=True,ignore_expires=True)
    listurl = 'http://www.maiziedu.com/home/base/'
    result = opener.open(listurl)
    bsObj = BeautifulSoup(result.read(),'html.parser')
    title = bsObj.body.h2
    return title
if __name__ == '__main__':
    res = login()
    if res == None:
        print 'no result'
    else:
        print res
