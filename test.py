#!/usr/bin/env python
#coding:utf-8

from  os.path import dirname, join, abspath
import sys

PREFIX = dirname(abspath(__file__)) 
sys.path.append(PREFIX)

from storage import test_upyun_store

def test_sotrage():
    filepath = PREFIX + "/test.jpg"
    with open(filepath) as ufile:
        path = "test/test.jpg"
        result = test_upyun_store.upload(ufile, path)
        if result:
            width, height = test_upyun_store.info()
            print "width", width
            print "height", height
            url = test_upyun_store.url(path)
            print "url", url

if __name__ == "__main__":
    test_sotrage()
