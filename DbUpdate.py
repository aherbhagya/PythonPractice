#!/usr/bin/python
import MySQLdb
db=MySQLdb.Connect("localhost","root","root","Eduction")
print "1"
cursor=db.cursor()
sql="""UPDATE Student SET Contact_Number=12345 WHERE Email=`mohan@gmail.com` """
print "2"
try :
	cursor.execute(sql)
	db.commit()
	print "3"
except :
	db.rollback()
	print "4"
db.close()
