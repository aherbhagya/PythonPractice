#!/usr/bin/python
string=raw_input("enter the string")
str2=[]
length=len(string)
print length
def reversestr():
	while length>=1:
		str3=string[length]
		length=length-1
	return str3
print reversestr
