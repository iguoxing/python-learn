import pymysql

#1.创建与数据库连接对象
db = pymysql.connect(host='localhost', user='root', password='Xing0309!', port=3306, db='caizhi')
#2.利用db方法创建游标对象
cursor = db.cursor()
#3.利用游标对象execute()方法执行SQL命令
#cur.execute(";") #这里填写正确的SQL语句  例如:
sql = 'select * from user;'
#4.提交到数据库执行
cursor.execute(sql)
D = cursor.fetchall()
print(D)
#5.关闭游标对象
cursor.close()
#6.断开数据库连接
db.close()