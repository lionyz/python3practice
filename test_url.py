import gevent
from gevent import monkey
monkey.patch_all()
import requests
import queue
#from pathlib import Path
import urllib3
urllib3.disable_warnings()

url_list = []
url_que = queue.Queue()

with open("E:\\编程\\python练习\\常用库练习\\gevent\\url1.txt","r",encoding="utf-8") as f:
    url_list = f.readlines()

def test_url():
    try:
        while not url_que.empty():
            url1 = url_que.get()
            url_status = requests.get(url=url1,verify=False,timeout=2)
            if url_status.status_code == 200:
                print("%s is open"%url1)
    except error as err:
        print(err)

for i in range(len(url_list)):
    url = url_list[i].split()[0]
    url_all = 'https://' + url
    url_que.put(url_all)

while not url_que.empty():
    all_task = [gevent.spawn(test_url) for i in range(3)]
    gevent.joinall(all_task)
