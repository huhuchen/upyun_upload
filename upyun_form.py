#!/usr/bin/env python
#coding:utf-8

from  os.path import dirname, join, abspath
from time import time
import hashlib
from base64 import b64encode
import sys

PREFIX = dirname(abspath(__file__)) 
sys.path.append(PREFIX)

from settings import UPYUN_FORM


form_templates  = """
                    <form action='http://v0.api.upyun.com/%(bucket)s' method="POST" enctype="multipart/form-data">
                    <input "type="file" name="file" /> 
                    <input name="policy" type="hidden" value="%(policy)s">
                    <input name="signature" type="hidden" value="%(signature)s">
				    <button type="submit">上传头像</button>
                    </form>
                  """

def upyun_policy_signature(name, return_url, notify_url=""):
    if name in UPYUN_FORM:
        bucket = UPYUN_FORM[name]["bucket"]
        key = UPYUN_FORM[name]["api_key"]
        policy = {
                    'bucket': bucket,
                    'expiration': int(time()) + 360000,
                    'save-key': '/{filemd5}',
                 }
        if return_url.startswith("//"):
            return_url = "http:%s"%return_url
        if notify_url.startswith("//"):
            notify_url = "http:%s"%notify_url
        if notify_url:
            policy['notify-url'] = notify_url
        if return_url:
            policy['return-url'] = return_url
        policy = b64encode(dumps(policy))
        signature = hashlib.md5('%s&%s'%(policy, key)).hexdigest()
        return bucket, policy, signature


##@app.route("/upyuncb/photo")
##def upyuncb_photo():
##    code = request.args.get('code', None)
##    if code == '200':
##        url = request.args.get('url', "")
##        width = request.args.get('image-width', 0)
##        height = request.args.get('image-height', 0)
##        message = request.args.get('message', 0)
##        _time = request.args.get('time', 0)
##        sign = request.args.get('sign', 0)
##        api_key = UPYUN[PHOTO_TYPE_ITEM]["api_key"]
##        signature = hashlib.md5('%s&%s&%s&%s&%s'%(code, message, url, _time, api_key)).hexdigest() 
##        if sign == signature:
##    return redirect(url_for('index'))
