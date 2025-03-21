# 19.03.2025

import pymysql

conn = pymysql.connect(host='127.0.0.1',port = 3306,user='root',password='root',database='')

cur = conn.cursor()
create_sql = 'CREATE TAble demo (id int,name Varchar(100),age int);'
cur.execute(create_sql)
insert_sql = 'Insert INTO demo(age,id,name) values(18,2,"Wolfgang");'
cur.execute(insert_sql)



cur.close()
conn.close()