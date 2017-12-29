import json 
jsondata1 = []
dict = {}
file_txt = open("newdata5.json")
data = file_txt.read()
jsondata = json.loads(data)
list1 =  jsondata["Records"]
print list1
for val in list1:  #val dictionary item of list 
	line = val["record"]
	line2 = val["ID"]
	print line2  # line by record key
	print line
	flag=  line.find("mill")
	if (flag >-1):
		jsondata1.append(val) 
dict["sports"] = jsondata1
file_json= open("newdata6.json", "w")
json.dump(sort(dict),file_json, indent=2)
file_txt.close()
file_json.close()