#!/usr/bin/python
import math
def jumpSearching(lst,n,x):
	step=math.sqrt(n)
	prev=0
	while lst[int(min(step,n-1))]< x :
		prev=step
		step +=math.sqrt(n)
		if prev>=n :
			return -1
	while lst[int(prev)] < x:
		prev +=1
		if prev==min(step,n) :
			return -1
	if lst[int(step)]== x:
		return prev
	return -1
lst=[10,12,23,45,56,78,79,88,89,90,95,98,100,102,302,504,800,1000]
n=len(lst)
x=45
print jumpSearching(lst,n,x)
