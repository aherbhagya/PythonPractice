import json 
f =  open("newdata3.json", "r") 
data = f.read()
jsondata = json.loads(data)
f.close()
fw =  open("newdata5.json", "w") 
json.dump(jsondata,fw, indent=2)
fw.close()