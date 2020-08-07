# -*- coding = utf-8 -*-
# @Time : 2020/8/3 16:25
# @Author : 姚远
# @File : douban.py
# @Software: PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request
import urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

# 影片详情链接规则
findlink = re.compile('<a href="(.*)">')
# 影片图片
findImagSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'')
#


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalit = getData(baseurl)
    # savepath = r'C:\Users\22395\Desktop\\豆瓣电影Top250.xls'


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):      # 获取豆瓣电影TOP 250，每页25个，所以循环10次
        url = baseurl + str(i*25)
        html = askURL(url)      # 每次爬取一次url网页
        # 逐一解析数据
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.find_all("div", class_="item"):
            print(item)
            # item = str(item)
            # data = []       # 保持一部电影的信息
            # link = re.findall(findlink, item)[0]        # 每部电影的超链接
            # print(link)
            break
    # return datalist


# 得到一个指定URL网页内容
def askURL(url):
    # 用户代理，表示告诉服务器，我们是什么样的机器、浏览器（本质上是告诉服务器我们适合接收什么样的数据）
    # 模拟浏览器头部信息，向服务器发送信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 "
    }
    request = urllib.request.Request(url=url, headers=headers)

    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(savepath):
    pass


if __name__ == '__main__':
    main()
