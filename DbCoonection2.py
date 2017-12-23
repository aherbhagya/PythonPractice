#!/usr/bin/python
import MySQLdb

db=MySQLdb.Connect("localhost","root","root","Eduction")
print "1"
cursor=db.cursor()
sql="SELECT * FROM Address"
print "2"
cursor.execute(sql)
print "3"
data=cursor.fetchall()
print "4"
try :
	for row in data:
		fname = row[0]
		print "First Name =%s"%fname
except :
	print "Exception is occure"
db.close()