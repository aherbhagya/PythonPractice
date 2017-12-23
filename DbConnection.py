#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","Eduction" )
print "db connect success"

# prepare a cursor object using cursor() method
cursor = db.cursor()
print "cursor success"

sql = "SELECT * FROM Address"
print "sql success"
try:
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      email = row[2]
      mobileno = row[3]
      uname = row[4]
      password = row[5]
      # Now print fetched result
      print "fname=%s,lname=%s,email=%s,mobileno=%s,uname=%s,password=%s" % \
             (fname, lname, email, mobileno, uname,password )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()