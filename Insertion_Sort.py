#!/usr/bin/python
def insertion_sort(lst):
	for i in range(len(lst)):
		key=lst[i]
		j=i-1
		while j>=0 and key<lst[j] :
			lst[j+1]=lst[j]
			j -=1
		lst[j+1]=key
lst=[15,23,12,14,15,41,31,54,4,34,53,23,2,43,45,9,23,34,45]
insertion_sort(lst)
for i in range(len(lst)):
	print lst[i]   
 