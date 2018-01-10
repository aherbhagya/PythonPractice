#!/usr/bin/python

dict={"Name":"mahesh","Age":25,"Company":"dp","contact":7875,"language":"english"}

# using str() to display dictionary
print str(dict)

# using items() 

print dict.items()
# find length of dict 
print len(dict)

# copy one dictionary to other

dict2={}
dict2=dict.copy()
print dict.items()
# get values
print dict.values()

# get keys
print dict.keys()

dict3={"id":12345}

# arange the sequnce in tuple 

sequ=("Name","id","Age","contact")
dict2.update(dict3)
print dict2.items()

# use forekeys

dict=dict.fromkeys(sequ,5)
print dict.items()
# use has_key method for checking key is present or not
if dict.has_key("contact"):
	print "contact is present"
else : 
	print " contact is not present"

# get method it return index on id element
print dict.get("id","not present")

dict5={"A":1,"B":"mahi","C":""}
print dict5.get("A")
print dict5.get("")
print dict5.get("z")
print dict5.get("z","not define")
print dict5.get("C")

# get values
print dict.values()