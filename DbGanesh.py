#!/usr/bin/python
import MySQLdb

db=MySQLdb.Connect("localhost","root","root","Eduction")
print "Database name is =%s"%db
curssor=db.curssor()
sql="SELECT * FROM Student where Email=`Ganesh@gmail.com`"

print "Hello"
