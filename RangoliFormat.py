#!/usr/bin/python
from __future__ import print_function
j=int(raw_input("please enter the number"))
for i in range(j):
	n=j+1
	for l in range(n-i):
		print(end=' ')
	for k in range(i):
		print("*",end="")
	for m in range(i):
		print("*",end="")
	print("")
for a in range(n):
	for k in range(a):
		print(" ",end="")
	for l in range(n):
		print("*",end="")
	for m in range(n):
		print("*",end="")
	n=n-1
	print("")
print("--------------------------------------------------")
n=int(raw_input("please enter the number"))


for i in range(n):
	j=i+1
	for n in range(j):
		print('*',end='')
	print()
print('------------------------------------------------------')
n=int(raw_input("please enter the number"))


for i in range(n):
	for l in range(n-i):
		print(end=' ')
	for k in range(i):
		print("*",end="")
	print("")

