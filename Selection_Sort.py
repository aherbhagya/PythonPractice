#!/usr/bin/python
def slectionSort(lst,n):
	for i in range(n):
		mix_id=i
		for j in range(i+1,len(lst)):
			if lst[mix_id]>lst[j] :
				min_id=j
		lst[i],lst[min_id]=lst[min_id],lst[i]

lst=[5,2,12,50,15,21,9,11,30,50,30]
n=len(lst)
lst=slectionSort(lst,n)
print lst
