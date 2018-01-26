#!/usr/bin/python
def bubbleSort(lst):
	n=len(lst)
	for i in range(n):
		for j in range(0,n-i-1,):
			if lst[j]>lst[j+1] :
				lst[j],lst[j+1] = lst[j+1],lst[j]
	

lst=[10,9,56,21,45,36,12,3,51,11,30,52,32,7,6,51,60,6446,35,39]
bubbleSort(lst)
for i in range(len(lst)):
	print lst[i]
