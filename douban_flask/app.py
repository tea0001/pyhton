from flask import Flask, render_template

import jieba                            # 分词
from matplotlib import pyplot as plt    # 绘图,数据可视化
from wordcloud import WordCloud         # 词云
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运输
import sqlite3                          # 数据库
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    return index()
    # return render_template('index.html')


@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('movie.html', datalist=datalist)


@app.route('/word')
def work():
    # conn = sqlite3.connect('movie.db')
    # cur = conn.cursor()
    # sql = 'select instroduction from movie250'
    # data = cur.execute(sql)
    # text = ''
    # for item in data:
    #     text = text + item[0]
    # cur.close()
    # conn.close()
    # # 语句进行分词
    # cut = jieba.cut(text)
    # string = ' '.join(cut)
    # #
    # img = Image.open('tree.jpg')  # 打开遮罩图片
    # img_array = np.array(img)  # 将图片转换成数组
    # wc = WordCloud(
    #     background_color='white',
    #     mask=img_array,
    #     font_path='STXINGKA.TTF'
    # )
    # wc.generate_from_text(string)
    #
    # # 绘制图片
    # fig = plt.figure(1)
    # plt.imshow(wc)
    # plt.axis('off')  # 是否显示坐标轴
    # # plt.show()
    # plt.savefig('static/assets/img/word.jpg')
    return render_template('word.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/score')
def score():
    xdata = []
    ydata = []
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select score,count(score) from movie250 group by score'
    data = cur.execute(sql)
    for item in data:
        xdata.append(item[0])
        ydata.append(item[1])
    cur.close()
    conn.close()
    return render_template('score.html', xdata=xdata, ydata=ydata)


if __name__ == '__main__':
    app.run()
