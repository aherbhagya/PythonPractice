#!/usr/bin/python
n=int(input("enetr the input")) 
width = len("{0:b}".format(n)) 
for num in range(1,n+1):
     print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(num, width=width))