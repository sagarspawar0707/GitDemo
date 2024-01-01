import mysql.connector
from utilites.configurations import *

#host,database,user,password
#conn=mysql.connector.connect(host='localhost',database='APIDevelop'
 #                       ,user='root',password='Shaunak@11')
conn=getconnction()
print(conn.is_connected())
cur=conn.cursor()
"""
cur.execute('Select * from Books')
#row=cur.fetchone()
#print(row)
#print(row[3])
all=cur.fetchall()
print(all)
print(all[0])
"""
cur.execute("select * from customerinfo")
rows=cur.fetchall()
print(rows)
sum=0
for row in rows:
    print(row[2])
    sum=sum+row[2]

print(sum)
query="update customerinfo set location=%s where CourseName=%s"
data=("UK","Jmeter")
cur.execute(query,data)
conn.commit()
cur.execute("INSERT INTO CustomerInfo values('Webservices',CURRENT_DATE(),76,'India')")
conn.commit()

conn.close()