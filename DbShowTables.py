#!/usr/bin/python
import MySQLdb
db=MySQLdb.Connect("localhost","root","root","Eduction")
cursor=db.cursor()
cursor.execute("SHOW TABLES")
data=cursor.fetchall()
for row in data:
	dbname = row[0]
	print "db name is =%s"%dbname
db.close()