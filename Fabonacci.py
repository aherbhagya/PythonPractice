def febonacci(no):
	f1=1
	f2=2
	for i in range(no) :
		f3=f1+f2
		f1=f2
		f2=f3
		print f2
no=5
print febonacci(no)