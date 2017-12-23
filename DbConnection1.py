#!/usr/bin/python
import MySQLdb

print "Database connection"
db=MySQLdb.Connect("localhost","root","root","Eduction")
print " Driver loded successfully"
cursor=db.cursor()
print "database is  %s"%db

cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print "data base version is = %s"%data
db.close()
print "database is after closing %s"%db


