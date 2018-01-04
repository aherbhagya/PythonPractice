#!/usr/bin/python
lst=filter(lambda x : x%2==0 , range(1,20))
print lst
#list is return odd number of 1 to 20 after that lambda return the if squer root is devigible by 5
lst1=filter(lambda x : x%5==0 , [x**2 for x in range(1,21) if x%2!=0])
print lst1
