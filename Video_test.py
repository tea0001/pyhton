# -*- coding = utf-8 -*-
# @Time : 2020/8/9 20:21
# @Author : tea
# @File : Video_test.py
# @Software: PyCharm
import json
import time
import sqlite3
import requests


def saveData():
    url = 'http://liuyan.people.com.cn/threads/queryThreadsList'
    headers = {
        "Referer": "http://liuyan.people.com.cn/threads/list?fid=539&tdsourcetag=s_pctim_aiomsg",
    }
    params = {
        'fid': '539',
        'lastItem': '0'
    }

    information_all = []
    response = requests.post(url=url, data=params, headers=headers)
    information_list = json.loads(response.text)
    con = sqlite3.connect('LiuYanBan')
    cur = con.cursor()
    while len(information_list['responseData'])==10:
        for i in range(0, len(information_list['responseData'])):
            sql = '''
            insert into Information
            values(%d,'%s','%s','%s','%s','%s','%s')
            ''' % (int(information_list['responseData'][i]['tid']), information_list['responseData'][i]['nickName'],
                   information_list['responseData'][i]['subject'], information_list['responseData'][i]['content'],
                   time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(information_list['responseData'][i]['dateline']))), information_list['responseData'][i]['typeName'],
                   information_list['responseData'][i]['domainName'])

            try:
                cur.execute(sql)
                con.commit()
                print(sql)
            except:
                con.rollback()
                exit(0)

        params['lastItem'] = information_list['responseData'][9]['tid']
        response = requests.post(url=url, data=params, headers=headers)
        information_list = json.loads(response.text)


if __name__ == '__main__':
    saveData()