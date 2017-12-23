#!/usr/bin/python
import MySQLdb
db=MySQLdb.Connect("localhost","root","root","Eduction")
cursor=db.cursor()
cursor.execute("DESCRIBE Student")
data=cursor.fetchall()
print data
db.close()