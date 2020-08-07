# -*- coding = utf-8 -*-
# @Time : 2020/8/3 19:24
# @Author : 姚远
# @File : train.py
# @Software: PyCharm

for i in range(1, 10):
    for j in range(1, i):
        print("{}*{}={}".format(i, j, i * j), end="\t")
    print('\n')
