#!/usr/bin/python
from __future__ import print_function
n=int(raw_input("please enter the number"))
for i in range(n):
	j=i+1
	for n in range(j):
		print('*',end='')
	print()

print('------------------------------------------------------')
for i in range(0,n):
	for j in range(0,n):
		print("*",end='')
		n=n-1
	print('')
