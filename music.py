from urllib.request import Request, urlopen
import random
from bs4 import BeautifulSoup
import xlwt

def main():
    html = gethtml('https://music.163.com/discover/toplist?id=19723756')
    music_list = getMusic(html)
    saveMusic(music_list)


def gethtml(url):
    ua_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/84.0.4147.105 Safari/537.36 ',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'
          ]
    ua = random.choice(ua_list)
    req = Request(url=url)
    req.add_header('user-agent',ua)
    with urlopen(req) as response:
        html = response.read().decode('utf-8')
        bs = BeautifulSoup(html, "html.parser")
        item = bs.find_all("ul", class_="f-hide")[0]
    return item


def getMusic(html):
    html = str(html)
    bs = BeautifulSoup(html, "html.parser")
    music_list = []
    for item in bs.select('ul > li >a'):
        music = []
        music.append(item.string)
        music.append('https://music.163.com/#'+item['href'])
        music_list.append(music)
    return music_list


def saveMusic(music_list):
    workbook = xlwt.Workbook(encoding='utf-8')    # 创建wookbook对象
    worksheet = workbook.add_sheet('sheet1')      # 创建工作表
    worksheet.write(0, 0, '音乐名')                # 写入数据，第一个参数‘行’；第二个参数‘列’；第三个参数是内容
    worksheet.write(0, 1, '音乐链接')
    for i in range(len(music_list)):
        worksheet.write(i+1, 0, music_list[i][0])
        worksheet.write(i+1, 1, music_list[i][1])
    workbook.save('music.xls')


if __name__ == '__main__':
    main()