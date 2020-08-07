import pymysql

try:
    con = pymysql.connect('localhost', 'root', '123456', 'train', charset='utf8')
    cur = con.cursor()
    cur.execute('select *from student')
    for ret in cur.fetchall():
        print(ret)
    # ret = cur.fetchone()
    cur.close()
    con.close()
except pymysql.Error as e:
    print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
