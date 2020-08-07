# -*- coding = utf-8 -*-
# @Time : 2020/8/6 20:07
# @Author : 姚远
# @File : testCloud.py
# @Software: PyCharm


import jieba                            # 分词
from matplotlib import pyplot as plt    # 绘图,数据可视化
from wordcloud import WordCloud         # 词云
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运输
import sqlite3                          # 数据库

# 准备词云所需要的文字
conn = sqlite3.connect('movie.db')
cur = conn.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
cur.close()
conn.close()
# 语句进行分词
cut = jieba.cut(text)
string = ' '.join(cut)
#
img = Image.open('tree.jpg')       # 打开遮罩图片
img_array = np.array(img)                               # 将图片转换成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='STXINGKA.TTF'
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')                                         # 是否显示坐标轴
# plt.show()
plt.savefig('word.jpg')
