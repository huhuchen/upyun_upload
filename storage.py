#!/usr/bin/env python
#coding:utf-8

from  os.path import dirname, join, abspath
import sys

PREFIX = dirname(abspath(__file__)) 
sys.path.append(PREFIX)

from upyun import UpYun, md5file
from settings import UPYUN_SPACENAME, UPYUN_OPERATOR, UPYUN_PASSWORD, UPYUN_DOMAIN 

class UpyunStore(UpYun):

    def __init__(self, bucket, username, password, domain):
        super(UpyunStore, self).__init__(bucket, username, password)
        self.domain = domain

    def url(self, path):
        return 'http://%s.%s/%s' % (self.bucket, self.domain, path)

    #if upload success, return upyun url,else return None
    def upload(self, stream, path):
        self.setContentMD5(md5file(stream))
        a = self.writeFile(path, stream, True) 
        if a:
            return True

    def info(self):    
        width = self.getWritedFileInfo('x-upyun-width')
        height = self.getWritedFileInfo('x-upyun-height')
        return width, height

test_upyun_store = UpyunStore(UPYUN_SPACENAME, UPYUN_OPERATOR, UPYUN_PASSWORD, UPYUN_DOMAIN)
