#!/usr/bin/python
import MySQLdb
db=MySQLdb.Connect("localhost","root","root","Eduction")
cursor=db.cursor()
sql="""INSERT INTO Student(First_Name,Last_Name,Age,Gender,Email,Languages,Contact_Number,Department,Year) VALUES("Mohan","patil",28,"Male","mohan@gmail.com","Hindi",7875,"Mech","2nd");"""
try:
	cursor.execute(sql)
	db.commit()
except :
	db.rollback()
db.close()

