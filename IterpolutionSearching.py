#!/usr/bin/python
def interPolution(lst,n,x):
	lo=0 
	hi=n-1
	while hi>=lo and x>=lst[lo] and x<=lst[hi]:
		pos= lo + (hi - lo)/(lst[hi]-lst[lo]) * (x-lst[lo])
		print pos
		if lst[pos]== x :
			return pos
		if lst[pos]< x :
			lo = pos +1
		else :
			hi= pos - 1	
lst=[10,20,30,40,56,78,85,89,92,96,99,101,105,109,120,130,140,155]
n=len(lst);
x=109
result=interPolution(lst,n,x)
if result !=-1 :
	print "element fround at index location ", result
else :
	print "elemnt not found"