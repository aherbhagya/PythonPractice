#!/usr/bin/python
import MySQLdb
db=MySQLdb.Connect("localhost","root","root","Eduction")
cursor=db.cursor()
sql="CREATE TABLE Student(First_Name varchar(30),Last_Name varchar(30),Age int(20),Gender varchar(30),Email varchar(50),Languages Varchar(100),Contact_Number int(20),Department varchar(30),Year varchar(20))"
cursor.execute(sql)
db.close()