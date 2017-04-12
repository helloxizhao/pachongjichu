#!/usr/bin/env python
#coding = utf-8
import  urllib2
import urllib
import re
import os
class spider(object):
    def __init__(self):
        self.url = 'http://jandan.net/ooxx/page-%s#comments'
        self.User_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'


    def get_content(self,page):
        try:
            headers = {'User-Agent':self.User_agent}
            request = urllib2.Request(url=self.url%str(page),headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e :
            print e
            exit()
        except urllib2.URLError as e :
            print 'network is wrong'
            exit()

    def get_data(self,content):
        pattern = re.compile('class="view_img_link">.*?</a><br /><img src="//(.*?)" /></p>', re.S)
        image_info = re.findall(pattern,content)
        return image_info

    def save_image_info(self,data,pic_path):
        if not os.path.exists(pic_path):
            os.makedirs(pic_path)
        for imageurl in data:
            name = str(imageurl).split("/")[-1]
            target = pic_path+'/'+name
            print type(target)
#            image = urllib.urlretrieve('http://'+imageurl,target)



    def run(self):
        print 'Begin to collect teacher_image info'
        start_page = 2401
        end_page = 2408
        path = 'jiandan/girl_image'
        for page in range(start_page,end_page):
            content = self.get_content(page)
            girl_image_info = self.get_data(content)
            self.save_image_info(girl_image_info,path)
        print 'Collect teacher image info done'


if __name__ == '__main__':
    spider1 = spider()
    spider1.run()

