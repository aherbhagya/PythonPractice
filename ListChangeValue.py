#!/usr/bin/python
# please execute this program line by line
import this
# chnage the value at 3 postion
li=[1,2,3,1,3,5,4,5,6,7]
print li
# add new element at 3th location it remove the 3 location value and add new value
li[3]=124
print li

# print the list length
print len(li)

# print list start with end index

print li[3:]
print li[:3]
# add new element at end
li.append(1245)
# remove duplicate
print set(li)
# delete 2th element
del li[2]
print li

# print the list with index
for key,value in enumerate(li):

	print key,value
# to identify data type or structure 
print type(li)