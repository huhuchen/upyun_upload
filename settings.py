#!/usr/bin/env python
#coding:utf-8

UPYUN_OPERATOR = "admin"
UPYUN_PASSWORD = "passwd"
UPYUN_DOMAIN = "b0.upaiyun.com"

UPYUN_SPACENAME = "spacename"

UPYUN_FORM = {
        "test": {
            "bucket": UPYUN_SPACENAME,
            "api_key": "xxxxxxxxx"
            },
        }

RETURN_URL = "/upyun/return_callback"
NOTIFY_URL = "/upyun/notify_callback"
