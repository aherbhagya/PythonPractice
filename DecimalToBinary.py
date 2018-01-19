
def toBinary(no):
	lst=[]
	index=1
	while no!=0 :
		lst[index+1]=no%2
		no=no/2
	return lst
no=6
print toBinary(no)