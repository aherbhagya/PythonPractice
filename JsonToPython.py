import json 

f =  open("newdata3.json", "r") 
data = f.read()

jsondata = json.loads(data)

print jsondata  # all json file
print "*********************"
print jsondata["Records"]  # list after dictionary
print "*********************"
print jsondata["Records"][0]  # first element of list

f.close()