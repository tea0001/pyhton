import pickle

f = open('example.txt', 'wb')
a = 'hello word'
b = [1, 2, 3, 4, 5, 6]
c = 1, 2, 3, 7, 9
d = {'星期一': 'Monisday'}
try:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)
    pickle.dump(d, f)
finally:
    f.close()
with open('example.txt', 'rb') as f:
    n = pickle.load(f)  #这是python2才可以的--获取文件的数据个数
    for i in range(n):
        x = pickle.load(f)
        print(x)
    f.close()
