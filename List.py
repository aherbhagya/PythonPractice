#!/usr/bin/python
li=[1,2,3,4,5,6,7,8,9,0]
def normal(li):
	sum=0
	for i in li:
		sum=sum+i
	return sum
print normal(li)

name=raw_input("enter the name")
print "your name is : ",name
length=len(name)
print "length of string is:", length
while length>=1:
	print name[length-1]
	length=length-1

