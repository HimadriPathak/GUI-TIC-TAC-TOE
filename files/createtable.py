import pymysql as sql
conn=sql.connect(host='localhost',user='root',passwd='root',db='test')
c=conn.cursor()
print('done')

c.execute('''create table record (Name char(20),Gameplayed int(10),
          Win int(10),Loss int(10),Draw int(10))''')
conn.commit()



