# -*- coding = utf-8 -*-
# @Time : 2020/8/5 17:51
# @Author : 姚远
# @File : snake.py
# @Software: PyCharm
import time
import random
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import zlib


def askURL(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_abcde_qweasd=0; bdshare_firstime=1596611204140; _abcde_qweasd=0; UM_distinctid=173bdf266bc70-0a5bbd6ce68c0c-3323765-100200-173bdf266bd31; CNZZDATA1253551727=1147383722-1596616436-%7C1596616436; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1596619541,1596622064,1596625937,1596627534; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1596628396",
        "Host": "www.xbiquge.la",
        "If-Modified-Since": "Tue, 24 Mar 2020 20:45:11 GMT",
        'If-None-Match': 'W/"5e7a7157-6152"',
        "Referer": "http://www.xbiquge.la/10/10489/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS).decode('utf-8')
    # html = response.read().decode('utf-8')
    bs = BeautifulSoup(html.replace('&nbsp;', ' '), 'html.parser')
    urlList = []
    for item in bs.select("div > #list > dl >dd >a"):  # 通过id来查找
        urlList.append(str(item.get('href')))
    return urlList


def getData(url):
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "_abcde_qweasd=0; bdshare_firstime=1596611204140; _abcde_qweasd=0; UM_distinctid=173bdf266bc70-0a5bbd6ce68c0c-3323765-100200-173bdf266bd31; CNZZDATA1253551727=1147383722-1596616436-%7C1596616436; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1596619541,1596622064,1596625937,1596627534; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1596628396",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = zlib.decompress(response.read(), 16 + zlib.MAX_WBITS).decode('utf-8')
    # html = response.read().decode('utf-8')
    bs = BeautifulSoup(html.replace('&nbsp;', ' '), 'html.parser')
    title = bs.select('h1')
    item = bs.select('body> div> div> div> #content')
    # a = random.randint(1, 4)
    time.sleep(2)
    return [title[0].text, item[0].text]


def main():
    url = 'http://www.xbiquge.la/10/10489/'
    urlList = askURL(url)
    flag_j = input("是否重新下载所有章节(yes or no):")
    if flag_j == 'yes':
        f = open("./snake.txt", "w")
        flag_i = 0
    elif flag_j == 'no':
        f = open("./snake.txt", "a+")
        flag_i = int(input("请输入需要起始下载的章节数："))
    flag = 0
    for item in urlList:
        if flag == flag_i:
            print("--------------------------------------------")
            print(flag, flag_i)
            flag_i += 1
            flag += 1
            # item_html = askURL("http://www.xbiquge.la/10/10489/4534454.html")
            dataList = getData('http://www.xbiquge.la' + item)
            f.seek(0, 2)
            f.write(dataList[0] + '\n')
            f.write(dataList[1] + '\n\n')
            print(dataList[0].replace('正文卷 ', '') + '爬取成功')
        else:
            flag += 1


if __name__ == '__main__':
    main()
