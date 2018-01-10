#!/usr/bin/python
from collections import OrderedDict
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
for key, values in d.items():
	print key,values
od=OrderedDict(	)
od["A"]=5
od["B"]=2
od["Z"]=3
od["D"]=4
for key,values in od.items():
	print key,values