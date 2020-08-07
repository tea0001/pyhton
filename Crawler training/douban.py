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
findTitle = re.compile(r'<span class="title">(.*?)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findTnq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    # savepath_xls = r'.\\豆瓣电影Top250.xls'
    # saveData(datalist, savepath_xls)
    # savepath_db = "movie.db"
    # saveDataDB(datalist, savepath_db)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 获取豆瓣电影TOP 250，每页25个，所以循环10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 每次爬取一次url网页
        # 逐一解析数据
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.find_all("div", class_="item"):
            item = str(item)
            data = []  # 保持一部电影的信息

            # 影片详细的链接
            link = re.findall(findlink, item)[0]  # 每部电影的超链接
            data.append(link)
            # 影片图片
            imgSrc = re.findall(findImagSrc, item)[0]
            data.append(imgSrc)
            # 影片片名
            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名，没有外国名
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)  # 添加中国名
                otitle = re.sub('(\s+)?/(\s+)?', '', titles[1])  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])  # 添加中国名
                data.append(' ')  # 添加外国名

            # 影片评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 找到评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            # 找到概况
            inq = re.findall(findTnq, item)
            if len(inq) != 0:
                inq = inq[0].replace('。', '')
            else:
                inq = ' '
            data.append(inq)
            # 找到影片的相关内容
            bd = re.findall(findBd, item)[0]

            # bd = re.sub('<br(\s+)?/>(\s+)?', ' ', bd)  # 去掉<br/>
            bd = re.sub('<br/>(\s+)?', ' ', bd)  # 去掉<br/>
            bd = re.sub('/', ' ', bd)  # 替换/这个符号
            data.append(''.join(bd.split()))  # 去掉前后的空格
            datalist.append(data)  # 把处理好的一部电影信息放入datalist
    return datalist


# 得到一个指定URL网页内容
def askURL(url):
    # 用户代理，表示告诉服务器，我们是什么样的机器、浏览器（本质上是告诉服务器我们适合接收什么样的数据）
    # 模拟浏览器头部信息，向服务器发送信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 "
    }
    request = urllib.request.Request(url=url, headers=headers)
    # html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(type(html))
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣Top250', cell_overwrite_ok=True)
    book.save(savepath)
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外国名', '评分', '评价数', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 表格标题（列名）
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])  # 数据
    book.save(savepath)  # 保持到excel中


def saveDataDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:

        for index in range(len(data)):
            if index not in (4, 5):
                data[index] = '"' + data[index] + '"'

        sql = '''
            insert into movie250(info_link, pic_link, cname, ename, score, rated, instroduction, info)
            values (%s)''' % str(','.join(data))
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250(
        id integer  primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar ,
        ename varchar ,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        )
    '''  # 创建数据表movie250
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    print('豆瓣Top250，爬取完毕！')
