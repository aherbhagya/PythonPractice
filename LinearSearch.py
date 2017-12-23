#!/usr/bin/python
def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1
arr=[12,32,54,1,2,34,54,65,76,34,65,76]
print search(arr,65)