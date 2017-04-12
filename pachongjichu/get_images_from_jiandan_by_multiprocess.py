#!/usr/bin/env python
#coding=utf-8
from multiprocessing.dummy import  Pool as  ThreadPool
import urllib
import  urllib2
from lxml import  etree
import  requests
import os
import  time
from bs4 import  BeautifulSoup
class spider(object):
    def __init__(self):
        self.User_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    def get_html(self,url):
        html = requests.get(url)
        html_format= etree.HTML(html.text)
        content = html_format.xpath('//div[@class="text"]/p/a/@href')
        return content
    def save_image(self,content):
        path1 = 'jiandan/xpath/images1'
        if not os.path.exists(path1):
            os.makedirs(path1)
        else:
            for image_url in content:
                name = str(image_url).split('/')[-1]
                target = path1 +'/'+name
                print 'downloading '+name
                image = urllib.urlretrieve('http:'+image_url,target)

    def run(self):
        print 'Begin to downloading images'
        path = 'jiandan/xpath/images'
        start_page = 2401
        end_page = 2405
        time1 = time.time()
        for pageNum in range(start_page,end_page+1):
            content = self.get_html(pageNum)
            self.save_image(content,path)
        print 'images download done'
        time2 = time.time()
        time_used_single = time2 -time1
        print 'single process handle the process used '+str(time_used_single) + 's'
    def multi_process_run(self):
        pool = ThreadPool(4)
        print 'Begin to downloading images'
        urls = []
        start_page = 2401
        end_page = 2405
        for url_num in range(start_page,end_page):
            urls.append('http://jandan.net/ooxx/page-%s#comments'%str(url_num))
        time1 = time.time()
        content = pool.map(self.get_html,urls)
        pool.map(self.save_image,content)
        pool.close()
        pool.join()
        time2 = time.time()
        time_used_multi = time2 - time1
        print 'multi process handle the process used'+ str(time2-time1) + 's'

    print 'images download done'

if __name__ == '__main__':
    spider1 = spider()
    spider1.multi_process_run()

